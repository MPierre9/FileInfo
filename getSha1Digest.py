import hashlib
## The following function returns the sha1 digest from a file containing text
## To use, call the function as follows print getSha1Digest("path/to/file")

def getSha1Digest(path):
    f = open(path)
    path = f.read()
    m = hashlib.sha1(path)

    return m.hexdigest()