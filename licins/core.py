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
from sys import exit
from shutil import copyfile
from datetime import datetime
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
from argparse import ArgumentParser

import licins.licenses
from licins import __version__

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
        self.args = None
        self.arg_parser = ArgumentParser(
                epilog="Always put multi-word option arguments in single quotes!\nUse ~/.config/licins.conf for persistent options.")

    def get_options(self):
        """Set config options"""
        myconf = os.getenv("HOME") + '/.config/licins.conf'
        if not os.path.isfile(myconf):
            confdir = os.getenv("HOME") + '/.config'
            if not os.path.exists(confdir): os.mkdir(confdir)
            if os.path.isfile('/usr/share/licins/config/licins.conf'):
                copyfile('/usr/share/licins/config/licins.conf', myconf)
            else:
                try:
                    copyfile('licins.conf', myconf)
                except IOError:
                    print('Error: ~/.config/licins.conf cannot be found.')
                    exit(0)
        config = ConfigParser()
        config.read(myconf)
        self.arg_parser.add_argument("--version", action="version",
                version="%(prog)s " + str(__version__))
        self.arg_parser.add_argument("--list",
                action="store_true", dest='list_licenses',
                help="return a list of available licenses")
        self.arg_parser.add_argument("-l",
                action="store",
                dest="license", default=config.get("licins", "license"),
                help="set which license to use")
        self.arg_parser.add_argument("-t",
                action="store",
                dest="lictype", default=config.get("licins", "lictype"),
                help="set license type")
        self.arg_parser.add_argument("-c",
                action="store",
                dest="comment", default=config.get("licins", "comment"),
                help="set the comment string")
        self.arg_parser.add_argument("-C",
                action="store",
                dest="commentend", default=config.get(
                    "licins", "commentend"),
                help="set the comment end string")
        self.arg_parser.add_argument("-d",
                action="store",
                dest="progdesc", default=config.get("licins", "progdesc"),
                help="set a program description line")
        self.arg_parser.add_argument("-n",
                action="store",
                dest="cname", default=config.get("licins", "cname"),
                help="set the copyright name")
        self.arg_parser.add_argument("-y",
                action="store",
                dest="cyear", default=False,
                help="set the copyright year (default: current year)")
        self.arg_parser.add_argument("-p",
                action="store",
                dest="prefix", default=config.get("licins", "prefix"),
                help="set the first line (e.g. '#!/bin/bash)'")
        self.arg_parser.add_argument("-e",
                action="store",
                dest="encoding", default=config.get("licins", "encoding"),
                help="add an encoding line")
        self.arg_parser.add_argument("-s",
                action="store",
                dest="signature", default=config.get("licins", "signature"),
                help="add a signature line to follow the (c) name")
        self.arg_parser.add_argument("files",
                metavar="FILE", nargs="*",
                help="specify files in which to insert licenses")
        
        self.args = self.arg_parser.parse_args()

    # License modules:
    def list_licenses(self, *args):
        """Return a list of available license modules"""
        print('==== Available license modules: ====\n')
        for lic in sorted(self.license_modules):
            print(self.license_modules[lic].name.ljust(10) + \
                    ': ' + self.license_modules[lic].desc)
        exit(0)
    
    def load_licenses(self):
        """Load license module(s)"""
        for lic in sorted(licins.licenses.__all__):
            self.license_modules[lic] = \
                    __import__('licins.licenses.' + lic, globals(), \
                    locals(), [licins]).LicenseModule()

    # The main event:
    def insert(self):
        """Prep the header and add it to files"""
        self.load_licenses()
        self.get_options()
        if self.args.list_licenses:
            self.list_licenses()
            exit(0)
        if self.args.cyear:
            ouryear = self.args.cyear
        else:
            ouryear = str(datetime.now().year)
        for job in self.args.files:
            thisjob = self.license_modules[self.args.license]
            thisjob.prep(lictype = self.args.lictype,
                    comment = self.args.comment,
                    commentend = self.args.commentend,
                    progdesc = self.args.progdesc,
                    prefix = self.args.prefix,
                    encoding = self.args.encoding,
                    cname = self.args.cname,
                    cyear = ouryear,
                    signature = self.args.signature)
            thisjob.write_final(job)

def main():
    surgery = LicInsCore()
    surgery.insert()

if __name__ == "__main__":
    surgery = LicInsCore()
    surgery.insert()
