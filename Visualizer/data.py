# Nikko Rush
# 7/10/2017

def reverse_dict(input):
    output = dict()
    for key, value in input.items():
        if value in output:
            print("Warning: Duplicate key will be overwritten in new dictionary")
        output[value] = key
    return output

class Data():

    def __init__(self, pmi_matrix, ts_correlation_matrix, ts_matrix, idea_names, x_vals):
        self.pmi = pmi_matrix
        self.ts_correlation = ts_correlation_matrix
        self.ts_matrix = ts_matrix
        self.idea_names = idea_names
        self.x_values = x_vals

        self.idea_numbers = reverse_dict(self.idea_names)
        self.num_ideas = len(self.idea_names)
