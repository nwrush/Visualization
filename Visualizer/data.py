# Nikko Rush
# 7/10/2017

# Last update 9/4/17

import os
import os.path
import pickle

import numpy as np


def reverse_dict(input_dict):
    output = dict()
    for key, value in input_dict.items():
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


class Data:
    def __init__(self, args, pmi_matrix, ts_correlation_matrix, ts_matrix, idea_names, x_vals,
                 name="Visualization"):

        self._args = args
        self._is_keywords = args.option.upper() == "KEYWORDS"
        self.pmi = pmi_matrix
        self.ts_correlation = ts_correlation_matrix
        self.ts_matrix = ts_matrix
        self.idea_names = idea_names  # Goes from indexes to text
        self.x_values = x_vals

        self.idea_numbers = reverse_dict(self.idea_names)  # Goes from text to indexes
        self.num_ideas = len(self.idea_names)

        self.strength_matrix = self._get_strength_matrix()

        self.relation_types = ("Friends", "Tryst", "Head-To-Head", "Arms-Race")  # Layout the relation in quadrant order

        self.name = name if name is not None else "Visualization"

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

    TOPIC_DISPLAY_WIDTH = 3

    def get_display_idea_names(self, indexes):
        if self._is_keywords:
            return self.get_idea_names(indexes)

        if isinstance(indexes, int):
            full_name = self.idea_names[indexes]
            return ','.join(full_name.split(',')[:self.TOPIC_DISPLAY_WIDTH]) + '...'

        try:
            names = list()
            first = True
            for index in indexes:
                full_name = self.idea_names[index]
                short_name = ','.join(full_name.split(',')[:self.TOPIC_DISPLAY_WIDTH]) + '...'
                names.append(short_name)
            return names
        except TypeError as err:
            print(err)
        return None
