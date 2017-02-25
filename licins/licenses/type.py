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
    def __init__(self, options):
        """Initialize a license object"""
        self.name = ''
        self.desc = ''
        # Short header version:
        self.header = ''
        # Full version:
        self.full = ''
        # What comes before your name on copyright line:
        self.copyrightpre = ''
        self.finalproduct = ''
        pass

    def prep(self, instype = 'header', comment = '# ', cname = '', \
            cyear = '', progdesc = None, prefix = None, \
            encoding = None, signature = None):
        """Prepare the license with comments, etc."""
        # To Do: replace default year with current year from os.
        # To Do: get rid of this next cheat line:
        instype = 'header'
        # if 'header' in instype: work = self.header.split('\n')
        if instype == 'header': work = self.header.split('\n')
        if instype == 'full': work = self.full.split('\n')
        # Handle copyright name and optional signature line:
        nextline = 1
        for line in work:
            if line.startswith(self.copyrightpre):
                line = str(line + cyear + ' ' + cname)
                if signature:
                    work.insert(nextline, signature)
            nextline = nextline + 1
        # Add all of the pre-copyright lines in reverse order:
        if progdesc: work.insert(0, progdesc)
        if encoding: work.insert(0, encoding)
        if prefix: work.insert(0, prefix)
        # Add the comments
        for line in work:
            line = str(str(comment) + str(line))
        # Prepare the final product:
        # To Do: fix problem: work is not made up of strings.
        # It's probably an option parsing problem, wrong thing
        # is being sent to this function for various variables.
        work = " ".join(work)
        self.finalproduct = work

    def write(self, inputfile):
        """Insert the formatted license into a file"""
        lines = open(inputfile, 'r').readlines()
        # Ignore the first line if it starts with #!:
        if lines[0].startswith('#!'): startline = 1
        else: startline = 0
        # Read the file and add our prepared license:
        final = lines.insert(startline, self.finalproduct)
        # Write the final result:
        output = open(inputfile, 'w')
        output.write(final)
        output.close()
