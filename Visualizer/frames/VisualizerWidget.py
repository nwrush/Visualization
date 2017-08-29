# Nikko Rush
# 8/7/2017

import logging

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTabWidget, QSplitter, QFileDialog

from events.listener import Listener
from frames.VisualizerFrame import VisualizerFrame
from frames.PMIPlot import PMIPlot
from frames.TimeSeriesFrame import TimeSeriesFrame
from frames.ListFrame import ListFrame
from frames.RelationTypeFrame import RelationTypeFrame
from frames.TopRelations import TopRelations
from ui import visualizer


class VisualizerWidget(VisualizerFrame):
    def __init__(self, parent, data_manager):
        super(VisualizerWidget, self).__init__(parent=parent)

        self.ui = visualizer.Ui_visualizaerWidget()
        self.ui.setupUi(self)

        self._data = data_manager
        self._load_visualizaer()

        self._reset_listener = Listener()

    def sizeHint(self):
        return self.parent().size()

    def _load_visualizaer(self):
        logging.error("This was not an error")
        self._pmi = PMIPlot(self, self._data)
        self._pmi.plot(sample=1000)
        self.ui.pmiWidget.layout().addWidget(self._pmi)

        self._ts = TimeSeriesFrame(self, self._data)
        self.ui.tsWidget.layout().addWidget(self._ts)

        self._idea_list = ListFrame(self.ui.tabWidget, data=self._data)
        self.ui.tabWidget.insertTab(0, self._idea_list, "Ideas")
        self._idea_list.add_items(self._data.idea_names.values())

        self._relation_types = RelationTypeFrame(self, data=self._data)
        self.ui.tabWidget.insertTab(1, self._relation_types, "Types")
        self._relation_types.color_tabs(self._pmi.color_samples)

        self._top_relation_1 = TopRelations(self, data=self._data, topic_index=0)
        self.ui.tabWidget.insertTab(2, self._top_relation_1, "Top Relation 1")
        self._top_relation_2 = TopRelations(self, data=self._data, topic_index=1)
        self.ui.tabWidget.insertTab(3, self._top_relation_2, "Top Relation 2")

        # PMI Select Listener
        self._pmi.add_select_listener(self._ts.plot_idea_indexes_event)
        self._pmi.add_select_listener(self._top_relation_1.set_idea_event)
        self._pmi.add_select_listener(self._top_relation_2.set_idea_event)

        # Idea list Select Listener
        self._idea_list.add_select_listener(self._pmi.filter_relation)

        # Relation types Select Listener
        self._relation_types.add_select_listener(self._pmi.filter_relation)

        # PMI reset Listeners
        self._pmi.add_reset_listener(self._clear_list_selections_factory())
        self._pmi.add_reset_listener(self._ts.clear)

        # Keep lists current with selection
        self._relation_types.add_select_listener(self._pmi.filter_relation)

        # Clear other lists on selection
        self._relation_types.add_select_listener(self._clear_list_selections_factory(self._relation_types))
        self._idea_list.add_select_listener(self._clear_list_selections_factory(self._idea_list))
        self._top_relation_1.add_select_listener(self._clear_list_selections_factory(self._top_relation_1))
        self._top_relation_2.add_select_listener(self._clear_list_selections_factory(self._top_relation_2))

        # Auxillary data structures
        self._lists = {self._idea_list, self._relation_types, self._top_relation_1, self._top_relation_2}

    def resizeEvent(self, event):
        dpi = self.physicalDpiX()
        # Make the width of the screen 3 inches or one fifth the width of the screen
        self.ui.tabWidget.setFixedWidth(min(3*dpi, int(self.size().width()/5)))
        super(VisualizerWidget, self).resizeEvent(event)

    def _clear_list_selections_factory(self, caller=None):
        def func():
            for item in self._lists:
                if item == caller:
                    continue
                item.clear_selection()
        return func

    def save_pmi(self):
        self._save_plot(self._pmi, "PMI")

    def save_ts(self):
        self._save_plot(self._ts, "Time Series")

    def save_both(self):
        self._save_plot(self._pmi, "PMI")
        self._save_plot(self._ts, "Time Series")

    def _save_plot(self, target, plot_name):
        if not target.confirm_on_empty(plot_name):
            return None

        dialog = QFileDialog(self)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setFileMode(QFileDialog.AnyFile)
        formats = self._mpl_output_formats(self._pmi)
        dialog.setNameFilters(["Matplotlib Formats " + formats, "All Files (*)"])
        if dialog.exec():
            target.save_plot(dialog.selectedFiles()[0])

    @staticmethod
    def _mpl_output_formats(widget):
        items = []
        for key in widget.get_supported_formats():
            items.append("*.{0}".format(key))
        return '(' + ', '.join(items) + ')'
