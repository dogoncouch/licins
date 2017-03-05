#!/usr/bin/env python

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
import sys
from shutil import copyfile
import string
import datetime
import ConfigParser
from optparse import OptionParser
from optparse import OptionGroup

import LicIns.licenses
from LicIns import __version__

class LicInsCore:

    def __init__(self):
        """Initialize license insert job"""
        self.license_modules = {}
        self.args = []
        self.prefix = ''
        self.encoding = ''
        self.cname = ''
        self.signature = ''
        self.comment = ''
        self.commentend = ''
        self.options = None
        self.option_parser = OptionParser(
                usage = ("Usage: %prog [options] filename"),
                version = "%prog" + '-' + str(__version__),
                epilog="Always put multi-word option arguments in single quotes! Use ~/.config/licins.conf for persistent options.")

    def config_options(self):
        """Set config options"""
        myconf = os.getenv("HOME") + '/.config/licins.conf'
        if not os.path.isfile(myconf):
            confdir = os.getenv("HOME") + '/.config'
            if not os.path.exists(confdir): os.mkdir(confdir)
            if os.path.isfile('/usr/share/licins/licins.conf'):
                copyfile('/usr/share/licins/licins.conf', myconf)
            else:
                copyfile('licins.conf', myconf)
        config = ConfigParser.ConfigParser()
        config.read(myconf)
        self.option_parser.add_option("--list",
                action="callback",
                callback=self.list_licenses,
                help="return a list of available licenses")
        self.option_parser.add_option("-l",
                action="store",
                dest="license", default=config.get("licins", "license"),
                help="set which license to use")
        self.option_parser.add_option("-t",
                action="store",
                dest="lictype", default=config.get("licins", "lictype"),
                help="set license type")
        self.option_parser.add_option("-c",
                action="store",
                dest="comment", default=config.get("licins", "comment"),
                help="set the comment string")
        self.option_parser.add_option("-C",
                action="store",
                dest="commentend", default=config.get("licins", "commentend"),
                help="set the comment end string")
        self.option_parser.add_option("-d",
                action="store",
                dest="progdesc", default=config.get("licins", "progdesc"),
                help="set a program description line")
        self.option_parser.add_option("-n",
                action="store",
                dest="cname", default=config.get("licins", "cname"),
                help="set the copyright name")
        self.option_parser.add_option("-p",
                action="store",
                dest="prefix", default=config.get("licins", "prefix"),
                help="set the first line (e.g. '#!/bin/bash)'")
        self.option_parser.add_option("-e",
                action="store",
                dest="encoding", default=config.get("licins", "encoding"),
                help="add an encoding line")
        self.option_parser.add_option("-s",
                action="store",
                dest="signature", default=config.get("licins", "signature"),
                help="add a signature line to follow the (c) name")
        
        self.options, self.args = self.option_parser.parse_args(sys.argv[1:])

    # License modules:
    def list_licenses(self, *args):
        """Return a list of available license modules"""
        print '==== Available license modules: ===='
        print
        for lic in sorted(self.license_modules):
            print string.ljust(self.license_modules[lic].name, 10) + \
                    ': ' + self.license_modules[lic].desc
        sys.exit(0)
    
    def load_licenses(self):
        """Load license module(s)"""
        for lic in sorted(LicIns.licenses.__all__):
            self.license_modules[lic] = \
                    __import__('LicIns.licenses.' + lic, globals(), \
                    locals(), [LicIns]).LicenseModule()

    # The main event:
    def insert(self):
        """Prep the header and add it to files"""
        self.load_licenses()
        self.config_options()
        ourlictype = self.options.lictype
        ourcomment = self.options.comment
        ourcommentend = self.options.commentend
        ourprefix = self.options.prefix
        ourencoding = self.options.encoding
        ourcname = self.options.cname
        oursignature = self.options.signature
        ouryear = str(datetime.datetime.now().year)
        for job in self.args:
            thisjob = self.license_modules[self.options.license]
            thisjob.prep(lictype = ourlictype, comment = ourcomment,
                    commentend = ourcommentend, progdesc = None,
                    prefix = ourprefix, encoding = ourencoding,
                    cname = ourcname, cyear = ouryear,
                    signature = oursignature)
            thisjob.write_final(job)

def main():
    surgery = LicInsCore()
    surgery.insert()

if __name__ == "__main__":
    surgery = LicInsCore()
    surgery.insert()
