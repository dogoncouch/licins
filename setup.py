#!/usr/bin/env python

# MIT License
# 
# Copyright (c) 2017 Dan Persons
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

from setuptools import setup
from os.path import join
from sys import prefix
from LicIns import __version__

ourdata = [(join(prefix, 'share/man/man1'), ['doc/licins.1']),
        (join(prefix, 'share/doc/licins'), ['README.md', 'LICENSE']),
        (join(prefix, 'share/doc/licins/licenses'), ['doc/licenses/LGPL-3',
            'doc/licenses/LGPL-2', 'doc/licenses/LGPL-2.1',
            'doc/licenses/GPL-3', 'doc/licenses/Apache-2.0',
            'doc/licenses/BSD-2', 'doc/licenses/GFDL-1.3',
            'doc/licenses/GFDL-1.2', 'doc/licenses/MIT',
            'doc/licenses/BSD-3', 'doc/licenses/GPL-2']),
        (join(prefix, 'share/licins/config'), ['licins.conf'])]

setup(name='licins', version = str(__version__),
        description = 'Insert commented licenses into source files',
        long_description = open('README.md').read(),
        author = 'Dan Persons', author_email = 'dpersonsdev@gmail.com',
        url = 'https://github.com/dogoncouch/licins',
        packages = [ 'LicIns', 'LicIns.licenses' ],
        entry_points = { 'console_scripts': [ 'licins = LicIns.core:main' ] },
        data_files = ourdata,
        classifiers = ["Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 2",
            "Topic :: Software Development"])
