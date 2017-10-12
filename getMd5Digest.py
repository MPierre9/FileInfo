import hashlib
## The following function returns the MD5 digest from a file containing text
## To use, call the function as follows print getMd5Digest("path/to/file")
def getMd5Digest(path):
    f = open(path)
    path = f.read()
    m = hashlib.md5(path)

    return m.hexdigest()
