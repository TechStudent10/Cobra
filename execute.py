import os
import sys

from run import run_function

filename = sys.argv[1]

with open(filename, 'r') as f:
    data = f.read()

lines = data.split('\n')
for line in lines:
    run_function(line)