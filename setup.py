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
"""
Licins
------

Licins is a tool for inserting commented software licenses into source code. It comes with modules for popular open source licenses, and can use config files for persistent options. Licenses are inserted at the beginnigs of files, but after any lines starting with #!. Options for copyright name, encoding, signature, and other add-ons.

Options
```````

::
    
    --version     show program's version number and exit
    -h, --help    show this help message and exit
    --list        return a list of available licenses
    -l LICENSE    set which license to use
    -t LICTYPE    set license type (header|full, default=header)
    -c COMMENT    set the comment string (default='# ')
    -c COMMENTEND set the comment end string
    -d PROGDESC   set a program description line
    -n CNAME      set the copyright name
    -p PREFIX     set the first line (e.g. #!/bin/bash)
    -e ENCODING   add an encoding line
    -s SIGNATURE  add a signature line to follow the (c) name

Always put multi-word option arguments in single quotes!

::

    ==== Available license modules: ====
    
    apache    : The Apache 2.0 license
    bsd2      : The Berkeley Software Distribution license v2
    bsd3      : The Berkeley Software Distribution license v3
    gfdl1-2   : The GNU Free Documentation License v1.2
    gfdl1-3   : The GNU Free Documentation License v1.3
    gpl2      : The GNU General Public License v2+
    gpl3      : The Gnu General Public License v3
    lgpl2     : The GNU Library General Public License v2+
    lgpl2-1   : The GNU Library General Public License v2.1+
    lgpl3     : The GNU Library General Public License v3
    mit       : The MIT License

Links
`````

* `Releases <https://github.com/dogoncouch/licins/releases/>`_
* `README <https://github.com/dogoncouch/licins/blob/master/README.md>`_
* `Development source <https://github.com/dogoncouch/licins/>`_

"""

from setuptools import setup
from os.path import join
from sys import prefix
from LicIns import __version__

ourdata = [(join(prefix, 'share/man/man1'), ['doc/licins.1']),
        (join(prefix, 'share/doc/licins'), ['README.md', 'LICENSE',
            'CHANGELOG']),
        (join(prefix, 'share/doc/licins/licenses'), ['doc/licenses/LGPL-3',
            'doc/licenses/LGPL-2', 'doc/licenses/LGPL-2.1',
            'doc/licenses/GPL-3', 'doc/licenses/Apache-2.0',
            'doc/licenses/BSD-2', 'doc/licenses/GFDL-1.3',
            'doc/licenses/GFDL-1.2', 'doc/licenses/MIT',
            'doc/licenses/BSD-3', 'doc/licenses/GPL-2']),
        (join(prefix, 'share/licins/config'), ['licins.conf'])]

setup(name='licins', version = str(__version__),
        description = 'Insert commented licenses into source files',
        long_description = __doc__,
        author = 'Dan Persons', author_email = 'dpersonsdev@gmail.com',
        url = 'https://github.com/dogoncouch/licins',
        download_url = 'https://github.com/dogoncouch/licins/' + \
                'archive/v' + str(__version__) + '.tar.gz',
        packages = [ 'LicIns', 'LicIns.licenses' ],
        entry_points = { 'console_scripts': [ 'licins = LicIns.core:main' ] },
        data_files = ourdata,
        keywords = ['development', 'developer-tools', 'cli', 'license',
            'license-management', 'licenses', 'open-source',
            'open-source-licensing', 'copyright', 'software-license'],
        classifiers = ["Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 2",
            "Topic :: Software Development"])
