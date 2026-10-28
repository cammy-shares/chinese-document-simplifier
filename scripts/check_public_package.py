#!/usr/bin/env python3
"""Check the release file set, references, and common privacy leak patterns."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "chinese-document-simplifier"
PATTERNS = {
    "absolute local user path": re.compile(r"(?:/Users/|/home/)[A-Za-z0-9_.-]+|[A-Z]:\\Users\\[^\\\s]+"),
    "personal email": re.compile(r"[A-Za-z0-9_.+-]+@(?!users[.]noreply[.]github[.]com)[A-Za-z0-9.-]+[.][A-Za-z]{2,}"),
    "GitHub credential": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "private workspace link": re.compile(r"https?://[^\s/]+[.](?:feishu[.]cn|larksuite[.]com)/(?:docx|wiki|base)/"),
}
REQUIRED = [
    "README.md", "README.zh-CN.md", "README.en.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
    "CONTRIBUTING.md", "examples.md", "EVALUATION.md", "CHANGELOG.md",
    "skills/chinese-document-simplifier/SKILL.md",
    "skills/chinese-document-simplifier/LICENSE",
    "skills/chinese-document-simplifier/THIRD_PARTY_NOTICES.md",
    "skills/chinese-document-simplifier/references/modes-and-files.md",
    "skills/chinese-document-simplifier/references/examples.md",
]
errors = []
for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")
allowed = {".md", ".py", ".yml", ".yaml", ".txt"}
count = 0
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or any(x in path.parts for x in [".git", "__pycache__"]):
        continue
    rel = str(path.relative_to(ROOT))
    if path.is_symlink():
        errors.append(f"symlink is not allowed: {rel}")
        continue
    if path.suffix not in allowed and path.name not in {"LICENSE", "CODEOWNERS", ".gitignore"}:
        errors.append(f"unexpected public file type: {rel}")
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"non-text file: {rel}")
        continue
    count += 1
    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            errors.append(f"{label}: {rel}")
skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
if not skill_text.startswith("---\nname: chinese-document-simplifier\n"):
    errors.append("skill name/frontmatter is inconsistent")
for rel in sorted(set(re.findall(r"(?:references|assets)/[A-Za-z0-9_./-]+", skill_text))):
    if not (SKILL / rel).is_file():
        errors.append(f"missing skill reference: {rel}")
for path in ROOT.rglob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        if target and not (path.parent / target).exists():
            errors.append(f"broken relative link: {path.relative_to(ROOT)} -> {target}")
print(f"Checked {count} public text files")
for error in errors:
    print("FAIL:", error)
if errors:
    sys.exit(1)
print("PASS: structure, relative links, and common privacy patterns")
print("Static checks do not prove semantic privacy or model behavior.")
