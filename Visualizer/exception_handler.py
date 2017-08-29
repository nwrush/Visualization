# Nikko Rush
# 8/3/2017

import logging
import sys
import traceback


def custom_handler(type, value, tback):
    logging.error(''.join(traceback.format_exception(type, value, tback)))

    sys.__excepthook__(type, value, traceback)

sys.excepthook = custom_handler
