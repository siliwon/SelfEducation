#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("newfile.txt"):

        # get the path to the file in the current directory
        scr = path.realpath('textfile.txt')

        # let's make a backup copy by appending "bak" to the name
        dst = scr + ".bak"

        # # copy over the permissions, modification times, and other info
        # shutil.copy(scr, dst)
        # shutil.copystat(scr, dst)

        # rename the original file
        # os.rename('a new one.txt', 'newfile.txt')
        # print("a new one.txt")

        # now put things into a ZIP archive
        # root_dir, tail = path.split(scr)
        # shutil.make_archive("archive", "zip", root_dir)


        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", 'w') as newzip:
            newzip.write("newfile.txt")

if __name__ == "__main__":
    main()
