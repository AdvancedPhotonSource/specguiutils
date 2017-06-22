'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import os
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
from PyQt4.Qt import QButtonGroup
from specguiutils.model.counterselectortablemodel import CounterSelectorTableModel
from specguiutils.radiobuttondelegate import RadioButtonDelegate
from specguiutils.view.counterselectorview import CounterSelectorView
import logging
logger = logging.getLogger(__name__)

COUNTER_LABEL_COLUMN = 0
COUNTER_HEADER_INIT = ['Counter',]

class CounterSelector(qtGui.QDialog):
    '''
    GUI to display the monitors for a selected scan
    '''
    # signal params (counterName, col, newVal)
    counterOptChanged = qtCore.pyqtSignal(str, int, bool, name='counterOptChanged')

    def __init__(self, parent=None, counterOpts=None):
        '''
        constructor
        '''
        super(CounterSelector, self).__init__(parent)
        layout = qtGui.QHBoxLayout()
        self.counterModel = CounterSelectorTableModel(parent=self, counterOpts=counterOpts)
        self.counterView = CounterSelectorView(parent, tableModel=self.counterModel)
        self.counterView.setModel(self.counterModel)
        self.counterModel.headerDataChanged.connect(self.counterView.headerChanged)
        layout.addWidget(self.counterView)
        self.setLayout(layout) 
        self.show()

    

    @qtCore.pyqtSlot(qtGui.QTableWidgetItem)
    def flagChangingOpts(self, item):
        logger.debug( "Entering flagChangingOpts")
        row = item.row()
        col = item.column()
        logger.debug ("row %d, column %d" % (row, col))
        nameItem = self.counterList.item(row, 0)
        counter = str(nameItem.text())
        value = item.checkState()
        #print ("name item %s, %s" % (nameItem, nameItem.text()))
        if value == True:
            for otherRows in range(self.counterListModel.rowCount()):
                otherItems = self.counterList.item(otherRows, col)
                if otherItems != item:
                    otherItems.setCheckState(False )
                
        self.counterOptChanged.emit(counter, col-1, value )
        logger.debug("Exiting ")

    def getSelectedCounters(self):
        counters = self.counterView.getSelectedCounters()
        logger.debug ("counters %s" %counters) 
        return counters

    def getSelectedCounterNames(self, counters):
        counterNames = []
        logger.debug ("counters %s" % counters)
        for counter in range(len(counters)):
            index = self.counterModel.index(counters[counter], 0,)
            name = str(self.counterModel.data(index))
            counterNames.append(name)
        logger.debug ("counters %s" % counterNames)
        return counterNames
        
    def setCurrentCounter(self, row):
        self.counterView.setCurrentIndex(self.counterModel.index(row,0))
        
    def setSelectedCounters(self, selections):
        logger.debug("Entering data size %d, %d" % (self.counterModel.rowCount(), self.counterModel.columnCount()))
        logger.debug("trying to set selections %s " % selections)
        for row in range(self.counterModel.rowCount()):
            for column in range(len(selections)):
                if not (selections[column] == ''):
                    nameIndex = self.counterModel.index( row,0)
                    logger.debug("nameIndex: %s" % nameIndex)
                    nameWidget = self.counterModel.data(nameIndex)
                    if str(nameWidget) == selections[column]:
                        self.counterModel.setItem(row, column+1, True)
                else:
                    self.counterModel.setItem(0, column+1, True)
