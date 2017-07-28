# Nikko Rush
# 7/18/17

import os
import os.path
from pathlib import Path
import queue
import subprocess
import threading

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

from frames.VisualizerFrame import VisualizerFrame

class InputField():

    def __init__(self, master, name, row, label_text=None, variable_fmt=None):
        self.frame = master

        self.name = name

        label_text = name if label_text is None else label_text
        self.label = tk.Label(self.frame, text=label_text)
        self.label.grid(row=row, column=0, sticky="W", pady=2)

        self._var = None
        self.data_field = None

        self.button = None

        self.variable_callback = variable_fmt

    def get_value(self):
        if self.variable_callback is None or not self._var.get():
            return self._var.get()
        else:
            return self.variable_callback(self._var.get())


def create_option_menu(field, options, row):
    var = field._var = tk.StringVar()
    field.data_field = tk.OptionMenu(field.frame, var, *options, command=None)
    field.data_field.grid(row=row, column=1)
    field._var.set(options[0])


def create_entry(field, row):
    var = field._var = tk.StringVar()
    field.data_field = tk.Entry(field.frame, textvariable=var, width=50)
    field.data_field.grid(row=row, column=1)


def create_checkbox(field, row):
    var = field._var = tk.IntVar()
    field.data_field = tk.Checkbutton(field.frame, var=var)
    field.data_field.grid(row=row, column=1)


def create_button(field, row, callback):
    button = tk.Button(master=field.frame, text="...", command=callback)
    button.grid(row=row, column=2, padx=5)
    field.button = button


def get_file_factory(field):
    def callback():
        value = filedialog.askopenfilename(parent=field.frame)
        if value is not None:
            field._var.set(value)

    return callback


def get_directory_factory(field):
    def callback():
        value = filedialog.askdirectory(parent=field.frame)
        if value is not None:
            field._var.set(value)

    return callback


def format_path(value):
    return str(Path(value))


