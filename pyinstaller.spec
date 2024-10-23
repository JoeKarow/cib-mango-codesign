# pyinstaller.spec

import os
from PyInstaller.utils.hooks import copy_metadata

block_cipher = None

platform = os.name

a = Analysis(
    ['mangotango.py'],  # Entry point
    pathex=['.'],
    binaries=[],
    datas=[
        *(
            [('./VERSION', '.')]
            if os.path.exists('VERSION') else []
        ),
        *copy_metadata('readchar'),
        ('./components/web_static', 'components/web_static'),
        ('./components/web_templates', 'components/web_templates')
    ],
    hiddenimports=[
        'readchar',
        'numpy',
        'numpy.core.multiarray'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[]
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)


# Create the executable for Windows
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='mangotango.exe',
    debug=False,
    strip=True,
    upx=True,
    console=True  # Change to False if you don't want a console window
)
# Create the macOS application bundle
app = BUNDLE(
    exe,
    name='mangotango.app',
    debug=False,
    icon='mango.icns',
    strip=True,
    upx=True,
)
