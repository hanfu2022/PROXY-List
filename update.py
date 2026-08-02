from pathlib import Path
from sources import fetch_sources
from checker import check_all

out=Path("output")
out.mkdir(exist_ok=True)

items=fetch_sources()
alive=check_all(items)

(out/"http.txt").write_text("\n".join(alive), encoding="utf-8")
(out/"socks4.txt").write_text("", encoding="utf-8")
(out/"socks5.txt").write_text("", encoding="utf-8")

print("Updated:", len(alive))
