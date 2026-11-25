"""Give each language its own search index: the plugin builds a single one, which mixes their results."""
import json
import re
from pathlib import Path

SITE = Path(__file__).parent / "site"
LANGS = ("es", "zh")
BASE = re.compile(r'(<script id="?__config"?[^>]*>\{"annotate": [^<]*?"base": ")([^"]*)(")|(<script id="?__config"?[^>]*>\{"base": ")([^"]*)(")')

index_file = SITE / "search" / "search_index.json"
index = json.loads(index_file.read_text())
rest = index["docs"]
for lang in LANGS:
    prefix = f"{lang}/"
    docs = [{**d, "location": d["location"].removeprefix(prefix)} for d in rest if d["location"].startswith(prefix)]
    rest = [d for d in rest if not d["location"].startswith(prefix)]
    if not docs:
        raise SystemExit(f"no {lang} pages in the search index")
    out = SITE / lang / "search" / "search_index.json"
    out.parent.mkdir(exist_ok=True)
    config = {**index["config"], "lang": ["en", lang], "separator": r"[\s\u200b\-]+"}
    out.write_text(json.dumps({"config": config, "docs": docs}, ensure_ascii=False))
    # The pages look for the index, and resolve its results, from "base"
    for page in (SITE / lang).rglob("*.html"):
        depth = len(page.relative_to(SITE / lang).parts) - 1
        base = "/".join([".."] * depth) or "."
        text, n = BASE.subn(lambda m: (m[1] or m[4]) + base + (m[3] or m[6]), page.read_text())
        if n != 1:
            raise SystemExit(f"no search base in {page}")
        page.write_text(text)
index["docs"] = rest
index["config"]["lang"] = ["en"]
index_file.write_text(json.dumps(index, ensure_ascii=False))
