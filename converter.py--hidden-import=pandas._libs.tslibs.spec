# -*- mode: python -*-

block_cipher = None


a = Analysis(['converter.py--hidden-import=pandas._libs.tslibs.timedeltas'],
             pathex=['C:\\Users\\eguot\\Desktop\\data_converter_7-18'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='converter.py--hidden-import=pandas._libs.tslibs',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
