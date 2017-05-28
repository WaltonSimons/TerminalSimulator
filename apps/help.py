from .app import App


class Help(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'help'

    @staticmethod
    def get_description():
        return 'Shows this list.'

    def call(self, args):
        for command, cls in self.console.commands.items():
            print(command + ' - ' + cls.get_description())
