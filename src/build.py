"""Собирает index.html из src/template.html, подставляя SVG-логотипы.
Запуск: python3 src/build.py (из корня репозитория)."""
import pathlib
root = pathlib.Path(__file__).resolve().parent
t = (root / "template.html").read_text(encoding="utf-8")
full = (root / "assets" / "logo-full.paths.txt").read_text(encoding="utf-8")
mark = (root / "assets" / "logo-mark.paths.txt").read_text(encoding="utf-8")
body = t.replace("{{LOGO_FULL}}", full).replace("{{LOGO_MARK}}", mark)
i = body.index('<div class="stack"')
head, rest = body[:i], body[i:]
doc = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<meta name="robots" content="noindex">\n'
       + head.strip() + "\n</head>\n<body>\n" + rest.strip() + "\n</body>\n</html>\n")
(root.parent / "index.html").write_text(doc, encoding="utf-8")
print("index.html:", len(doc.encode("utf-8")), "bytes")
