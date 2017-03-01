# licins
Command line tool to insert software licenses into source code.

# SYNOPSIS
licins [-t LICTYPE] [-c COMMENT] [-C COMMENTEND] [-d PROGDESC] [-n CNAME] [-l LICENSE] [-p PREFIX] [-e ENCODING] [-s SIGNATURE] files

# DESCRIPTION
licins is a tool for inserting commented software licenses into source code. Comes with modules for popular open source licenses, and uses a config file for persistent options. Stop copying and pasting.

# OPTIONS

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

Always put multi-word option arguments in quotes!

# EXAMPLES
    licins -l mit -n 'Dan Persons' -p '#!/usr/bin/env python' *.py
    licins -l gpl2 -n 'John Exampleton' -c '/*' -C '*/' example.c

# AUTHOR
    Dan Persons (dpersonsdev@gmail.com)

# COPYRIGHT
MIT License

Copyright (c) 2017 Dan Persons

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

