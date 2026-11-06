#!/usr/bin/env python3
"""Compile packages/*/package.yaml into dist/registry.json.zip + dist/checksums.txt."""
import hashlib, json, pathlib, sys, zipfile
import yaml

root = pathlib.Path(__file__).resolve().parent.parent
pkgs = [yaml.safe_load(p.read_text()) for p in sorted(root.glob("packages/*/package.yaml"))]
for p in pkgs:
    for k in ("name", "source", "bin"):
        assert k in p, f"{p.get('name', '?')}: missing {k}"

dist = root / "dist"
dist.mkdir(exist_ok=True)
(dist / "registry.json").write_text(json.dumps(pkgs, indent=2))
with zipfile.ZipFile(dist / "registry.json.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write(dist / "registry.json", "registry.json")
(dist / "checksums.txt").write_text(
    "".join(f"{hashlib.sha256((dist / f).read_bytes()).hexdigest()}  {f}\n"
            for f in ("registry.json", "registry.json.zip")))
print(f"built {len(pkgs)} package(s) -> {dist}", file=sys.stderr)
