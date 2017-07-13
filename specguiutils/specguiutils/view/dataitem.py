'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''

import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
import logging
logger = logging.getLogger(__name__)

class DataItem(qtGui.QStandardItem):

    def __init__(self, name):
        super(DataItem, self).__init__(name)

