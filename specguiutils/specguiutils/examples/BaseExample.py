'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''
import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore

FILE_MENU_TEXT = 'File'
OPEN_ACTION_TEXT = 'Open'

class BaseExample(qtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(BaseExample, self).__init__(parent)
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
    
        fileMenu = menuBar.addMenu(FILE_MENU_TEXT)
        self.openAction = qtGui.QAction(OPEN_ACTION_TEXT, self)
        fileMenu.addAction(self.openAction)
        
    def connectOpenFileAction(self, openFileAction):
        self.openAction.triggered.connect(openFileAction)
