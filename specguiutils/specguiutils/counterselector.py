'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import os
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore

COUNTER_LABEL_COLUMN = 0

class CounterSelector(qtGui.QDialog):
    '''
    GUI to display the monitors for a selected scan
    '''
    
    def __init__(self, parent=None, counterOpts=None):
        '''
        constructor
        '''
        super(CounterSelector, self).__init__(parent)
        self.counterOpts = counterOpts
        layout = qtGui.QHBoxLayout()
        self.counterList = qtGui.QTableWidget()
        self.counterList.setRowCount(1)
        if counterOpts is not None:
            numCounterOpts = len(self.counterOpts)
        else:
            numCounterOpts = 0
        if numCounterOpts != 0:
            self.counterList.setColumnCount(numCounterOpts+1)
            headerLabels = ["Counter" ,]
            headerLabels.extend(self.counterOpts)
            print headerLabels
            self.counterList.setHorizontalHeaderLabels(headerLabels)
        else:
            self.counterList.setColumnCount(1)
            self.counterList.setHorizontalHeaderLabels(["Counter",])
        layout.addWidget(self.counterList)
        self.setLayout(layout) 
        self.show()
        
    def changeScanCounters(self, scan):
        print("changeScanCounters %s" % scan)
        for row in range(self.counterList.rowCount()):
            self.counterList.removeRow(row)
        dataKeys = scan.L
        self.counterList.setRowCount(len(dataKeys))
        for row in range(len( dataKeys)):
            counterLabel = qtGui.QTableWidgetItem(dataKeys[row])
            self.counterList.setItem(row, COUNTER_LABEL_COLUMN, counterLabel)
            for col in range(1, len(self.counterOpts) +1):
                booleanLabel = qtGui.QTableWidgetItem(1)
                booleanLabel.data(qtCore.Qt.CheckStateRole)
                booleanLabel.data.setCheckedState(qtCore.Qt.Unchecked)
                self.counterList.setItem(row, col, booleanLabel)
        