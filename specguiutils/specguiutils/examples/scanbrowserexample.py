'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import sys
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
from specguiutils.scanbrowser import ScanBrowser
from spec2nexus.spec import SpecDataFile

FILE_MENU_TEXT = 'File'
OPEN_ACTION_TEXT = 'Open'

class TestWindow(qtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self.scanBrowser = ScanBrowser()
        self.setCentralWidget(self.scanBrowser)
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        self.scanBrowser.scanSelected[str].connect(self.handleScanChanged)
    
        fileMenu = menuBar.addMenu(FILE_MENU_TEXT)
        openAction = qtGui.QAction(OPEN_ACTION_TEXT, self)
        openAction.triggered.connect(self.openFile)
        
        fileMenu.addAction(openAction)
        self.show()
        
    def openFile(self):
        fileName = qtGui.QFileDialog.getOpenFileName(None, "Open Spec File")
        specFile = SpecDataFile(fileName)
        self.scanBrowser.loadScans(specFile.scans)
        
    @qtCore.pyqtSlot(str)
    def handleScanChanged(self, newScan):
        print("Test Code intecepted scan change %s" % newScan)
        
if __name__ == '__main__':
    app = qtGui.QApplication(sys.argv)
    mainForm = TestWindow()
    app.exec_()
    
