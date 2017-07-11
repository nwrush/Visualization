# Nikko Rush
# 6/21/2017

import functools
import math
import pickle

import matplotlib
matplotlib.use("TKAgg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import ttk

from data import Data
from MouseInteraction import MouseInteract
from TimeSeriesFrame import TimeSeriesFrame
from PMIPlot import PMIPlot
from ListFrame import ListFrame
from RelationTypeFrame import RelationTypeFrame
from TopRelations import TopRelations

def is_square_matrix(a):
    return a.shape[0] == a.shape[1]
    

def reverse_dict(input):
    output = dict()
    for key, value in input.items():
        if value in output:
            print("Warning: Duplicate key will be overwritten in new dictionary")
        output[value] = key
    return output

def pmi_vs_corr_plot(pmi, ts_correlation, axes, sample=None):
    num_ideas = pmi.shape[0]
    xs, ys = [], []
    for i in range(num_ideas):
        for j in range(i + 1, num_ideas):
            if np.isnan(pmi[i, j]) or np.isnan(ts_correlation[i, j]):
                continue
            if np.isinf(pmi[i, j]) or np.isinf(ts_correlation[i, j]):
                continue
            xs.append(ts_correlation[i, j])
            ys.append(pmi[i, j])

    if sample is None or not isinstance(sample, int):
        # Don't sample from the points
        plot_x = xs
        plot_y = ys
    else:
        # Do sample
        if sample < 0 or sample > len(xs):
            sample = num_ideas
        plot_x = np.random.choice(xs, sample, replace=False)
        plot_y = np.random.choice(ys, sample, replace=False)

    c = ["Pink"] * len(plot_x)

    plot = axes.scatter(plot_x, plot_y, color=c, picker=True)
    return (plot, (plot_x, plot_y))

def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return (int(row), int(col))

def get_index(n, i, j):
    """
    Does the reverse of get_row_col
    """
    return (n * (n - 1) / 2) - (n - i) * ((n - i) - 1) / 2 + j - i - 1

    
### Plot the Time Series for the given idea
def plot_idea_timeseries(idea_name, idea_numbers, ts_matrix):
    ts_data = ts_matrix[idea_numbers[idea_name]]

    start = 1980
    end = 2015

    plt.plot(ts_data)
    plt.show()

def show_time_series(idea_numbers, ts_matrix):
    # Get a list of idea names
    ideas = list(idea_numbers.keys())

    display_help()
    
    quit = False
    while not quit:
        selection = input(">")
        if selection in ideas:
            plot_idea_timeseries(selection, idea_numbers, ts_matrix)
        elif selection == "l":
            print(ideas)
        elif selection == "q":
            quit = True
        else:
            display_help()

def display_help():
    print("Enter an idea name to view the time series, l to list ideas, q to quit, or h to view this help message")

"""
First of the real Visualizations.
View the time series for the selected point in the PMI vs. TS Correlation plot
"""
def select_callback(event, axes, idea_ts, idea_names, correlation_matrix):
    index = event.ind[0]
    row, col = get_row_col(idea_ts.shape[0], index)
    
    axes.lines = []  # Clear the old lines from the plot
    
    x_values = [i for i in range(1980, 2015)]

    axes.plot(x_values, idea_ts[row])
    axes.plot(x_values, idea_ts[col])

    text_box_prop = {'pad':5, 'facecolor':"none"}
    tmp = axes.text(1.05, 0.5, "Correlation\n{0:.5f}".format(correlation_matrix[row][col]), transform=axes.transAxes, bbox=text_box_prop)
    legend = axes.legend([idea_names[row], idea_names[col]], loc='center left', bbox_to_anchor=(1, 0.7))

    axes.figure.canvas.draw()

def draw(pmi, ts_correlation, ts_matrix, idea_names):
    pmi_corr_fig = plt.figure()
    pmi_corr_axes = pmi_corr_fig.gca()
    pmi_corr_axes.set_title("PMI vs. Cooccurrence")
    pmi_corr_axes.set_xlabel("Prevalence Correlation")
    pmi_corr_axes.set_ylabel("Cooccurrence")
    pmi_corr_axes.set_xlim([-1.0, 1.0])

    ts_fig = plt.figure(2)
    ts_axes = ts_fig.gca()
    ts_axes.set_title("Time Series")
    ts_axes.set_xlabel("Year")
    ts_axes.set_ylabel("Frequency")

    ts_axes_box = ts_axes.get_position()
    ts_axes.set_position([ts_axes_box.x0, ts_axes_box.y0, ts_axes_box.width * 0.85, ts_axes_box.height])

    root = tk.Tk()

    def delete_window_callback():
        root.quit()

    pmi_corr_canvas = FigureCanvasTkAgg(pmi_corr_fig, master=root)
    pmi_corr_canvas.get_tk_widget().pack(side=tk.LEFT, expand=tk.YES)

    ts_canvas = FigureCanvasTkAgg(ts_fig, master=root)
    ts_canvas.get_tk_widget().pack(side=tk.LEFT, expand=tk.YES)

    pmi_plot, points = pmi_vs_corr_plot(pmi, ts_correlation, pmi_corr_axes, sample=1000)

    partial_select_callback = functools.partial(select_callback, axes=ts_axes, idea_ts=ts_matrix, idea_names=idea_names, correlation_matrix=ts_correlation)

    interaction = MouseInteract(pmi_corr_canvas, pmi_plot, partial_select_callback)

    root.protocol("WM_DELETE_WINDOW", delete_window_callback)
    tk.mainloop()
    print("Goodbye")

def gui(pmi_matrix, ts_correlation, ts_matrix, idea_names):
    idea_numbers = reverse_dict(idea_names)

    root = tk.Tk()

    def exit_callback():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", exit_callback)

    x_vals = [i for i in range(1980, 2015)]

    data_manager = Data(pmi_matrix, ts_correlation, ts_matrix, idea_names, x_vals)

    ts = TimeSeriesFrame(master=root, data=data_manager)
    pmi = PMIPlot(master=root, time_series_plot=ts, data=data_manager)

    idea_list = ListFrame(master=root)
    idea_list.add_items(idea_names.values())
    idea_list.update_width()

    relation_types = RelationTypeFrame(master=root, data=data_manager)

    top_relation_1 = TopRelations(master=root, data=data_manager, position={"row":1, "column":1}, topic_index=0)
    top_relation_1.set_idea_index(0)

    top_relation_2 = TopRelations(master=root, data=data_manager, position={"row":1, "column":2}, topic_index=1)
    top_relation_2.set_idea_index(10)

    pmi.add_select_listener(ts.plot_idea_indexes_event)
    pmi.add_select_listener(top_relation_1.set_idea_event)
    pmi.add_select_listener(top_relation_2.set_idea_event)

    idea_list.add_select_listener(pmi.filter_by_selected)
    relation_types.add_select_listener(pmi.filter_relation)
    relation_types.add_select_listener(ts.select_relation_type)

    pmi.plot(sample=1000)

    tk.mainloop()
    print("Boo")

def main():
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("keywords_data.p", 'rb'))
    assert is_square_matrix(pmi)
    assert is_square_matrix(ts_correlation)

    idea_numbers = reverse_dict(idea_names)
    """
    idea_names: maps the index of an idea/keyword to the text name of it
    idea_numbers: maps idea_name or keyword or whatever -> relevant index
    """
    ## pmi_vs_corr_plot(pmi, ts_correlation)
    #plot_idea_timeseries("web", idea_numbers, ts_matrix)
    #show_time_series(idea_numbers, ts_matrix)
    #draw(pmi, ts_correlation, ts_matrix, idea_names)
    gui(pmi, ts_correlation, ts_matrix, idea_names)

if __name__ == "__main__":
    main()
