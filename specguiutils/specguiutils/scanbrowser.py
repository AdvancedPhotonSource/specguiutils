'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore

SCAN_COL_WIDTH = 40
CMD_COL_WIDTH = 240
NUM_PTS_COL_WIDTH = 40
MINIMUM_WIDGET_WIDTH = 420
SCAN_COL = 0
CMD_COL = 1
NUM_PTS_COL = 2

class ScanBrowser(qtGui.QDialog):
    '''
    '''
    # Define some signals that this class will provide to users
    scanSelected = qtCore.pyqtSignal(str, name="scanSelected")
               
    def __init__(self, parent=None):
        '''
        constructor
        '''
        super(ScanBrowser, self).__init__(parent)
        layout = qtGui.QHBoxLayout()
        self.scanList = qtGui.QTableWidget()
        self.scanList.setRowCount(1)
        self.scanList.setColumnCount(3)
        self.scanList.setColumnWidth(SCAN_COL, SCAN_COL_WIDTH)
        self.scanList.setColumnWidth(CMD_COL, CMD_COL_WIDTH)
        self.scanList.setColumnWidth(NUM_PTS_COL, NUM_PTS_COL_WIDTH)
        self.scanList.setHorizontalHeaderLabels(['S#', 'Command', 'Points'])
        self.scanList.setSelectionBehavior(qtGui.QAbstractItemView.SelectRows)
        self.setMinimumWidth(420)
        layout.addWidget(self.scanList)
        self.setLayout(layout)
        self.show()
        
        self.scanList.currentCellChanged[int, int, int, int].connect(self.scanSelectionChanged)
        
    def loadScans(self, scans):
        self.scans = scans
        self.scanList.setRowCount(len(self.scans.keys()) )
        row = 0
        scanKeys = self.scans.keys()
        scanKeys.sort(key=int)
        for scan in scanKeys:
            scanItem = qtGui.QTableWidgetItem(str(scans[scan].scanNum))
            self.scanList.setItem(row, SCAN_COL, scanItem)
            cmdItem = qtGui.QTableWidgetItem(scans[scan].scanCmd)
            self.scanList.setItem(row, CMD_COL, cmdItem)
            nPointsItem = qtGui.QTableWidgetItem(str(len(scans[scan].data_lines)))
            self.scanList.setItem(row, NUM_PTS_COL, nPointsItem)
            row += 1
            
    @qtCore.pyqtSlot(int, int, int, int)
    def scanSelectionChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        #print("Scan Selection Changed")
        self.scanSelected.emit(str(self.scanList.item(currentRow,0).text()))
            
        