# Nikko Rush
# 7/11/17

import matplotlib.pyplot as plt

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