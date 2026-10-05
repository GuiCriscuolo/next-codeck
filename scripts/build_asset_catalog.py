#!/usr/bin/env python3
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT_JSON = ASSETS / "asset-catalog.json"
OUT_MD = ASSETS / "asset-catalog.md"
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
STOP = {"pexels","unsplash","photo","image","png","jpg","jpeg","webp","the","and","with","for","using","from","of","in","a","an"}
def keywords(name):
    s = Path(name).stem.lower()
    s = re.sub(r"[_\\-]+", " ", s)
    s = re.sub(r"\\b\\d+\\b", " ", s)
    return list(dict.fromkeys(w for w in re.findall(r"[a-z0-9]+", s) if w not in STOP))
items = []
for folder in ("icons", "photos"):
    d = ASSETS / folder
    if d.exists():
        for p in sorted(d.rglob("*")):
            if p.is_file() and p.suffix.lower() in EXTS:
                rel = p.relative_to(ASSETS).as_posix()
                typ = "icon" if folder == "icons" else "photo"
                items.append({"id": rel.rsplit(".",1)[0].replace("/","__"), "path": rel, "type": typ, "filename": p.name, "keywords": keywords(p.name)})
catalog = {"schema_version":"1.0", "generated_from":"assets/", "asset_count":len(items), "icons":sum(x["type"]=="icon" for x in items), "photos":sum(x["type"]=="photo" for x in items), "assets":items}
OUT_JSON.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
lines = ["# Next Codeck Asset Catalog", "", "Generated automatically from assets/.", "", "| Type | Asset | Keywords | Path |", "|---|---|---|---|"]
for x in items: lines.append("| {} | {} | {} | `{}` |".format(x["type"], x["filename"], ", ".join(x["keywords"]), x["path"]))
OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")