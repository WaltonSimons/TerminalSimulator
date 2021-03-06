from apps.app import App
from files import Folder


class MkDir(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'mkdir'

    @staticmethod
    def get_description():
        return 'Make new directory.'

    def call(self, *args, **kwargs):
        new_dir = args[0]
        directory_exists = self.terminal.path.file_exists(new_dir)
        if not directory_exists:
            self.terminal.path.add_subfolder(Folder(new_dir))
        else:
            self.terminal.print('mkdir: cannot create directory ‘%s’: File exists' % new_dir)
