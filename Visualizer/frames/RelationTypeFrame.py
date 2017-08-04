# Nikko Rush
# 7/6/2017

import functools
from PyQt5 import QtWidgets

import numpy as np

from events import listener, event
from frames.VisualizerFrame import VisualizerFrame
from ui import relation_types


def _sort_by_strength(data, strength_index=2):
    sorted_list = sorted(data, key=lambda item: abs(item[strength_index]))
    sorted_list.reverse()
    return sorted_list


class RelationTypeFrame(VisualizerFrame):

    def __init__(self, parent, data):
        super(RelationTypeFrame, self).__init__(parent=parent, data_manager=data)

        self.ui = relation_types.Ui_relationTypes()
        self.ui.setupUi(self)

        self.data = data
        self.types = self.data.relation_types

        self._buttons = []
        self._tables = []
        self._config_ui()

        self.list_data = {name: [] for name in self.types}

        self.active_index = None
        self._onselect_listener = listener.Listener()

        self._determine_relations()
        self._fill_tables()

        self._set_active_index(0)
        pass

    def _config_ui(self):
        for i, name in enumerate(self.types):
            btn_name = "{0}Button".format(name.lower().replace('-', ''))
            tbl_name = "{0}Table".format(name.lower().replace('-', ''))

            btn = self.findChild(QtWidgets.QPushButton, btn_name)
            tbl = self.findChild(QtWidgets.QTableWidget, tbl_name)

            self._buttons.append(btn)
            self._tables.append(tbl)

            btn.clicked.connect(functools.partial(self._btn_click, name))
            tbl.itemSelectionChanged.connect(self._on_select)
            tbl.hide()

    def _determine_relations(self):
        pmi = self.data.pmi
        ts_correlation = self.data.ts_correlation
        trysts, friends, head, arms = [], [], [], []
        num_ideas = self.data.num_ideas
        cnt = 0
        for i in range(0, num_ideas):
            for j in range(i + 1, num_ideas):
                point_pmi = pmi[i, j]
                point_cor = ts_correlation[i, j]
                if np.isnan(point_pmi) or np.isnan(point_cor):
                    continue
                if np.isinf(point_pmi) or np.isinf(point_cor):
                    continue
                cnt += 1
                strength = point_pmi * point_cor

                if 0 <= point_pmi and point_cor < 0:
                    trysts.append((i,j,strength))
                elif 0 <= point_pmi and 0 <= point_cor:
                    friends.append((i, j, strength))
                elif point_pmi < 0 and point_cor < 0:
                    head.append((i, j, strength))
                elif point_pmi < 0 and 0 <= point_cor:
                    arms.append((i, j, strength))

        assert len(trysts) + len(friends) + len(head) + len(arms) == cnt

        self._add_to_list(friends, "Friends", sort=True, top=25)
        self._add_to_list(trysts, "Tryst", sort=True, top=25)
        self._add_to_list(head, "Head-To-Head", sort=True, top=25)
        self._add_to_list(arms, "Arms-Race", sort=True, top=25)

    def _add_to_list(self, items, name, sort=True, top=None):
        data = self.list_data[name]
        if sort:
            items = _sort_by_strength(items)

        if top is not None:
            items = items[:top]

        data.extend(items)

    def _fill_tables(self):
        for index, name in enumerate(self.data.relation_types):
            raw_data = self.list_data[name]
            tbl = self._tables[index]

            data = self._get_output_repr(raw_data)

            for i, relation in enumerate(data):
                tbl.insertRow(i)
                for j, item in enumerate(relation):
                    qtbl_item = QtWidgets.QTableWidgetItem(item)
                    tbl.setItem(i, j, qtbl_item)

    def _get_output_repr(self, items):
        outputs = []
        for item in items:
            output = ("{n:.{d}}".format(n=item[2], d=4), self.data.idea_names[item[0]], self.data.idea_names[item[1]])
            outputs.append(output)
        return outputs

    def clear_lists(self):
        for table in self._tables:
            table.clearContents()

    def add_select_listener(self, func):
        self._onselect_listener.add(func)

    def has_select_listener(self, func):
        return self._onselect_listener.has_handler(func)

    def remove_select_listener(self, func):
        self._onselect_listener.remove(func)

    def _on_select(self):
        col_count = self._tables[self.active_index].columnCount()

        selected_items = dict()
        for item in self._tables[self.active_index].selectedItems():
            row, col = item.row(), item.column()
            if row not in selected_items.keys():
                selected_items[row] = [0] * col_count
            selected_items[row][col] = item.text()

        if not len(selected_items):
            return None

        selected_indexes = list()
        for row, item in selected_items.items():
            selected_indexes.append(self.data.idea_numbers[item[1]])
            selected_indexes.append(self.data.idea_numbers[item[2]])

        eve = event.Event()
        eve.selected_indexes = selected_indexes
        eve.should_select = True
        self._onselect_listener.invoke(eve)
        
    def _btn_click(self, name):
        self._set_active(name)

    def _set_active(self, name):
        index = self.types.index(name)
        return self._set_active_index(index)

    def _set_active_index(self, index):
        if self.active_index is not None:
            self._tables[self.active_index].hide()
            self._tables[self.active_index].clearSelection()

            font = self._buttons[self.active_index].font()
            font.setUnderline(False)
            self._buttons[self.active_index].setFont(font)

        self._tables[index].show()

        font = self._buttons[index].font()
        font.setUnderline(True)
        self._buttons[index].setFont(font)

        self.active_index = index

    def clear_selection(self):
        self.lists[self.active_index].clearSelection()

    def color_buttons(self, color_map):
        for btn, name in zip(self.buttons, self.types):
            btn['background'] = color_map[name]

    def color_changed(self, pmi_frame):
        self.color_buttons(pmi_frame.color_samples)