class PreprocessorController(VisualizerFrame):

    def __init__(self, master, finished_callback=None):
        super(PreprocessorController, self).__init__(master=master)

        self.pack_frame()

        self.basic_options = ttk.LabelFrame(master=self.frame, text="Options")
        self.basic_options.pack(side=tk.TOP)

        self.adv_options = ttk.LabelFrame(master=self.frame, text="Advanced")
        self.adv_options.pack(side=tk.TOP, fill=tk.X, expand=1)
        
        self.status_field = ttk.LabelFrame(master=self.frame, text="Status")
        self.status_field.pack(side=tk.TOP, fill=tk.X, expand=1)

        self._options = dict()
        self._flags = dict()
        self._create_options()
        self._create_status()

        self._preprocessor_thread = None
        self._message_queue = queue.Queue()
        self._callback = finished_callback

        self.output_name = None

    def _create_options(self):
        row = 0

        run_type = InputField(self.basic_options, "option", row, label_text="Option: ")
        create_option_menu(run_type, ["keywords", "topics"], row)
        self._options["option"] = run_type
        row += 1

        input_file = InputField(self.basic_options, "input_file", row, label_text="Input File:")
        create_entry(input_file, row)
        create_button(input_file, row, get_file_factory(input_file))
        self._options["input_file"] = input_file
        row += 1

        data_output_dir = InputField(self.basic_options, "data_output_dir", row, label_text="Output Directory:",
                                     variable_fmt=format_path)
        create_entry(data_output_dir, row)
        create_button(data_output_dir, row, get_directory_factory(data_output_dir))
        self._options["data_output_dir"] = data_output_dir
        row += 1

        final_output_dir = InputField(self.basic_options, "final_output_dir", row, label_text="Final Output Directory:",
                                      variable_fmt=format_path)
        create_entry(final_output_dir, row)
        create_button(final_output_dir, row, get_directory_factory(final_output_dir))
        self._options["final_output_dir"] = final_output_dir
        row += 1

        background_file = InputField(self.basic_options, "background_file", row, label_text="Background File:")
        create_entry(background_file, row)
        create_button(background_file, row, get_file_factory(background_file))
        self._options["background_file"] = background_file
        row += 1

        mallet_bin_dir = InputField(self.basic_options, "mallet_bin_dir", row, label_text="Mallet Bin Directory:")
        create_entry(mallet_bin_dir, row)
        create_button(mallet_bin_dir, row, get_directory_factory(mallet_bin_dir))
        self._options["mallet_bin_dir"] = mallet_bin_dir
        row += 1

        group_by = InputField(self.basic_options, "group_by", row, label_text="Group By:")
        create_option_menu(group_by, ["year", "quarter", "month"], row)
        self._options["group_by"] = group_by
        row += 1

        prefix = InputField(self.basic_options, "prefix", row, label_text="Prefix:")
        create_entry(prefix, row)
        self._options["prefix"] = prefix
        row += 1

        num_ideas = InputField(self.basic_options, "num_ideas", row, label_text="Number of Ideas:")
        create_entry(num_ideas, row)
        self._options["num_ideas"] = num_ideas
        row += 1

        tokenize = InputField(self.adv_options, "tokenize", row, label_text="Tokenize: ")
        create_checkbox(tokenize, row)
        self._flags["tokenize"] = tokenize
        row += 1

        lemmatize = InputField(self.adv_options, "lemmatize", row, label_text="Lemmatize: ")
        create_checkbox(lemmatize, row)
        self._flags["lemmatize"] = lemmatize
        row += 1

        nostop = InputField(self.adv_options, "nostopwords", row, label_text="No Stop Words: ")
        create_checkbox(nostop, row)
        self._flags["nostopwords"] = nostop
        row += 1

        def toggle_fields(*args):
            value = run_type._var.get()
            if value == "keywords":
                mallet_bin_dir.data_field['state'] = tk.DISABLED
                background_file.data_field['state'] = tk.NORMAL
            elif value == "topics":
                mallet_bin_dir.data_field['state'] = tk.NORMAL
                background_file.data_field['state'] = tk.DISABLED

        run_type._var.trace('w', toggle_fields)
        toggle_fields()

    def _create_status(self):
        self.run = tk.Button(master=self.status_field, text="Run Preprocessor", command=self._start)
        self.run.pack(side=tk.TOP, pady=(0, 2))

        self.progress = ttk.Progressbar(master=self.status_field, mode="indeterminate")
        self.progress.pack(side=tk.LEFT, expand=1, fill=tk.X)
        self.progress.pack_forget()

    def _start(self):
        valid = self._validate_params()
        if not valid:
            return

        self._run_preprocessor()

    def _validate_params(self):
        valid = True

        # TODO: validate the form
        return valid

    def _run_preprocessor(self):
        args = list()
        for name, field in self._options.items():
            if field.get_value():
                args.append("--" + name)
                args.append(field.get_value())

        for name, field in self._flags.items():
            if field.get_value():
                args.append("--"+name)

        args.append("--no_create_graphs")

        output_name = "banana.p"
        args.extend(["--objects_location", output_name])

        if os.name == 'nt':
            args = [".\\venv\\Scripts\\python.exe", "-u", "main.py"] + args
            cwd = ".\\idea_relations"
        else:
            # args = ["python", "--version"]
            args = ["python", "-u", "main.py"] + args
            cwd = "./idea_relations"

        self._preprocessor_thread = threading.Thread(target=self._preprocessor_thread_runner, args=(args, cwd))
        self._preprocessor_thread.start()
        self.frame.after(500, self._poll_queue)

        self.output_name = os.path.join(cwd, output_name)

    def _preprocessor_thread_runner(self, args, cwd):
        self.progress.pack()
        self.progress.start()

        output = subprocess.run(args, cwd=cwd)

        self._message_queue.put(output.returncode)
        self.progress.stop()

    def _poll_queue(self):
        if not self._message_queue.empty():
            return_code = self._message_queue.get()
            print(return_code)
            
            if self._callback is not None:
                self._callback(self, return_code)
        else:
            self.frame.after(500, func=self._poll_queue)
