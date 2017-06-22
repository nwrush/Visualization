# Nikko Rush
# 6/21/2017

import matplotlib.pyplot as plt
import numpy as np
import pickle


def is_square_matrix(a):
    return a.shape[0] == a.shape[1]
    

def reverse_dict(input):
    output = dict()
    for key, value in input.items():
        if value in output:
            print("Warning: Duplicate key will be overwritten in new dictionary")
        output[value] = key
    return output

def pmi_vs_corr_plot(pmi, ts_correlation, sample=None):
    num_ideas = pmi.shape[0]
    xs, ys = [], []
    for i in range(num_ideas):
        for j in range(i + 1, num_ideas):
            if np.isnan(pmi[i, j]) or np.isnan(ts_correlation[i, j]):
                print("NaN")
                continue
            if np.isinf(pmi[i, j]) or np.isinf(ts_correlation[i, j]):
                print("Inf")
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
        
    plt.scatter(plot_x, plot_y)
    plt.show()

def plot_idea_timeseries(idea_name, idea_numbers, ts_matrix):
    ts_data = ts_matrix[idea_numbers[idea_name]]

    start = 1980
    end = 2015

    plt.plot(ts_data)
    plt.show()


def main():
    pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    assert is_square_matrix(pmi)
    assert is_square_matrix(ts_correlation)

    idea_numbers = reverse_dict(idea_names)
    """
    idea_names: maps the index of an idea/keyword to the text name of it
    idea_numbers: maps idea_name or keyword or whatever -> relevant index
    """
    # pmi_vs_corr_plot(pmi, ts_correlation)
    plot_idea_timeseries("web", idea_numbers, ts_matrix)

if __name__ == "__main__":
    main()
