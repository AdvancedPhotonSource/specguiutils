'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import sys
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
from specguiutils.scanbrowser import ScanBrowser
from spec2nexus.spec import SpecDataFile
from specguiutils.examples.BaseExample import BaseExample


class ScanBrowserExample(BaseExample):
    def __init__(self, parent=None):
        super(ScanBrowserExample, self).__init__(parent)
        self.scanBrowser = ScanBrowser()
        self.scanBrowser.scanSelected[str].connect(self.handleScanChanged)
        self.setCentralWidget(self.scanBrowser)
        self.connectOpenFileAction(self.openFile)
        self.show()
        
        
    @qtCore.pyqtSlot(str)
    def handleScanChanged(self, newScan):
        print("Test Code intecepted scan change %s" % newScan)

    @qtCore.pyqtSlot()
    def openFile(self):
        fileName = qtGui.QFileDialog.getOpenFileName(None, "Open Spec File")
        self.specFile = SpecDataFile(fileName)
        self.scanBrowser.loadScans(self.specFile.scans)
        
if __name__ == '__main__':
    app = qtGui.QApplication(sys.argv)
    mainForm = ScanBrowserExample()
    app.exec_()
    
