# Nikko Rush
# 8/7/2017

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

    def _load_visualizaer(self):
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
        self._pmi.add_reset_listener(self._idea_list.clear_selection)
        self._pmi.add_reset_listener(self._relation_types.clear_selection)
        self._pmi.add_reset_listener(self._ts.clear)

        # Keep lists current with selection
        self._relation_types.add_select_listener(self._pmi.filter_relation)
        self._relation_types.add_select_listener(self._idea_list.clear_selection)
