
'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''

import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
import logging
from specguiutils.view.dataitem import DataItem
logger = logging.getLogger(__name__)

class SpecDataFileItem(DataItem):
    
    def __init__(self, fileName, specDataFile):
        super(SpecDataFileItem, self).__init__(fileName)
        self.specDataFile = specDataFile
        self.setData(self.specDataFile.fileName)
        
    def getSpecDataFile(self):
        return self.specDataFile
    
#     def text(self):
#         logger.debug("Enter")
#         logger.debug("specDataFile.fileName %s" % self.specDataFile.fileName)
#         return self.specDataFile.fileName 
#     
#     def data(self, role=qtCore.Qt.UserRole + 1):
#         return self.specDataFile.fileName 

