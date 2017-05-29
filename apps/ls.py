from apps.app import App


class LS(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'ls'

    @staticmethod
    def get_description():
        return 'Lists subfolders and files.'

    def call(self, args):
        self.terminal.print('   '.join([f.name for f in self.terminal.path.subfolders]))
