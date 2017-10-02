'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
from setuptools import setup
from setuptools import find_packages
PACKAGE_NAME = 'specguiutils'
setup(name=PACKAGE_NAME,


      version='0.1',
      description='Library to provide PyQt4 widgets to display spec file information read using ' +
                   'spec2nexus.spec file library',
      author = 'John Hammonds',
      author_email = 'JPHammonds@anl.gov',
      url = '',
      packages = find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      install_requires = ['spec2nexus', ],
      license = 'See LICENSE File',
      platforms = 'any',
      install_requires = ['pyqt5 >= 5.6',
                          'spec2nexus >= 2017.901.4']
)