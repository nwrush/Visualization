# Nikko Rush
# 7/17/17

import json
import os.path

FILENAME="./layout.json"


def load_layouts(fname=FILENAME):
    if not os.path.isfile(fname):
        print("Layout file doesn't exist")

    return json.load(open(fname, 'r'))

def create_layout():
    layouts = dict()
    more_frames = True
    while more_frames:
        frame_name = input(">Frame name: ")

        print("Enter parameters or STOP to stop")

        params = dict()
        while True:
            name = input(">Name: ")
            value = input(">Value: ")
            if name == "STOP" or value == "STOP":
                break
            params[name] = value

        layouts[frame_name] = params
        
        should_stop = input("Type QUIT to stop or anything else to continue: ")
        if should_stop == "QUIT":
            break

    file_name = input("Filename to save layout to (default is: {0}): ".format(FILENAME))
    if file_name == "":
        file_name = FILENAME
    json.dump(layouts, open(file_name, 'w'), indent=4)

if __name__ == "__main__":
    create_layout()
