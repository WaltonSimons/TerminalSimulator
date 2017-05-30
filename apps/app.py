from abc import abstractmethod


class App(object):

    def __init__(self, terminal):
        self.terminal = terminal

    @staticmethod
    def get_command():
        return ''

    @staticmethod
    def get_description():
        return ''

    @abstractmethod
    def call(self, *args, **kwargs):
        return NotImplemented
