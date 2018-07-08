## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
import catkin_pkg.python_setup

# fetch values from package.xml
setup_args = catkin_pkg.python_setup.generate_distutils_setup(
    packages=['sensor'],
    package_dir={'': 'src'})

setup(**setup_args)
