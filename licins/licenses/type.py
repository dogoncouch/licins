# MIT License
# 
# Copyright (c) 2017 Dan Persons <dpersonsdev@gmail.com>
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

# import os

class LicenseData:
    def __init__(self, options):
        import os
        """Initialize a license object"""
        self.name = ""
        self.desc = ""
        self.header = ""
        self.full = ""
        pass

    def prep(self, instype = 'header', prefix = '', encoding = '', \
            signature = ''):
        """Prepare the license with comments, etc."""
        pass

    def write(self, inputfile, printlicense):
        """Insert the formatted license into a file"""
        lines = os.popen(inputfile).readlines()
        if lines[0].startswith('#!'): startline = 1
        else: startline = 0
        final = lines.insert(startline, printlicense)
        output = open(inputfile, 'w')
        output.write(final)
        output.close()