# FileInfo
![Travis Build](https://travis-ci.org/MPierre9/FileInfo.svg?branch=master)
## Summary
File Info is a Python library which contains various useful file functions. The purpose of this library is tp provide easy and intuitive ways to get information/data about a file. Currently there are four functions included in the FileInfo library: 

1. getFileSize
1. getFilename
1. getMd5Digest
1. getSha1Digest

## Prerequisites 
- Python 2.7 or higher
- Python IDE of your choice Ex. [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio 2015](https://www.visualstudio.com/downloads/)

## Installation 

1. Install the latest version of [Python](https://www.python.org/) 

1. Install/Start your preferred Python IDE (FileInfo was developed in [Visual Studio 2015](https://www.visualstudio.com/downloads/)

1. Clone the FileInfo repository `git clone https://github.com/MPierre9/FileInfo.git`

1. Import FileInfo functions in your project: 
   * `from getFilename import getFilename`
   * `from getFileSize import getFileSize`
   * `from getMd5Digest import getMd5Digest`
   * `from getSha1Digest import getSha1Digest` 
   
1. You're good to go! Feel free to use FileInfo's functions in your code!




## Usage 

#### getFileSize

**Summary**: This function returns the size of a file, in bytes
To use, call the function as follows: 
`print getFileSize("path/to/file")`
Output: `4`

#### getFilename

**Summary**: The following function returns the filename when given a path
 To use simply pass your desired path as a string into the function getFilename:
 `print getFilename("path/to/file");`
 Output: `Example.txt`


 #### getMd5Digest 

 **Summary**: The following function returns the MD5 digest from a file containing text.
 To use, call the function as follows: 
 `print getMd5Digest("path/to/file")`
 Output: `b59c67bf196a4758191e42f76670ceba`



#### getSha1Digest 

**Summary**: The following function returns the sha1 digest from a file containing text.
To use, call the function as follows:
`print getSha1Digest("path/to/file")`
Output: `011c945f30ce2cbafc452f39840f025693339c42`

## Contributing

Contributions are welcome! Please read the [contribution document](./CONTRIBUTE.md) for tips and guidelines on contributing

## Author

**FileInfo**  [MPierre9](https://github.com/MPierre9), Released under the [MIT](./LICENSE) License.<br>
Authored and maintained by MPierre9 with help from contributors ([list](https://github.com/MPierre9/FileInfo/contributors)).
