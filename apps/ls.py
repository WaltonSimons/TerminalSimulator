from .app import App


class LS(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'ls'

    @staticmethod
    def get_description():
        return 'Lists subfolders and files.'

    def call(self, args):
        print('   '.join([f.name for f in self.console.path.subfolders]))
