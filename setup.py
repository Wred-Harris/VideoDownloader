from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'gui'

executables = [
    Executable('main.py', base=base)
]

setup(name='Vidi',
      version = '1',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
