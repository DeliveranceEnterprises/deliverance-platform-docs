"""Give every heading of the translated pages the anchor of its English heading, so links work in every language."""
import re
import sys
import unicodedata
from pathlib import Path

DOCS = Path(__file__).parent / "docs"
HEADING = re.compile(r"^(#{1,6}) (.*?)(?: \{#([\w-]+)\})?$")


def headings(lines):
    fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and (m := HEADING.match(line)):
            yield i, m


def slug(text):
    text = re.sub(r"\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[-\s]+", "-", re.sub(r"[^\w\s-]", "", text).strip().lower())


failed = False
for source in sorted(DOCS.rglob("*.en.md")):
    slugs, seen = [], {}
    for _, m in headings(source.read_text().split("\n")):
        s = slug(m[2])
        seen[s] = seen.get(s, -1) + 1
        slugs.append((m[1], f"{s}_{seen[s]}" if seen[s] else s))
    for lang in ("es", "zh"):
        page = source.with_name(source.name.replace(".en.md", f".{lang}.md"))
        if not page.exists():
            print("missing", page.relative_to(DOCS))
            failed = True
            continue
        lines = page.read_text().split("\n")
        found = list(headings(lines))
        if [m[1] for _, m in found] != [level for level, _ in slugs]:
            print("different headings", page.relative_to(DOCS))
            failed = True
            continue
        for (i, m), (level, s) in zip(found, slugs):
            lines[i] = f"{level} {m[2]} {{#{s}}}"
        page.write_text("\n".join(lines))
sys.exit(failed)
