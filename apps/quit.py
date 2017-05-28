from apps.app import App


class Quit(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'quit'

    @staticmethod
    def get_description():
        return 'Exits current terminal.'

    def call(self, args):
        self.console.running = False
