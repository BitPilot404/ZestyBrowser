import sys
from cx_Freeze import setup, Executable

# Replace 'Browser.py' with your actual file name
filename = 'Browser.py'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'  # Use this for GUI applications, omit for console

executables = [Executable(filename, base=base)]

# Include any additional dependencies if needed (e.g., 'packages': ['module'])
options = {
    'build_exe': {
        'includes': [],
        'include_files': [],  # Add any additional files or resources here
    }
}

setup(
    name='ZestyBaba Browser',  # Replace with your app name
    version='1.0',
    description='Description of your application',
    options=options,
    executables=executables
)
