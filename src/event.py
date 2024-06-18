from typing import Callable

class Event:
    def __init__(self, callback: Callable, args: list = None):
        self.callback = callback
        if args:    
            self.args = args
        else:
            self.args = []

    def add_args(self, args: list):
        self.args.append(args)

    def call(self, *args):
        c_cargs = self.args + list(args)
        self.callback(*c_cargs)