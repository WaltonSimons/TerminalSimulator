class Quit(object):

    def __init__(self, console):
        self.console = console

    @staticmethod
    def get_command():
        return 'quit'

    @staticmethod
    def get_description():
        return 'Exits current terminal.'

    def call(self, args):
        self.console.running = False
