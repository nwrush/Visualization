# Nikko Rush
# 8/7/2017

import PyQt5.QtWidgets as QtWidgets

from frames.VisualizerFrame import VisualizerFrame
from frames.PMIPlot import PMIPlot
from frames.TimeSeriesFrame import TimeSeriesFrame
from frames.ListFrame import ListFrame
from frames.RelationTypeFrame import RelationTypeFrame
from frames.TopRelations import TopRelations

class VisualizerWidget(VisualizerFrame):

    def __init__(self, parent, data_manager):
        super(VisualizerWidget, self).__init__(parent=parent)

        self._layout = QtWidgets.QGridLayout(self)
        self._data = data_manager
        self._load_visualizaer()


    def _load_visualizaer(self):
        self.pmi = PMIPlot(self, self._data)
        self.pmi.plot(sample=1000)
        self._layout.addWidget(self.pmi, 0, 1)

        self.ts = TimeSeriesFrame(self, self._data)
        self._layout.addWidget(self.ts, 0, 2)

        self.idea_list = ListFrame(self, data=self._data)
        self._layout.addWidget(self.idea_list, 0, 0)
        self.idea_list.add_items(self._data.idea_names.values())

        self.relation_types = RelationTypeFrame(self, data=self._data)
        self._layout.addWidget(self.relation_types, 1, 0)
        self.relation_types.color_buttons(self.pmi.color_samples)

        self.top_relation_1 = TopRelations(self, data=self._data, topic_index=0)
        self._layout.addWidget(self.top_relation_1, 1, 1)
        self.top_relation_2 = TopRelations(self, data=self._data, topic_index=1)
        self._layout.addWidget(self.top_relation_2, 1, 2)

        # PMI Select Listener
        self.pmi.add_select_listener(self.ts.plot_idea_indexes_event)
        self.pmi.add_select_listener(self.top_relation_1.set_idea_event)
        self.pmi.add_select_listener(self.top_relation_2.set_idea_event)

        # Idea list Select Listener
        self.idea_list.add_select_listener(self.pmi.filter_relation)

        # Relation types Select Listener
        self.relation_types.add_select_listener(self.pmi.filter_relation)

        # PMI reset Listeners
        self.pmi.add_reset_listener(self.idea_list.clear_selection)
        self.pmi.add_reset_listener(self.relation_types.clear_selection)
        self.pmi.add_reset_listener(self.ts.clear)

        # Keep lists current with selection
        self.relation_types.add_select_listener(self.pmi.filter_relation)
        self.relation_types.add_select_listener(self.idea_list.clear_selection)