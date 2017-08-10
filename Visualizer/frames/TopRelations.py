# Nikko Rush
# 7/10/2017

import PyQt5.QtWidgets as QtWidgets

import numpy as np

from frames.VisualizerFrame import VisualizerFrame
from ui import top_relations

class TopRelations(VisualizerFrame):
    
    def __init__(self, parent, data, topic_index=0):
        super(TopRelations, self).__init__(parent, data_manager=data)

        self.ui = top_relations.Ui_topRelation()
        self.ui.setupUi(self)

        self._index = topic_index

    def set_idea_name(self, name):
        return self.set_idea_index(self.data.idea_numbers[name])

    def set_idea_index(self, index):
        strengths = []
        pmi, ts_cor = self.data.pmi, self.data.ts_correlation
        for i in range(0, self.data.num_ideas):
            for j in range(i+1, self.data.num_ideas):
                if i != index and j != index:
                    continue
                point_pmi = pmi[i, j]
                point_cor = ts_cor[i, j]
                if np.isnan(point_pmi) or np.isnan(point_cor):
                    continue
                if np.isinf(point_pmi) or np.isinf(point_cor):
                    continue

                strength = point_pmi * point_cor
                type = self._get_point_type(point_pmi, point_cor)

                other_topic_name = self.data.idea_names[i if i != index else j]
                self._insert_sorted(strengths, ("{n:.{d}}".format(n=strength, d=3), type, other_topic_name), sort_index=0)

        self._clear_list()
        self._insert_list(strengths)

        # Update the frame title
        self.ui.relationName.setText(self.data.idea_names[index])

    @staticmethod
    def _get_point_type(point_pmi, point_cor):
        if 0 <= point_pmi and point_cor < 0:
            return "Tryst"
        elif 0 <= point_pmi and 0 <= point_cor:
            return "Friends"
        elif point_pmi < 0 and point_cor < 0:
            return "Head-To-Head"
        elif point_pmi < 0 and 0 <= point_cor:
            return "Arms-Race"

    @staticmethod
    def _insert_sorted(items, item, sort_index=0):
        index = 0
        for index in range(len(items)):
            list_item = items[index]

            if item[sort_index] >= list_item[sort_index]:
                break
        items.insert(index, item)

    def _insert_list(self, items):
        tbl = self.ui.tableWidget
        for i, relation in enumerate(items):
            tbl.insertRow(i)
            for j, item in enumerate(relation):
                qtbl_item = QtWidgets.QTableWidgetItem(item)
                tbl.setItem(i, j, qtbl_item)

    def set_idea_event(self, event):
        self.set_idea_index(event.selected_indexes[self._index])

    def clear(self):
        self.ui.relationName.clear()
        self._clear_list()

    def _clear_list(self):
        self.ui.tableWidget.clearContents()
