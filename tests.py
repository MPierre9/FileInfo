import unittest
from getFilename import getFilename
from getFileSize import getFileSize
from getMd5Digest import getMd5Digest
from getSha1Digest import getSha1Digest 

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(getFilename("C:/user/mpierre/test.txt"),"test.txt")

    def test2(self):
        self.assertEqual(getFileSize("sizeTest.txt"),4)

    def test3(self):
        self.assertEqual(getMd5Digest("sizeTest.txt"),"b59c67bf196a4758191e42f76670ceba")

    def test4(self): 
        self.assertEqual(getSha1Digest("sizeTest.txt"),"011c945f30ce2cbafc452f39840f025693339c42")

if __name__ == '__main__':
    unittest.main()