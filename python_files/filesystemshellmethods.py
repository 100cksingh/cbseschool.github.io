# problem in program and program is half complete from the video lecture

# example file for working with filesystem shell methods

import os
from os import path
import shutil

def main():
    if path.exists("textfile.txt"):
        src=path.realpath("textfile.txt")
    dst=src+".bak"
    shutil.copy(src,dst)
    shutil.copystat(src,dst)

