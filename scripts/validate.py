#!/usr/bin/env python3
"""Validate and build the skill and plugin ZIPs; stdlib only."""
from pathlib import Path
import json
import os
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "review-korean-writing"


def main():
    source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert source.startswith("---\n"), "Missing YAML frontmatter"
    _, frontmatter, body = source.split("---\n", 2)
    fields = dict(line.split(": ", 1) for line in frontmatter.strip().splitlines())
    assert fields["name"] == SKILL.name, "Skill name must match folder"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields["name"])
    assert 0 < len(fields["description"]) <= 1024
    assert body.strip(), "Empty skill instructions"
    files = sorted(p for p in SKILL.rglob("*") if p.is_file())
    assert not any(p.is_symlink() for p in SKILL.rglob("*")), "No external symlinks"
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            assert resolved.is_relative_to(ROOT), f"External local link: {path}: {target}"
            assert resolved.exists(), f"Broken local link: {path}: {target}"
            if path.is_relative_to(SKILL):
                assert resolved.is_relative_to(SKILL), f"Skill dependency outside package: {target}"
    out = ROOT / "dist" / f"{SKILL.name}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(SKILL.parent))
    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        assert f"{SKILL.name}/SKILL.md" in archive.namelist()
        assert len(archive.namelist()) == len(files)
    print(f"PASS: metadata, local links, self-contained package; {len(files)} files")
    print(f"Built {out}")
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert manifest["name"] == "korean-writing-review"
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Use a stable semantic version"
    if os.environ.get("GITHUB_REF_TYPE") == "tag":
        assert os.environ["GITHUB_REF_NAME"] == f"v{manifest['version']}", "Tag must match plugin version"
    interface = manifest["extensions"]["com.openai"]["interface"]
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "defaultPrompt"):
        assert interface[key], f"Missing plugin presentation: {key}"
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    assert len(marketplace["plugins"]) == 1
    entry = marketplace["plugins"][0]
    assert entry["name"] == manifest["name"]
    assert entry["source"] == {"source": "local", "path": "./"}
    assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    plugin_files = [ROOT / "plugin.json", ROOT / "LICENSE", *files]
    assert not any(p.is_symlink() for p in plugin_files), "No external symlinks"
    plugin_out = ROOT / "dist" / f"{manifest['name']}-plugin.zip"
    with zipfile.ZipFile(plugin_out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in plugin_files:
            archive.write(path, path.relative_to(ROOT))
    with zipfile.ZipFile(plugin_out) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {p.relative_to(ROOT).as_posix() for p in plugin_files}
        for path in plugin_files:
            assert archive.read(path.relative_to(ROOT).as_posix()) == path.read_bytes()
    print(f"PASS: plugin metadata, marketplace, ZIP contents; {len(plugin_files)} files")
    print(f"Built {plugin_out}")


if __name__ == "__main__":
    main()
