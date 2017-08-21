'''
Created on Aug 21, 2017

@author: hammonds
'''
import unittest
from specguiutils.test import testScanBrowser, testCounterSelectorModel


def suite():
    suite = unittest.TestSuite()
    suite.addTest(testScanBrowser.TestScanBrowserTest())
    suite.addTest(testCounterSelectorModel.CounterSelectorTableModelTest())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)