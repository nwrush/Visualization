# Nikko Rush
# 7/12/17

"""
Run the preprocessor (ask for arguments, etc.) and feed the output into the gui
"""

def main():
    import datetime
    print(datetime.datetime.now())
    import os
    import os.path
    import sys

    # Import matplotlib to ensure the backend it set to tk
    import matplotlib
    import tkinter
    matplotlib.use("TKAgg")

    from data_processor import main
    import Visualizer
    class Namespace:
        #def __getattr__(self, name):
        #    return None
        pass

    def read_config_file(fname):
        if not os.path.isfile(fname):
            print("Error: Couldn't find file {0}".format(fname))
            sys.exit(1)

        f = open(fname, 'r')

        args = []
        for line in f.readlines():
            line = line.strip()
            if line == '':
                continue

            name, value = line.split('=')

            args.append("--{0}".format(name))
            args.append(value)
        
        return args

    print(datetime.datetime.now())
    args = read_config_file("Keywords.config")

    print(datetime.datetime.now())
    #args = main.main(args, True)

    print(datetime.datetime.now())
    Visualizer.main("keywords_data.p")
