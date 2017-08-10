# Nikko Rush
# 7/18/17

import os
import os.path
from pathlib import Path
import queue
import subprocess
import threading

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QWidget

from frames.VisualizerFrame import VisualizerFrame
from ui import preprocessor_form
from ui import preprocessor_run

RUNTYPE_OPTIONS = ["Keywords", "Topics"]
GROUP_BY = ["Year", "Month", "Quarter"]

class PreprocessorController(VisualizerFrame):

    def __init__(self, parent, finished_callback=None):
        super(PreprocessorController, self).__init__(parent=parent)

        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)

        self._form_widget = QWidget(self)
        self._form_ui = preprocessor_form.Ui_preprocessorForm()
        self._form_ui.setupUi(self._form_widget)
        self._layout.addWidget(self._form_widget)
        self._connect_form_ui()

        self._run_widget = QWidget(self)
        self._run_ui = preprocessor_run.Ui_preprocessorRun()
        self._run_ui.setupUi(self._run_widget)
        self._layout.addWidget(self._run_widget)
        self._connect_run_ui()

        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.setInterval(500)

        self._preprocessor_thread = None
        self._message_queue = queue.Queue()
        self._callback = finished_callback

        self.output_name = None

    def _connect_form_ui(self):
        # Setup the option combo box
        ui = self._form_ui
        ui.optionBox.currentIndexChanged.connect(self._option_box_changed)
        self._option_box_changed(0)

        self._file_dialog_factory(ui.inputFileBtn, ui.inputFile, QFileDialog.ExistingFile)
        self._file_dialog_factory(ui.outputDirBtn, ui.outputDir, QFileDialog.Directory)
        self._file_dialog_factory(ui.finalDirBtn, ui.finalDir, QFileDialog.Directory)
        self._file_dialog_factory(ui.bckFileBtn, ui.bckFile, QFileDialog.ExistingFile)
        self._file_dialog_factory(ui.malletDirBtn, ui.malletDir, QFileDialog.Directory)

    def _option_box_changed(self, index):
        text = self._form_ui.optionBox.currentText()

        is_keywords = text.lower() == "keywords"

        self._form_ui.bckFile.setEnabled(is_keywords)
        self._form_ui.bckFileBtn.setEnabled(is_keywords)

        self._form_ui.malletDir.setEnabled(not is_keywords)
        self._form_ui.malletDirBtn.setEnabled(not is_keywords)

    @staticmethod
    def _file_dialog_factory(btn, line, selection_type):
        def tmp():
            dialog = QFileDialog()
            dialog.setFileMode(selection_type)

            dialog.exec()
            selected = dialog.selectedFiles()[0]
            line.setText(selected)

        btn.clicked.connect(tmp)

    def _get_form_values(self):
        ui = self._form_ui

        args = dict()

        args["option"] = ui.optionBox.currentText()
        args["input_file"] = ui.inputFile.text()
        args["data_output_dir"] = ui.outputDir.text()
        args["final_output_dir"] = ui.finalDir.text()
        args["mallet_bin_dir"] = ui.malletDir.text()
        args["background_file"] = ui.bckFile.text()
        args["group_by"] = ui.groupBox.currentText()
        args["prefix"] = ui.prefix.text()

        args["tokenize"] = ui.tokenizeBox.isChecked()
        args["lemmatize"] = ui.lemmatizeBox.isChecked()
        args["nostopwords"] = ui.stopwordBox.isChecked()

        return args

    def _connect_run_ui(self):
        ui = self._run_ui
        ui.progressBar.hide()
        ui.progressBar.setMinimum(0)
        ui.progressBar.setMaximum(0)

        ui.runPreprocessor.clicked.connect(self._run_preprocessor)

    def _start(self):
        valid = self._validate_params(None)
        if not valid:
            return

        self._run_preprocessor()

    def _validate_params(self, args):
        valid = True

        # TODO: validate the form
        return valid

    def _run_preprocessor(self):

        values = self._get_form_values()
        if not self._validate_params(values):
            pass

        args = list()
        for name, value in values.items():
            if value:
                args.append("--" + name)
                if isinstance(value, str):
                    args.append(value.lower())

        args.append("--no_create_graphs")

        output_name = "banana.p"
        args.extend(["--objects_location", output_name])

        if os.name == 'nt':
            args = ["python.exe", "-u", "main.py"] + args
            # args = ["python.exe", "--version"]
            cwd = ".\\idea_relations"
        else:
            # args = ["python", "--version"]
            args = ["python", "-u", "main.py"] + args
            cwd = "./idea_relations"

        self._preprocessor_thread = threading.Thread(target=self._preprocessor_thread_runner, args=(args, cwd))

        self._run_ui.progressBar.show()
        self._preprocessor_thread.start()

        self._timer.timeout.connect(self._poll_queue)
        self._timer.start()

        self.output_name = os.path.join(cwd, output_name)

    def _preprocessor_thread_runner(self, args, cwd):
        output = subprocess.run(args, cwd=cwd)
        print("Done")

        self._message_queue.put(output.returncode)

    def _poll_queue(self):
        if not self._message_queue.empty():
            return_code = self._message_queue.get()
            print(return_code)

            self._preprocessor_done(return_code)

        else:
            self._timer.start()

    def _preprocessor_done(self, *args):
        self._run_ui.progressBar.setMaximum(1)
        self._run_ui.progressBar.setValue(1)

        if self._callback is not None:
            self._callback(*args)
