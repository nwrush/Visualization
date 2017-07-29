# Nikko Rush
# 7/28/2017

class Listener(object):
    
    def __init__(self, *handlers):
        self._handlers = set(handlers)

    def add_handler(self, func):
        self._handlers.add(func)

    def has_handler(self, func):
        return func in self._handlers

    def remove_handler(self, func):
        self._handlers.discard(func)

    add = add_handler
    remove = remove_handler

    def invoke_empty(self):
        for func in self._handlers:
            func()

    def invoke(self, event):
        for func in self._handlers:
            code = func.__code__
            if code.co_argcount == 0:
                func()
            elif code.co_argcount == 1 and code.co_varnames == ('self',):
                func()
            else:
                func(event)
