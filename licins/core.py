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
import string
from optparse import OptionParser
from optparse import OptionGroup

class LogDissectCore:

    def __init__(self):
        """Initialize logdissect job"""
        self.input_file = ''
        self.instype_modules = {}
        self.prefix = ''
        self.encoding = ''
        self.cname = ''
        self.signature = ''
        self.options = None
        self.option_parser = OptionParser(
                usage = ("Usage: %prog [options]"),
                version = "%prog" + str(__version__))
        self.instype_options = OptionGroup(self.option_parser, \
                _("Insert type options"))
        self.prefix_options = OptionGroup(self.option_parser, \
                _("Prefix options"))
        self.encoding_options = OptionGroup(self.option_parser, \
                _("Encoding options"))
        self.cname_options = OptionGroup(self.option_parser, \
                _("Copyright name options"))
        self.sig_options = OptionGroup(self.option_parser, \
                _("Signature options"))
    
    def insert(self, instype = 'header', prefix = '', encoding = '', \
            cname = '', signature = ''):
        """Insert the header"""
        pass

    def do_output(self, options):
        """Output to file"""
        pass

    def config_options(self):
        """Set config options"""
        self.option_parser.add_option("--list-types",
                action="callback",
                callback=self.list_instypes,
                help=_("returns a list of available insert types"))
        self.option_parser.add_option("-t", "--type",
                action="store",
                dest="instype_list", default="header",
                help=_("sets the insert type"))
        self.option_parser.add_option("-l", "--license",
                action="store",
                dest="license_list", default="mit",
                help=_("specifies which license to use"))
        self.option_parser.add_option("-p", "--prefix",
                action="store",
                dest="prefix",
                help=_("sets the first line (e.g. #!/bin/bash)"))
        self.option_parser.add_option("-e", "--encoding",
                action="store",
                dest="encoding",
                help=_("sets an encoding line"))
        self.option_parser.add_option("-c", "--cname",
                action="store",
                dest="cname",
                help=_("sets the copyright name"))
        self.option_parser.add_option("-s", "--signature",
                action="store",
                dest="signature",
                help=_("sets a signature to follow the (C) name"))
        
        self.option_parser.add_option_group(self.instype_options)
        self.option_parser.add_option_group(self.prefix_options)
        self.option_parser.add_option_group(self.cname_options)
        self.option_parser.add_option_group(self.signature_options)
        self.option_parser.add_option_group(self.signature_options)
        self.options, args = self.option_parser.parse_args(sys.argv[1:])

    # Load input files:
    def load_inputs(self, options):
        """Load the specified inputs"""
        for f in self.input_options:
            fullpath = os.path.abspath(f)
            log = LogData(source_full_path=fullpath)
            self.data_set.append(log)

    # Parsing modules:
    def list_instypes(self):
        """Return a list of available insert types"""
        print '==== Available insert types: ===='
        print
        for ins in sorted(self.instype_modules):
            print string.ljust(self.instype_modules[ins].name, 16) + \
                ': ' + self.instype_modules[ins].desc
        sys.exit(0)
    
    def load_instypes(self, instype_modules):
        """Load insert type module(s)"""
        for ins in sorted(licins.modules.__instypes__):
            self.instype_modules[ins] = \
                __import__('licins.modules.' + ins, globals(), \
                locals(), [licins]).InsTypeModule(self.instype_options)

if __name__ == "__main__":
    surgery = LicInsCore()
    surgery.insert()
