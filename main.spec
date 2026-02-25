# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller import compat
from PyInstaller.utils.hooks import collect_data_files, copy_metadata


Path('build/main').mkdir(parents=True, exist_ok=True)
Path('dist').mkdir(parents=True, exist_ok=True)


hiddenimports = [
    'docling.backend.docling_parse_v2_backend',
    'docling.backend.docling_parse_v4_backend',
    'docling.backend.pypdfium2_backend',
    'docling.models.plugins',
    'docling.models.plugins.defaults',
    'markitdown.__main__',
    'textractor.cli',
    'textractor.cli.cli',
]

datas = (
    collect_data_files('docling')
    + collect_data_files('docling_parse')
    + collect_data_files('magika')
    + collect_data_files('rapidocr')
    + collect_data_files('pypdfium2_raw')
    + copy_metadata('docling')
    + copy_metadata('docling-core')
    + copy_metadata('docling-ibm-models')
    + copy_metadata('docling-parse')
    + copy_metadata('markitdown')
    + copy_metadata('rapidocr')
    + copy_metadata('pypdfium2')
)

excludes = [
    'pytest',
    '_pytest',
    'tensorflow',
    'tensorboard',
    'torch.utils.tensorboard',
    'torchaudio',
    'speech_recognition',
]

use_strip = not compat.is_win
use_upx = not compat.is_win

a = Analysis(
    ['src/lwPython/main.py'],
    pathex=['src'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=use_strip,
    upx=use_upx,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=use_strip,
    upx=use_upx,
    upx_exclude=[],
    name='main',
)
