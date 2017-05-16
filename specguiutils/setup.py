'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
from setuptools import setup

setup(name='specguiutils',
      version='0.0.1',
      description='Library to provide PyQt4 widgets to display spec file information read using ' +
                   'spec2nexus.spec file library',
      author = 'John Hammonds',
      author_email = 'JPHammonds@anl.gov',
      url = '',
      packages = ['specguiutils',
                  'specguiutils.scanbrowser',
                  'specguiutils.counterselector',
                  'specguiutils.examples',
                  'specguiutils.examples.scanbrowserexample'] ,
      install_requires = ['spec2nexus', ],
      license = 'See LICENSE File',
      platforms = 'any',
#       scripts = ['Scripts/rsMap3D',
#                  'Scripts/rsMap3D.bat'],
)