from abc import abstractmethod


class App(object):

    def __init__(self, console):
        self.console = console

    @staticmethod
    def get_command():
        return ''

    @staticmethod
    def get_description():
        return ''

    @abstractmethod
    def call(self, args):
        return NotImplemented
