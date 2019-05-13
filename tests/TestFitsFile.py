import unittest
import PythonFits
import numpy as np

#NEED BETTER TESTING...

class TestFitsFile(unittest.TestCase):

    def setUp(self):
        self.fitsFile = PythonFits.PythonFits("C:\\Users\\aanania\\Documents\\ts_python_fitsfile", "testFits", separator='\\')

    def test_addDataAndCloseFile(self):
        data = np.arange(100.0)
        self.fitsFile.addData(data)
        self.fitsFile.closeFile()

    def test_testChecksum(self):
        a = len(self.fitsFile.getChecksum())
        self.assertGreater(a, 1)


if __name__ == "__main__":
    unittest.main()