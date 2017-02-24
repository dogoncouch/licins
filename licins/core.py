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

class LicInsCore:

    def __init__(self):
        """Initialize license insert job"""
        self.input_files = []
        self.instype_modules = ''
        self.prefix = ''
        self.encoding = ''
        self.cname = ''
        self.signature = ''
        self.options = None
        self.option_parser = OptionParser(
                usage = ("Usage: %prog [options]"),
                version = "%prog" + str(__version__))
        self.file_options = OptionGroup(self.option_parser, \
                _("File options"))
        self.instype_options = OptionGroup(self.option_parser, \
                _("Insert type options"))
        self.comment_options = OptionGroup(self.option_parser, \
                _("Comment options"))
        self.cname_options = OptionGroup(self.option_parser, \
                _("Copyright name"))
        self.license_options = OptionGroup(self.option_parser, \
                _("License options"))
        self.prefix_options = OptionGroup(self.option_parser, \
                _("Prefix options"))
        self.encoding_options = OptionGroup(self.option_parser, \
                _("Encoding options"))
        self.cname_options = OptionGroup(self.option_parser, \
                _("Copyright name options"))
        self.sig_options = OptionGroup(self.option_parser, \
                _("Signature options"))
    
#     # Load file:
#     def load_input(self, options):
#         """Load the specified inputs"""
#         # Initialize the license

#         for f in self.input_options:
#             fullpath = os.path.abspath(f)
#             ourmodule = 'licins.licenses.' + self.license_options[0]
            

    def insert(self):
        """Output the prepared header to files"""
        self.load_input()
        self.load_licenses()
        self.load_instypes()
        ourmodule = 'licins.licenses.' + self.license_options[0]
        job = ourmodule.LicenseModule()
        prefix = ' '.join(prefix)
        encoding = ' '.join(encoding)
        cname = ' '.join(cname)
        signature = ' '.join(signature)
        job.prep(instype = instype_options[0], \
                comments = ' '.join(comment_options), \
                cyear = '2017', progdesc = None, \
                prefix = ' '.join(prefix_options), \
                encoding = ' '.join(encoding_options), \
                signature = ' '.join(signature_options))
        for dest in self.file_options:
            job.write(dest)

    def config_options(self):
        """Set config options"""
        self.option_parser.add_option("--list-types",
                action="callback",
                callback=self.list_instypes,
                help=_("returns a list of available insert types"))
        self.option_parser.add_option("--list-licenses",
                action="callback",
                callback=self.list_licenses,
                help=_("returns a list of available licenses"))
        self.option_parser.add_option("-f", "--file",
                action="store",
                dest="file_list",
                help=_("specifies target files"))
        self.option_parser.add_option("-t", "--type",
                action="store",
                dest="instype_list", default="header",
                help=_("sets the insert type"))
        self.option_parser.add_option("-c", "--comment",
                action="store",
                dest="comment_list", default="# ",
                help=_("sets the comment type"))
        self.option_parser.add_option("-n", "--name",
                action="store",
                dest="cname", default="# ",
                help=_("sets the copyright name"))
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
                help=_("sets a signature to follow the (c) name"))
        
        self.option_parser.add_option_group(self.file_options)
        self.option_parser.add_option_group(self.instype_options)
        self.option_parser.add_option_group(self.comment_options)
        self.option_parser.add_option_group(self.cname_options)
        self.option_parser.add_option_group(self.license_options)
        self.option_parser.add_option_group(self.prefix_options)
        self.option_parser.add_option_group(self.encoding_options)
        self.option_parser.add_option_group(self.cname_options)
        self.option_parser.add_option_group(self.signature_options)
        self.options, args = self.option_parser.parse_args(sys.argv[1:])

    # Insert type modules:
    def list_instypes(self):
        """Return a list of available insert types"""
        print '==== Available insert types: ===='
        print
        print string.ljust('header', 16) + \
                ': Adds a short license header (default')
        print string.ljust('full', 16) + \
                ': Adds a full license (not recommended for code')

    def load_instypes(self, instype_modules):
        """Sets the insert type (header or full)"""
        self.instype_modules = instype_options

#         for ins in sorted(self.instype_modules):
#             print string.ljust(self.instype_modules[ins].name, 16) + \
#                 ': ' + self.instype_modules[ins].desc
#         sys.exit(0)
    
#     def load_instypes(self, instype_modules):
#         """Load insert type module(s)"""
#         for ins in sorted(licins.modules.__instypes__):
#             self.instype_modules[ins] = \
#                 __import__('licins.modules.' + ins, globals(), \
#                 locals(), [licins]).InsTypeModule(self.instype_options)

    # License modules:
    def list_licenses(self):
        """Return a list of available insert types"""
        print '==== Available license modules: ===='
        print
        for lic in sorted(self.license_modules):
            print string.ljust(self.license_modules[lic].name, 16) + \
                    ': ' + self.license_modules[lic].desc
        sys.exit(0)
    
    def load_licenses(self, license_modules):
        """Load license module(s)"""
#         for lic in sorted(licins.licenses.__all__):
#             self.license_modules[lic] = \
#                     __import__('licins.licenses.' + lic, globals(), \
#                     locals(), [licins]).LicenseModule(self.license_options)

        self.license_module = __import__('licins.licenses.' + \
                self.license_options[0])

if __name__ == "__main__":
    surgery = LicInsCore()
    surgery.insert()
