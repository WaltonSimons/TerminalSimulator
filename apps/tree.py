from apps.app import App
from files import Folder, File


class Tree(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'tree'

    @staticmethod
    def get_description():
        return 'Shows current directory as a tree.'

    def call(self, args):
        self.terminal.path.list_directory()
