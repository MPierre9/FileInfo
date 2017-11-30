# FileInfo
![Travis Build](https://travis-ci.org/MPierre9/FileInfo.svg?branch=master)
## Summary
File Info is a Python library which contains various useful file functions. Currently there are four functions included in the FileInfo library: 

1. getFileSize
1. getFilename
1. getMd5Digest
1. getSha1Digest


## Installation 

1. Install/Start your preferred Python IDE (FileInfo was developed in [Visual Studio 2015](https://www.visualstudio.com/downloads/))

1. Clone the FileInfo repository `git clone https://github.com/MPierre9/FileInfo.git`

1. Import FileInfo functions in your project: 
   * `from getFilename import getFilename`
   * `from getFileSize import getFileSize`
   * `from getMd5Digest import getMd5Digest`
   * `from getSha1Digest import getSha1Digest` 
   
1. Your good to go! Feel free to use FileInfo's functions in your code!




## Usage 

##### getFileSize

Summary: This function returns the size of a file, in bytes
To use, call the function as follows `print getFileSize("path/to/file")`
