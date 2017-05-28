from abc import abstractmethod


class App(object):

    def __init__(self, console):
        self.console = console

    @staticmethod
    def get_command():
        return 'cd'

    @staticmethod
    def get_description():
        return 'Changes current directory.'

    def call(self, args):
        current_path = self.console._terminal_prefix[1:]
        if args[0] == '..':
            self.console._terminal_prefix = '>' + '/'.join(current_path.split('/')[:-1])
        else:
            self.console._terminal_prefix = '>' + args[0]
