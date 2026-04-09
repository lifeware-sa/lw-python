# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller import compat


Path('build/main').mkdir(parents=True, exist_ok=True)
Path('dist').mkdir(parents=True, exist_ok=True)


hiddenimports = [
    'textractor.cli',
    'textractor.cli.cli',
]

datas = []

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
