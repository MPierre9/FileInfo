import ntpath
## The following function returns the filename when given a path 
## To use simply pass your desired path as a string into the function getFilename
def getFilename(path):
    path, fileName = ntpath.split(path)
    return fileName
