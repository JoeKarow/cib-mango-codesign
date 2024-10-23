# pyinstaller.spec

import os
from PyInstaller.utils.hooks import copy_metadata

block_cipher = None

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

# Create the macOS application bundle
app = BUNDLE(
    exe,
    name='mangotango',
    debug=False,
    icon='mango.icns',
    strip=True,
    upx=True,
)
