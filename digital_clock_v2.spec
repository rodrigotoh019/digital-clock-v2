# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['digital_clock_v2.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')],  # Include your fonts folder!
    hiddenimports=['pyglet', 'pytz'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pth = Tree('assets', prefix='assets')  # Include assets folder

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    pth,
    [],
    name='Baby-lou Clock',  # Your .exe name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for users!
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    coerce_macros=True,
    entitlements_file=None,
    icon=None
)