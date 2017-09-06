# Nikko Rush
# 9/5/2017

import PyQt5.QtCore as QtCore
from PyQt5.QtCore import Qt

class ListModel(QtCore.QAbstractListModel):
    
    def __init__(self, data, parent=None):
        super(ListModel, self).__init__(parent)

        self._data = sorted(list(data))

    def rowCount(self, parent):
        return len(self._data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()]
        return QtCore.QVariant() # Return an invalid variant

class ListModelFilter(QtCore.QSortFilterProxyModel):
    
    def __init__(self, parent=None):
        super(ListModelFilter, self).__init__(parent)
