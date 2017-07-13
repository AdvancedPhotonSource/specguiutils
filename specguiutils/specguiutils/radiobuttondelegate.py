'''
 Copyright (c) 2017, UChicago Argonne, LLC
 See LICENSE file.
'''

import PyQt4.QtGui as qtGui
import PyQt4.QtCore as qtCore
import logging
logger = logging.getLogger(__name__)

class RadioButtonDelegate(qtGui.QStyledItemDelegate):
    
    def __init__(self, parent=None):
        super(RadioButtonDelegate, self).__init__(parent)
        

    def createEditor(self, parent, option, index):
        radio = qtGui.QRadioButton(parent)
        
#        radio.setChecked[bool].connect(self.setChecked)
        self.editor = radio
        self.editor.setAutoFillBackground(True)
        return radio
    
    def setEditorData(self, editor, value):
#        print("settingEditorData %s" % value)
        editor.setChecked(value.data().toBool())
        
    @qtCore.pyqtSlot(bool)
    def setChecked(self, checked):
        logger.debug("setChecked")
        self.commitData(self.sender())
        
    @qtCore.pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

    def setModelData(self, editor, model, index):
#        print("gettingModelData %d, %d" %(index.row(), index.column()))
        model.setData(index, bool(editor.isChecked()))
        
    def setButtonGroup(self, buttonGroup):
        buttonGroup.addButton(self.editor)