# Nikko Rush
# 7/10/2017

import os.path
import pickle

import numpy as np

def reverse_dict(input):
    output = dict()
    for key, value in input.items():
        if value in output:
            print("Warning: Duplicate key will be overwritten in new dictionary")
        output[value] = key
    return output

def is_square(a):
    row, col = a.shape
    return row == col

def load_data(fname):
    if not os.path.isfile(fname):
        print("Data file {0} doesn't exist".format(fname))
        return None

    return pickle.load(open(fname, 'rb'))

class Data():

    def __init__(self, pmi_matrix=None, ts_correlation_matrix=None, ts_matrix=None, idea_names=None, x_vals=None):
        self.pmi = pmi_matrix
        self.ts_correlation = ts_correlation_matrix
        self.ts_matrix = ts_matrix
        self.idea_names = idea_names
        self.x_values = x_vals

        self.idea_numbers = reverse_dict(self.idea_names)
        self.num_ideas = len(self.idea_names)

        self.strength_matrix = self._get_strength_matrix()

        self.relation_types = ("Friends", "Tryst", "Head-To-Head", "Arms-Race") # Layout the relation in quadrant order
        pass

    def _get_strength_matrix(self):
        assert self.pmi.shape == self.ts_correlation.shape
        assert is_square(self.pmi)

        a = np.multiply(self.pmi, self.ts_correlation)

        lower_indexes = np.tril_indices(self.pmi.shape[0])
        a[lower_indexes] = np.nan
        return a

    def get_idea_names(self, indexes):
        if isinstance(indexes, int):
            return self.idea_names[indexes]

        try:
            names = list()
            for index in indexes:
                names.append(self.idea_names[index])
            return names
        except TypeError as err:
            print(err)

        return None
