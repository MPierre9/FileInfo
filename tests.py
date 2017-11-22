import unittest
from getFilename import getFilename
from getFileSize import getFileSize
from getMd5Digest import getMd5Digest
from getSha1Digest import getSha1Digest 

class MyTest(unittest.TestCase):
    def testGetFilename(self):
        self.assertEqual(getFilename("C:/user/mpierre/test.txt"),"test.txt","Error: the expected file name is {1} however the result is {0}".format(getFilename("C:/user/mpierre/test.txt"),"test.txt"))

    def testGetFileSize(self):
        self.assertEqual(getFileSize("sizeTest.txt"),4,"Error: the expected file size is {1} however the result is {0}".format(getFileSize("sizeTest.txt"),4))

    def testGetMd5Digest(self):
        self.assertEqual(getMd5Digest("sizeTest.txt"),"b59c67bf196a4758191e42f76670ceba","Error: the expected file size is {1} however the result is {0}".format(getMd5Digest("sizeTest.txt"),"b59c67bf196a4758191e42f76670ceba"))

    def testGetSha1Digest(self): 
        self.assertEqual(getSha1Digest("sizeTest.txt"),"011c945f30ce2cbafc452f39840f025693339c42","Error: the expected file size is {1} however the result is {0}".format(getMd5Digest("sizeTest.txt"),"011c945f30ce2cbafc452f39840f025693339c42"))

if __name__ == '__main__':
    unittest.main()