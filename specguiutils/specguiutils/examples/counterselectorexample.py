'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''

import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
from specguiutils.scanbrowser import ScanBrowser
from specguiutils.counterselector import CounterSelector
from specguiutils.examples.BaseExample import BaseExample
from spec2nexus.spec import SpecDataFile
import sys

COUNTER_OPTS = ["X", "Y", "Mon"]
class CounterSelectorExample(BaseExample):
    '''
    '''
    
    def __init__(self, parent=None):
        super(CounterSelectorExample, self).__init__(parent)
        mainWidget = qtGui.QWidget()
        layout = qtGui.QVBoxLayout()
        self.scanBrowser = ScanBrowser()
        self.counterSelector = CounterSelector(counterOpts=COUNTER_OPTS)
        self.scanBrowser.scanSelected[str].connect(self.handleScanSelection)
        layout.addWidget(self.scanBrowser)
        layout.addWidget(self.counterSelector)
        
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)
        self.connectOpenFileAction(self.openFile)
        self.show()
        
    @qtCore.pyqtSlot(str)
    def handleScanSelection(self, newScan):
        print ("handling selection of scan %s" %newScan)
        self.counterSelector.changeScanCounters(self.specFile.scans[str(newScan)])
        
    @qtCore.pyqtSlot()
    def openFile(self):
        fileName = qtGui.QFileDialog.getOpenFileName(None, "Open Spec File")
        self.specFile = SpecDataFile(fileName)
        self.scanBrowser.loadScans(self.specFile.scans)

if __name__ == '__main__':
    app = qtGui.QApplication(sys.argv)
    mainForm = CounterSelectorExample()
    app.exec_()
    
