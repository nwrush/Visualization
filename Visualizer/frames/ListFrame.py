# Nikko Rush
# 7/6/2017

from events import event, listener
from frames.VisualizerFrame import VisualizerFrame
from ui import topics_list


class ListFrame(VisualizerFrame):
    """description of class"""
    def __init__(self, parent, data=None):
        super(ListFrame, self).__init__(parent, data_manager=data)

        self.ui = topics_list.Ui_topicsList()
        self.ui.setupUi(self)

        self.ui.listWidget.itemClicked.connect(self._on_select)
        self._onselect_listener = listener.Listener()

    def add_item(self, item):
        all_items = self._select_all()
        all_items.append(str(item))
        self._add_items(sorted(all_items))

    def add_items(self, items):
        all_items = self._select_all()
        all_items.extend(map(str, items))
        self._add_items(sorted(all_items))

    def _select_all(self):
        return [self.ui.listWidget.item(i) for i in range(0, self.ui.listWidget.count())]

    def _add_items(self, items):
        self.clear_list()
        self.ui.listWidget.addItems(items)

    def remove_item(self, position):
        return self.ui.listWidget.takeItem(position)

    def clear_list(self):
        self.ui.listWidget.clear()

    def add_select_listener(self, func):
        self._onselect_listener.add(func)

    def has_select_listener(self, func):
        return self._onselect_listener.has_handler(func)

    def remove_select_listener(self, func):
        self._onselect_listener.remove(func)

    def clear_selection(self):
        self.ui.listWidget.clearSelection()

    def _on_select(self, selected_item):
        indexes = set()
        for item in self.ui.listWidget.selectedItems():
            indexes.add(self.data.idea_numbers[item.text()])

        eve = event.Event()
        eve.selected_indexes = indexes
        self._onselect_listener.invoke(eve)
