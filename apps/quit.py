from apps.app import App


class Quit(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'disconnect'

    @staticmethod
    def get_description():
        return 'Disconnects from terminal.'

    def call(self, args):
        self.terminal.running = False
