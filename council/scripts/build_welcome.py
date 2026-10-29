#!/usr/bin/env python3
"""Fill the council welcome page with an owner's data.

Usage: python3 council/scripts/build_welcome.py council/welcome-data.json [council/welcome.html]

Reads council/templates/welcome.html, swaps the JSON inside
<script type="application/json" id="council-data"> for the given file
(validated first), applies the owner's brand theme if the data has one,
and writes the finished page. Part of the Meteoric
Council's /council-start skill.
"""
import json
import re
import sys
from pathlib import Path

REQUIRED = ["owner", "headline", "lede", "goal", "seats", "asks", "rituals", "coach", "gaps", "answers", "councils"]
BLOCK = re.compile(r'(<script type="application/json" id="council-data">)(.*?)(</script>)', re.S)
THEME = re.compile(r"/\*THEME\*/.*?/\*/THEME\*/", re.S)
FONTS = re.compile(r"<!--FONTS-->.*?<!--/FONTS-->", re.S)
TOKENS = ["bg", "surface", "ink", "mute", "line", "panel", "on-panel", "on-panel-mute",
          "accent", "on-accent", "accent-ink", "seed", "warn"]
COLOR = re.compile(r"^#[0-9A-Fa-f]{3,8}$|^rgba?\([0-9., %]+\)$")
SAFE_FONT = re.compile(r"^[A-Za-z0-9 ,\"'\-]+$")


def theme_css(theme: dict) -> str:
    """Build the token block from the owner's brand: light on :root, dark in both dark blocks."""
    light, dark = theme.get("light") or {}, theme.get("dark") or theme.get("light") or {}
    for name, pal in (("light", light), ("dark", dark)):
        bad = [t for t in TOKENS if not COLOR.match(str(pal.get(t, "")))]
        if bad:
            sys.exit(f"theme.{name} needs a colour for: {', '.join(bad)}")
    fonts = theme.get("fonts", {})
    fam = {k: fonts.get(k, d) for k, d in (
        ("display", '"Inter","Helvetica Neue",Helvetica,Arial,sans-serif'),
        ("serif", fonts.get("display", '"Inter","Helvetica Neue",Helvetica,Arial,sans-serif')),
        ("mono", '"JetBrains Mono","SF Mono",Menlo,Consolas,monospace'))}
    for k, v in fam.items():
        if not SAFE_FONT.match(v):
            sys.exit(f"theme.fonts.{k} has characters a font stack can't have")
    decl = lambda pal: " ".join(f"--{t}:{pal[t]};" for t in TOKENS)
    return ("/*THEME*/\n"
            f":root{{ {decl(light)} --display:{fam['display']}; --serif:{fam['serif']}; --mono:{fam['mono']}; }}\n"
            f'@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{ {decl(dark)} color-scheme:dark}}}}\n'
            f':root[data-theme="dark"]{{ {decl(dark)} color-scheme:dark}}\n'
            "/*/THEME*/")


def fonts_link(theme: dict) -> str:
    q = (theme.get("fonts") or {}).get("google")
    if not q:
        return None
    if not re.match(r"^[A-Za-z0-9+:;,@.&=_-]+$", q):
        sys.exit("theme.fonts.google must be the query part of a Google Fonts css2 URL")
    return f'<!--FONTS--><link rel="stylesheet" href="https://fonts.googleapis.com/css2?{q}&display=swap"><!--/FONTS-->'


def main() -> None:
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    here = Path(__file__).resolve().parent
    template = here.parent / "templates" / "welcome.html"
    data_path = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else here.parent / "welcome.html"

    data = json.loads(data_path.read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED if k not in data]
    if missing:
        sys.exit(f"welcome data is missing: {', '.join(missing)}")
    data.setdefault("example", False)

    page = template.read_text(encoding="utf-8")
    theme = data.get("theme")
    if theme:
        page = THEME.sub(lambda m: theme_css(theme), page, count=1)
        link = fonts_link(theme)
        if link:
            page = FONTS.sub(lambda m: link, page, count=1)
    payload = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    page, n = BLOCK.subn(lambda m: m.group(1) + "\n" + payload + "\n" + m.group(3), page, count=1)
    if n != 1:
        sys.exit("template has no council-data block")
    out.write_text(page, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
