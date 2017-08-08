# Nikko Rush
# 8/3/2017

import sys
import traceback

def custom_handler(type, value, tback):
    # print(type,file=sys.stderr)
    # print(value, file=sys.stderr)
    # print(tback, file=sys.stderr)
    print("banana")
    traceback.print_exception(type, value, tback)

    sys.__excepthook__(type, value, traceback)

sys.excepthook = custom_handler