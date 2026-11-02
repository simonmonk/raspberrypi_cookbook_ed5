#!/usr/bin/python

from getopt import getopt
from sys import argv

args = argv[1:]
dps = 2

number = float(args[-1])
arguments, values = getopt(args, 'd:')
for currentArg, currentVal in arguments:
    #print(f"currentArg:{currentArg} currentVal:{currentVal}")
    if currentArg == '-d':
        dps = int(currentVal)

print(f"dps={dps} {number:.{dps}f}")

