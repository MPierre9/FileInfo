# import sys
import os

# first_arg = sys.argv[1]

## The following function returns the size of a file, in bytes
## To use, call the function as follows print getFileSize("path/to/file")
def getFileSize(path):

    fileSize = os.path.getsize(path)
    return fileSize

# getFileSize(first_arg)