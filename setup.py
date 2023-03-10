
from setuptools import setup, find_packages
from pathlib import Path
import ast

VERSION = ast.literal_eval((Path(__file__).parent / 'src' / 'betterdicts' / 'VERSION.py').open('r').read().split('=')[1].strip())

setup(
  name='betterdicts',
  description='Better dictionary types for Python.',
  version=VERSION,
  long_description_content_type='text/markdown',
  long_description=open('README.md', 'r').read(),
  author='Frank S. Hestvik',
  author_email='tristesse@gmail.com',

  install_requires=[],

  url='https://gitlab.com/franksh/betterdicts',
  license='Apache-2.0',
  keywords=["dict", "prelude", "utility", "convenience"],
  classifiers=[
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: Apache Software License",
    "Topic :: Utilities",
  ],
  packages=find_packages('src'),
  package_dir={'': 'src'},
  python_requires='>=3.8',
  # zip_safe=False,
  # package_data={
  #   'betterdicts': ['VERSION'],
  # },
  # include_package_data=True,
)
