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

    def prep(self, instype = 'header', comment = '## ', cname = '', \
            cyear = '', progdesc = None, prefix = None, \
            encoding = None, signature = None):
        """Prepare the license with comments, etc."""
        # To Do: replace default year with current year from os.
        # To Do: get rid of this next cheat line:
        #instype = 'header'
        # if 'header' in instype: work = self.header.split('\n')
        #if instype == 'header': work = self.header.split('\n')
        if instype == 'full': initwork = self.full.split('\n')
        else: initwork = self.header.split('\n')
        # Handle copyright name and optional signature line:
        work = []
        for line in initwork:
            if line.startswith(self.copyrightpre):
                # To Do: Fix next line, it's the problem.
                work.append(line + cyear + ' ' + cname)
                if signature:
                    work.append(signature)
            else:
                work.append(line)
        # Add all of the pre-copyright lines in reverse order:
        if progdesc: work.insert(0, progdesc)
        if encoding: work.insert(0, encoding)
        if prefix: work.insert(0, prefix)
        # Add the comments
        # To Do: make this work.
        # ['# ' + s + '\n' for s in work]
        # for line in work:
        #     line = '# ' + line + '\n'
        # Prepare the final product:
        # To Do: fix problem: work is not made up of strings.
        # It's probably an option parsing problem, wrong thing
        # is being sent to this function for various variables.
        # work = " ".join(work)
        self.finalproduct = [comment + line + '\n' for line in work]
        return 0

    def write_final(self, inputfile):
        """Insert the formatted license into a file"""
        # lines = []
        lines = open(inputfile, 'r').readlines()
        # Ignore the first line if it starts with #!:
        # To Do: add this back later!
        startline = 0
        if lines[0]: 
            if lines[0].startswith('#!'): startline = 1
        # startline = 0
        # Read the file and add our prepared license:
        # final_list = []
        # self.finalproduct = '\n'.join(self.finalproduct)
        lines[startline:startline] = self.finalproduct
        # final_list = lines.insert(startline, self.finalproduct)
        # final_list = lines.insert(startline, self.final_list)
        final = ''.join(lines)
        # Write the final result:
        output = open(inputfile, 'w')
        output.write(final)
        output.close()
        return 0
