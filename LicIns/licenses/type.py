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

import os

class LicenseModule:
    def __init__(self):
        """Initialize a license object"""
        self.name = ''
        self.desc = ''
        # Short header version:
        self.header = ''
        # Full version:
        self.full = ''
        # What comes before your name on copyright line:
        self.copyrightpre = ''
        self.finalproduct = []
        pass

    def prep(self, lictype = 'header', comment = '# ', commentend = '',
            cname = '', cyear = 2017, progdesc = None, prefix = None,
            encoding = None, signature = None):
        """Prepare the license with comments, etc."""
        if lictype == 'full': initwork = self.full.split('\n')
        else: initwork = self.header.split('\n')
        # Handle copyright name and optional signature line in headers:
        work = []
        for line in initwork:
            if line.startswith(self.copyrightpre):
                if cname and not lictype == 'full':
                    work.append(line + cyear + ' ' + cname)
                else: work.append(line)
                if signature: work.append(signature)
            else:
                work.append(line)
        # Add all of the pre-copyright lines in reverse order:
        if progdesc: work.insert(0, progdesc)
        if encoding: work.insert(0, encoding)
        # Prepare the final product with comments:
        if commentend:
            self.finalproduct = [comment + line + commentend + \
                    '\n' for line in work]
        else:
            self.finalproduct = [comment + line + '\n' for line in work]
        if prefix: self.finalproduct.insert(0, prefix + '\n\n')
        return 0

    def write_final(self, inputfile):
        """Insert the formatted license into a file"""
        if not os.path.isfile(inputfile):
            touchit = open(inputfile, 'w')
            touchit.write('\n')
            touchit.close()
        lines = open(inputfile, 'r').readlines()
        # Ignore the first line if it starts with #!:
        startline = 0
        if not lines: lines.append('\n')
        if lines[0]: 
            if lines[0].startswith('#!'): startline = 1
        # Insert our header:
        lines[startline:startline] = self.finalproduct
        # Convert output from list to string:
        final = ''.join(lines)
        # Write to the file:
        with open(inputfile, 'w') as output:
            output.write(final)
        return 0
