# FileInfo
![Travis Build](https://travis-ci.org/MPierre9/FileInfo.svg?branch=master)
## Summary
File Info is a Python library which contains various useful file functions. Currently there are four functions included in the FileInfo library: 

1. getFileSize
1. getFilename
1. getMd5Digest
1. getSha1Digest


## Installation 

1. Install the latest version of [Python](https://www.python.org/) 

1. Install/Start your preferred Python IDE (FileInfo was developed in [Visual Studio 2015](https://www.visualstudio.com/downloads/))

1. Clone the FileInfo repository `git clone https://github.com/MPierre9/FileInfo.git`

1. Import FileInfo functions in your project: 
   * `from getFilename import getFilename`
   * `from getFileSize import getFileSize`
   * `from getMd5Digest import getMd5Digest`
   * `from getSha1Digest import getSha1Digest` 
   
1. Your good to go! Feel free to use FileInfo's functions in your code!




## Usage 

#### getFileSize

**Summary**: This function returns the size of a file, in bytes
To use, call the function as follows: 
`print getFileSize("path/to/file")`

#### getFilename

**Summary**: The following function returns the filename when given a path
 To use simply pass your desired path as a string into the function getFilename:
 `print getFilename("path/to/file");`


 #### getMd5Digest 

 **Summary**: The following function returns the MD5 digest from a file containing text.
 To use, call the function as follows: 
 `print getMd5Digest("path/to/file")`



#### getSha1Digest 

**Summary**: The following function returns the sha1 digest from a file containing text.
To use, call the function as follows:
`print getSha1Digest("path/to/file")`


## Author

**FileInfo**  [MPierre9](https://github.com/MPierre9), Released under the [MIT](./LICENSE) License.<br>
Authored and maintained by DIYgod with help from contributors ([list](https://github.com/DIYgod/FileInfo/contributors)).