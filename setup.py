# Processing for Pygments is a Pygments lexer and style for Processing.  
# Copyright (C) 2015  Sigmund Hansen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name='pygments-processing',
    description='Pygments lexer and style for Processing\'s Java.',
    version='0.1',
    long_description=open('README.md').read(),
    keywords='pygments processing java pde',
    packages=find_packages(),
    install_requires=['pygments >= 1.4'],
    entry_points={'pygments.lexers':
                    'processing=pygments_processing:ProcessingLexer',
                  'pygments.styles':
                    'processing=pygments_processing:ProcessingStyle',
              },
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Plugins',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
