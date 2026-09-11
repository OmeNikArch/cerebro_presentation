"""Сборка деки из src/template.html: подстановка SVG-логотипов и сквозная нумерация слайдов.
Запуск из корня репозитория: python3 src/build.py -> index.html"""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent
t = (root / "template.html").read_text(encoding="utf-8")
full = (root / "assets" / "logo-full.paths.txt").read_text(encoding="utf-8")
mark = (root / "assets" / "logo-mark.paths.txt").read_text(encoding="utf-8")
body = t.replace("{{LOGO_FULL}}", full).replace("{{LOGO_MARK}}", mark)
counter = {"n": 1}  # обложка без номера, нумерация начинается с 02
def num(m):
    counter["n"] += 1
    return '<div class="num">%02d</div>' % counter["n"]
body = re.sub(r'<div class="num">\d+</div>', num, body)
total = body.count("<section")
body = re.sub(r'<span class="cnt" id="cnt">1 / \d+</span>', '<span class="cnt" id="cnt">1 / %d</span>' % total, body)
i = body.index('<div class="stack"')
head, rest = body[:i], body[i:]
doc = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       '<meta name="robots" content="noindex">\n'
       + head.strip() + "\n</head>\n<body>\n" + rest.strip() + "\n</body>\n</html>\n")
(root.parent / "index.html").write_text(doc, encoding="utf-8")
print("slides:", total, "| index.html:", len(doc.encode()), "bytes")
