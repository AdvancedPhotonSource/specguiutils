'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import sys
import unittest
from PyQt5.QtTest import QSignalSpy, QTest
from PyQt5.QtWidgets import QApplication
from specguiutils.scanbrowser import ScanBrowser
from spec2nexus.spec import SpecDataFile
import specguiutils
app =  QApplication(sys.argv)

COUNTER_OPTS_1 = ["X", "Y", "Z"]
COUNTER_NAMES_1 = ["A", "B", "C"]

class Test(unittest.TestCase):


    def setUp(self):
        self.scanBrowser = ScanBrowser()
        

    def tearDown(self):
        pass


    def testLoadScans(self):
        specFile = "/Volumes/RSM_DATA/DanielHaskel/Brian-Nick/Fluorescence/lineup"
        specData = SpecDataFile(specFile)
        spy = QSignalSpy(self.scanBrowser.scanLoaded)
        self.scanBrowser.loadScans(specData.scans, newFile=True)
        self.assertEqual(len(spy), 1)
        self.assertEqual(self.scanBrowser.scanList.rowCount(),
                         len(specData.getScanNumbers()))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()