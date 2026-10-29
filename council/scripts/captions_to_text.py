#!/usr/bin/env python3
"""Convert YouTube json3 caption files to timestamped plain text.

Usage: python3 captions_to_text.py <folder>

For every <id>*.json3 in <folder>, writes <id>.txt with lines like
"[mm:ss] text", merging caption events into roughly sentence-sized lines.
Part of the Meteoric Council's /add-advisor skill.
"""
import json
import sys
from pathlib import Path


def stamp(ms: int) -> str:
    s = ms // 1000
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}"


def convert(path: Path) -> Path:
    data = json.loads(path.read_text(encoding="utf-8"))
    lines, buf, start = [], [], None
    for ev in data.get("events", []):
        segs = ev.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs).replace("\n", " ").strip()
        if not text:
            continue
        if start is None:
            start = ev.get("tStartMs", 0)
        buf.append(text)
        joined = " ".join(buf)
        if len(joined) > 220 or joined.endswith((".", "?", "!")):
            lines.append(f"[{stamp(start)}] {joined}")
            buf, start = [], None
    if buf:
        lines.append(f"[{stamp(start or 0)}] {' '.join(buf)}")
    video_id = path.name.split(".")[0]
    out = path.with_name(f"{video_id}.txt")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = Path(sys.argv[1]).expanduser()
    files = sorted(folder.glob("*.json3"))
    if not files:
        sys.exit(f"No .json3 files in {folder}")
    for f in files:
        out = convert(f)
        print(f"{f.name} -> {out.name}")


if __name__ == "__main__":
    main()
