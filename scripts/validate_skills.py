# -*- coding: utf-8 -*-
"""Validate SKILL.md frontmatter against the agent-skills spec.

Checks: SKILL.md exists, YAML frontmatter present, `name` matches the parent
folder (lowercase a-z, 0-9, hyphens, <= 64 chars), `description` present and
<= 1024 chars, SKILL.md under 500 lines.

Usage: python scripts/validate_skills.py [root]
"""
import io
import os
import re
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skills")

errors = []
warnings = []
count = 0

for dirpath, dirnames, filenames in os.walk(root):
    if "SKILL.md" not in filenames:
        continue
    dirnames[:] = []
    count += 1
    rel = os.path.relpath(dirpath, root).replace("\\", "/")
    folder = os.path.basename(dirpath)
    text = io.open(os.path.join(dirpath, "SKILL.md"), encoding="utf-8",
                   errors="replace").read()
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        errors.append(rel + ": missing YAML frontmatter")
        continue
    body = stripped[3:]
    end = body.find("\n---")
    fm = body[:end] if end != -1 else body
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not m:
        errors.append(rel + ": frontmatter has no `name`")
    else:
        name = m.group(1).strip().strip('"').strip("'")
        if name != folder:
            warnings.append(rel + ": name `" + name + "` != folder `" + folder + "`")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
            warnings.append(rel + ": name `" + name + "` is not lowercase-hyphenated")
        if len(name) > 64:
            errors.append(rel + ": name longer than 64 chars")
    m = re.search(r"^description:\s*([\s\S]*?)(?=\n[A-Za-z_-]+:\s|\Z)", fm, re.M)
    if not m or not m.group(1).strip():
        errors.append(rel + ": frontmatter has no `description`")
    elif len(" ".join(m.group(1).split())) > 1024:
        errors.append(rel + ": description longer than 1024 chars")
    lines = text.count("\n") + 1
    if lines > 500:
        warnings.append(rel + ": SKILL.md is " + str(lines) + " lines (spec suggests < 500)")

print("skills checked: " + str(count))
print("errors: " + str(len(errors)))
for e in errors:
    print("  ERROR " + e)
print("warnings: " + str(len(warnings)))
for w in warnings[:40]:
    print("  warn  " + w)
if len(warnings) > 40:
    print("  ... " + str(len(warnings) - 40) + " more warnings")
sys.exit(1 if errors else 0)
