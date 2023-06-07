#1: os.remove(file)
import os, atexit

atexit.register(lambda file = __file__: os.remove(file))

#2: argv[0]
from os import remove
from sys import argv

remove(argv[0])