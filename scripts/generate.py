#!/usr/bin/env python3
"""Read src/*.yaml and write rule/{Clash,Stash,Surge,Shadowrocket}/*.{yaml,list}."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
src_dir = root / "src"

OUTPUT_NAMES = {
    "claude": "Claude",
    "google-ai": "GoogleAI",
    "grok": "Grok",
    "meta-ai": "MetaAI",
    "openai": "OpenAI",
}


def output_name(path: Path) -> str:
    return OUTPUT_NAMES.get(path.stem, path.stem)


def strip_no_resolve(rule: str) -> str:
    suffix = ",no-resolve"
    return rule[: -len(suffix)] if rule.endswith(suffix) else rule


def parse(path: Path):
    header, body, in_body = [], [], False
    for line in path.read_text().splitlines():
        s = line.strip()
        if not in_body:
            if s == "rules:":
                in_body = True
            elif s.startswith("#") or s == "":
                header.append(s)
            continue
        if s == "":
            body.append(("blank", ""))
        elif s.startswith("#"):
            body.append(("comment", s))
        elif s.startswith("- "):
            body.append(("rule", s[2:]))
    return header, body


sources = [(output_name(p), parse(p)) for p in sorted(src_dir.glob("*.yaml"))]
expected_names = {name for name, _ in sources}

for client, fmt in (("Clash", "yaml"), ("Stash", "list"), ("Surge", "list"), ("Shadowrocket", "list")):
    d = root / "rule" / client
    d.mkdir(parents=True, exist_ok=True)
    for stale in d.glob(f"*.{fmt}"):
        if stale.stem not in expected_names:
            stale.unlink()
            print(f"removed {stale.name} <- rule/{client}")
    for name, (header, body) in sources:
        out = list(header)
        if fmt == "yaml":
            out.append("payload:")
            for kind, value in body:
                if kind == "blank":
                    out.append("")
                elif kind == "comment":
                    out.append(f"  {value}")
                else:
                    out.append(f"  - {value}")
            (d / f"{name}.yaml").write_text("\n".join(out) + "\n")
        else:
            for kind, value in body:
                if kind == "blank":
                    out.append("")
                elif kind == "comment":
                    out.append(value)
                else:
                    out.append(strip_no_resolve(value))
            (d / f"{name}.list").write_text("\n".join(out) + "\n")
        print(f"wrote {name}.{fmt} -> rule/{client}")
