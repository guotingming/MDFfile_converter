# -*- mode: python -*-

block_cipher = None


a = Analysis(['converter.py'],
             pathex=['C:\\Users\\guo\\Desktop\\data_converter_7-18-21-00\\data_converter_7-18'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
def get_pandas_path():
    import pandas
    pandas_path = pandas.__path__[0]
    return pandas_path
 
dict_tree = Tree(get_pandas_path(), prefix='pandas', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'pandas' not in x[0], a.binaries)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='converter',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
