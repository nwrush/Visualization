# Nikko Rush
# 7/10/2017

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

class Data():

    def __init__(self, pmi_matrix, ts_correlation_matrix, ts_matrix, idea_names, x_vals):
        self.pmi = pmi_matrix
        self.ts_correlation = ts_correlation_matrix
        self.ts_matrix = ts_matrix
        self.idea_names = idea_names
        self.x_values = x_vals

        self.idea_numbers = reverse_dict(self.idea_names)
        self.num_ideas = len(self.idea_names)

        self.strength_matrix = self._get_strength_matrix()
        pass

    def _get_strength_matrix(self):
        assert self.pmi.shape == self.ts_correlation.shape
        assert is_square(self.pmi)

        a = np.multiply(self.pmi, self.ts_correlation)

        lower_indexes = np.tril_indices(self.pmi.shape[0])
        a[lower_indexes] = np.nan
        return a