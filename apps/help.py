from apps.app import App


class Help(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'help'

    @staticmethod
    def get_description():
        return 'Shows this list.'

    def call(self, *args, **kwargs):
        for command, cls in self.terminal.commands.items():
            self.terminal.print(command + ' - ' + cls.get_description())
