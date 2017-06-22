'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
import logging
logger = logging.getLogger(__name__)

COUNTER_HEADER_INIT = ['Counter',]

class CounterSelectorTableModel(qtCore.QAbstractTableModel):

    def __init__(self,parent=None, counterOpts=None ):
        super(CounterSelectorTableModel, self).__init__(parent)
        self.counterData = [[0], ]
        self.setCounterOptions(counterOpts)
        self.initializeBlankRow()
        
    def initializeDataRows(self, scanLabels):
        logger.debug("Entering %s" % scanLabels)

        self.beginRemoveRows( qtCore.QModelIndex(), 0, self.rowCount() -1 )
        for row in range(self.rowCount()):
            self.removeRow(row)
        self.counterData = [[0], ]
        self.endRemoveRows()
        dataKeys = scanLabels
        logger.debug ("dataKeys %s" % dataKeys)
#         print "self.counterOpts %s " % self.counterOpts
        self.beginInsertRows(qtCore.QModelIndex(), 0, len(dataKeys)-1)
        
        self.counterData = [[0 for i in range(len(self.counterOpts))] for j in range(len(scanLabels))]
#         print "counterData %s " % self.counterData
        #print ("rowCount %d " % self.rowCount())
#        buttonGroups = []

#         for col in range(len(self.counterOpts)):
#             buttonGroups.append(qtGui.QButtonGroup())
        for row in range(len( dataKeys)):
            #print ("Setting key %s row %d" % (dataKeys[row], row))
            self.setRowName(row, dataKeys[row])
            for col in range(1, len(self.counterOpts)):
                self.setItem(row, col, False)
#        self.dataChanged.emit(self.index(0,0), self.index(len(dataKeys), len(self.counterOpts)))
        self.endInsertRows()
#         success = self.insertRows(0, len(dataKeys))
#         print ("Success adding rows %s" % success)
        
        
    def headerData(self, col, orientation, role):
        if orientation == qtCore.Qt.Horizontal and role == qtCore.Qt.DisplayRole:
            return self.counterOpts[col]

    def initializeBlankRow(self):
        if self.counterOpts == None:
            self.counterData = [[],]
        else:
            self.counterData = [['1',],]
#             print "counterOpts %s" % self.counterOpts
            if len(self.counterOpts) == 1:
                self.counterData = [['1',],]
            elif len(self.counterOpts) > 1 :
                self.counterData = [['1',],]
                for item in self.counterOpts[1:]:
                    self.counterData[0].append(False)
        self.insertRow(0)

#     def initializeRowValues(self, row):
#         '''
#         Initialize Row data to False
#         '''
#         if len(self.counterData) < row+1 :
#             raise(TypeError("Wrong row Number %d only %d rows" %(row, len(self.counterData)) ))
#         col = 1
#         for item in self.counterOpts():
#             self.counterData[row][col] = False
#         self.dataChanged.emit(self.index(row,1), self.index(row,len(self.counterOpts)-1))
#         
        
    def setHeaderData(self, counterOpts=None):
        self.counterOpts = counterOpts
        self.headerDataChanged.emit(qtCore.Qt.Horizontal, 0, len(self.counterOpts))
        
        
    def columnCount(self, parent=qtCore.QModelIndex()):
        return  len(self.counterOpts)
    
    def rowCount(self, parent=qtCore.QModelIndex()):
#         print("rowCount: %d" % len(self.counterData))
        return len(self.counterData)
    
    def data(self, modelIndex, role = qtCore.Qt.DisplayRole):
        if not modelIndex.isValid():
            return None
        elif role != qtCore.Qt.DisplayRole:
            return None
        returnData = None
        try:
            returnData = self.counterData[modelIndex.row()][modelIndex.column()]
        except IndexError as ie:
            logger.debug( "counterData %s " % self.counterData)
            logger.debug( "row, column %d, %d" % (modelIndex.row(), modelIndex.column()))
            logger.debug(  "row values %s" % str(self.counterData[modelIndex.row()]))
            logger.debug(  "value %s" % str(self.counterData[modelIndex.row()][modelIndex.column()]))
            raise ie
        return returnData

    
    def setCounterOptions(self, counterOpts):
#        self.counterOpts = counterOpts
        logger.debug ("setCounterOpts %s " %  counterOpts)
        if counterOpts is not None:
            numCounterOpts = len(counterOpts)
        else:
            numCounterOpts = 0
        if numCounterOpts != 0:
#             self.counterList.setColumnCount(numCounterOpts+1)
            headerLabels = None
#             print "setCounterOpts: headerLabels %s" % headerLabels
#             print "setCounterOpts: COUNTER_HEADER_INIT %s" % COUNTER_HEADER_INIT
            headerLabels = COUNTER_HEADER_INIT[:]
#             print "setCounterOpts: headerLabels %s" % headerLabels
            headerLabels.extend(counterOpts)
#             print "setCounterOpts: headerLabels %s" % headerLabels
            self.setHeaderData(headerLabels)
        else:
            #self.counterList.setColumnCount(1)
            self.setHeaderData(COUNTER_HEADER_INIT)

    def setRowName(self, row, name):
        if len(self.counterData) < row+1 :
            raise(TypeError("Wrong row Number %d only %d rows" %(row, len(self.counterData)) ))
        self.counterData[row][0] = name
        self.setData(self.index(row, 0), name)
#         print "setRowName: counterData %s " % self.counterData
#         print ("setRowName Setting self.counterData[%d][0] %s" % (row, name) )
        self.dataChanged.emit(self.index(row,0), self.index(row,0))
        
    def setItem(self, row, col, value):
        if len(self.counterData) < row+1 :
            raise(TypeError("Wrong row Number %d only %d rows" %(row, len(self.counterData)) ))
        try:
            self.counterData[row][col] = value
            self.dataChanged.emit(self.index(row,col), self.index(row,col))
        except IndexError as ie:
            print ("Index Error: trying to set self.counterData[%d][%d]" % (row, col))
            print ("len(self.counterData) %d " % len(self.counterData))
            print ("len(self.counterData[row]) %d " % len(self.counterData[row]))
            
        
        