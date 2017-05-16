'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import os
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
from copy_reg import constructor

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
        numCounterOpts = len(self.monitorOpts)
        if numCounterOpts == 0:
            self.counterList.setColumnCount(numCounterOpts+1)
            headerLabels = ["Counter" ,].append(self.counterOpts)
            self.counterlist.setHorzontalHeaderLabels(headerLabels)
        else:
            self.counterList.setColumnCount(1)
            self.counterList.setHorizonatlHeaderLables(["Counter",])
            
            