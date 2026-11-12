"""
sync_curriculum.py — Synchronizes data/curriculum.json into the embedded offline
<script id="kc-curriculum-fallback"> snapshot inside index.html.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON = os.path.join(ROOT, "data", "curriculum.json")
INDEX_HTML = os.path.join(ROOT, "index.html")


def main():
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    minified = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    minified = minified.replace("</script", "<\\/script")

    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(
        r'(<script\s+type="application/json"\s+id="kc-curriculum-fallback">)(.*?)(</script>)',
        re.DOTALL,
    )
    if not pattern.search(html):
        raise RuntimeError("Could not find #kc-curriculum-fallback tag in index.html")

    new_html = pattern.sub(lambda m: m.group(1) + minified + m.group(3), html, count=1)
    with open(INDEX_HTML, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_html)

    print(
        f"Synced {len(data.get('districts', []))} districts and "
        f"{sum(len(c.get('lessons', [])) for c in data.get('chapters', []))} lessons into index.html."
    )


if __name__ == "__main__":
    main()
