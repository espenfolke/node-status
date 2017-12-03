#!/usr/bin/python

import functions as fn
from sys import argv

NO_INPUT_FILE = 'Input file was not included in the command \n python app.py <inputfile> '
WRONG_ARGS = 'Only one argument is required \n python app.py <inputfile> '
LOST = "LOST"
FOUND = "FOUND"
HELLO = "HELLO"

if (len(argv) < 2):
    raise Exception(NO_INPUT_FILE)
if (len(argv) > 2):
    raise Exception(WRONG_ARGS)
data = fn.read_file(argv[1])
# fn.debug_show_nodes(data)

for key in data:
    data[key].get_status()
