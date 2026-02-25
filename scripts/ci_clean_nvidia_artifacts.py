#!/usr/bin/env -S uv run --active --script --quiet
# /// script
# requires-python = ">=3.12"
# ///

import shutil
import site
import sysconfig
from pathlib import Path


candidate_paths: set[Path] = set()

for path in site.getsitepackages():
    candidate_paths.add(Path(path))

candidate_paths.add(Path(site.getusersitepackages()))

purelib = sysconfig.get_paths().get("purelib")
if purelib:
    candidate_paths.add(Path(purelib))

static_targets = [
    Path("nvidia"),
]

removed: list[str] = []

artifact_roots = [
    Path("dist") / "main" / "_internal",
    Path("main") / "_internal",
]

artifact_targets = [
    Path("nvidia"),
]

artifact_globs = [
    "torch/lib/libtorch_cuda*.so*",
]

for base_path in sorted(candidate_paths):
    if not base_path.exists():
        continue

    for rel_target in static_targets:
        target_path = base_path / rel_target
        if target_path.exists():
            if target_path.is_dir():
                shutil.rmtree(target_path, ignore_errors=True)
            else:
                target_path.unlink(missing_ok=True)
            removed.append(str(target_path))

    for dist_info in base_path.glob("nvidia*dist-info"):
        shutil.rmtree(dist_info, ignore_errors=True)
        removed.append(str(dist_info))

for artifact_root in artifact_roots:
    if not artifact_root.exists():
        continue

    for rel_target in artifact_targets:
        target_path = artifact_root / rel_target
        if target_path.exists():
            if target_path.is_dir():
                shutil.rmtree(target_path, ignore_errors=True)
            else:
                target_path.unlink(missing_ok=True)
            removed.append(str(target_path))

    for dist_info in artifact_root.glob("nvidia*dist-info"):
        shutil.rmtree(dist_info, ignore_errors=True)
        removed.append(str(dist_info))

    for pattern in artifact_globs:
        for matched_file in artifact_root.glob(pattern):
            if matched_file.exists():
                matched_file.unlink(missing_ok=True)
                removed.append(str(matched_file))

if removed:
    print("Removed NVIDIA artifacts:")
    for item in removed:
        print(f"- {item}")
else:
    print("No NVIDIA artifacts found.")
