#!/usr/bin/env python3
"""Check project-owned design records using only the Python standard library."""

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


FIELDS = {"id", "title", "layer", "status", "date", "depends_on", "approval"}
STATUSES = {"proposed", "approved", "superseded"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def read_metadata(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing metadata delimiters")
    header = text[4:].split("\n---\n", 1)[0]
    metadata = {}
    for line in header.splitlines():
        key, separator, raw = line.partition(":")
        if not separator or not re.fullmatch(r"[a-z_]+", key):
            raise ValueError(f"expected key: JSON value, got {line!r}")
        if key in metadata:
            raise ValueError(f"duplicate metadata field: {key}")
        metadata[key] = json.loads(raw, object_pairs_hook=unique_object)
    if set(metadata) != FIELDS:
        raise ValueError(f"metadata fields differ: {sorted(set(metadata) ^ FIELDS)}")
    return metadata


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def git(cwd, *args):
    return subprocess.check_output(
        ["git", "-C", str(cwd), *args], text=True, stderr=subprocess.PIPE
    ).strip()


def validate(root):
    errors = []
    records = {}
    decisions = root / "Docs/Design/Decisions"
    for path in sorted(decisions.glob("*.md")):
        label = str(path.relative_to(root))
        try:
            record = read_metadata(path)
            identifier = record["id"]
            if not isinstance(identifier, str) or not re.fullmatch(r"DEC-\d{4}", identifier):
                raise ValueError("invalid decision id")
            if not path.stem.startswith(identifier + "-"):
                raise ValueError("filename must start with decision id and a hyphen")
            if identifier in records:
                raise ValueError(f"duplicate decision id: {identifier}")
            if not nonempty(record["title"]) or not valid_date(record["date"]):
                raise ValueError("invalid title or date")
            if type(record["layer"]) is not int or record["layer"] not in range(5):
                raise ValueError("layer must be an integer from 0 to 4")
            if not isinstance(record["status"], str) or record["status"] not in STATUSES:
                raise ValueError("invalid decision status")
            dependencies = record["depends_on"]
            if not isinstance(dependencies, list) or any(not nonempty(d) for d in dependencies):
                raise ValueError("depends_on must be an array of decision ids")
            if len(dependencies) != len(set(dependencies)):
                raise ValueError("duplicate dependency")
            approval = record["approval"]
            if record["status"] in {"approved", "superseded"}:
                if not isinstance(approval, dict) or set(approval) != {"by", "date", "evidence"}:
                    raise ValueError("approved records require approval by, date and evidence")
                if approval["by"] != "user" or not valid_date(approval["date"]) or not nonempty(approval["evidence"]):
                    raise ValueError("approved records require user approval and nonempty evidence")
            elif approval is not None:
                raise ValueError("proposed decisions must have null approval")
            records[identifier] = record
        except (OSError, ValueError) as error:
            errors.append(f"{label}: {error}")

    if not records:
        errors.append("no valid decision records found")
    for identifier, record in records.items():
        for dependency in record["depends_on"]:
            if dependency not in records:
                errors.append(f"{identifier}: unknown dependency {dependency}")
            elif record["status"] == "approved" and records[dependency]["status"] != "approved":
                errors.append(f"{identifier}: approved decision depends on inactive {dependency}")

    visited, active = set(), set()

    def visit(identifier):
        if identifier in active:
            errors.append(f"dependency cycle at {identifier}")
            return
        if identifier in visited:
            return
        active.add(identifier)
        for dependency in records[identifier]["depends_on"]:
            if dependency in records:
                visit(dependency)
        active.remove(identifier)
        visited.add(identifier)

    for identifier in records:
        visit(identifier)

    documents = [root / "README.md", root / "AGENTS.md", root / "References/README.md"]
    documents.extend(sorted((root / "Docs").rglob("*.md")))
    for path in documents:
        try:
            body = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", body):
                link = urlsplit(target)
                if link.scheme or link.netloc or not link.path:
                    continue
                if not (path.parent / unquote(link.path)).exists():
                    errors.append(f"{path.relative_to(root)}: broken file link {target}")
        except OSError as error:
            errors.append(f"{path.relative_to(root)}: {error}")

    try:
        lock = json.loads((root / "References/sources.lock.json").read_text(encoding="utf-8"))
        if lock["version"] != 1 or not lock["sources"]:
            raise ValueError("invalid reference lock format")
        for source in lock["sources"]:
            reference = root / source["path"]
            if not (reference / ".git").exists():
                errors.append(f"{source['path']}: initialize the reference submodule first")
                continue
            if git(reference, "rev-parse", "HEAD") != source["commit"]:
                errors.append(f"{source['path']}: checkout differs from locked commit")
            entry = git(root, "ls-files", "--stage", "--", source["path"]).split()
            if entry[:2] != ["160000", source["commit"]]:
                errors.append(f"{source['path']}: indexed submodule differs from locked commit")
            configured_url = git(root, "config", "--file", ".gitmodules", "--get", f"submodule.{source['path']}.url")
            if configured_url != source["repository"]:
                errors.append(f"{source['path']}: submodule URL differs from source record")
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        errors.append(f"reference validation failed: {error}")
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    count = len(list((root / "Docs/Design/Decisions").glob("*.md")))
    print(f"PASS: {count} decisions; approval fields, dependencies, file links and reference pin checked.")
    print("This checks record structure, not actual consent, gameplay or balance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
