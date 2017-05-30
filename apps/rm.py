from apps.app import App
from files import Folder


class RM(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'rm'

    @staticmethod
    def get_description():
        return 'Removes directory or file.'

    def call(self, *args, **kwargs):
        remove_name = args[0]
        directory_exists = remove_name in [folder.name for folder in self.terminal.path.subfolders]
        if directory_exists:
            for sub in self.terminal.path.subfolders:
                if sub.name == remove_name:
                    self.terminal.path.remove_subfolder(sub)
        else:
            self.terminal.print('rm: cannot remove \'%s\': No such file or directory' % remove_name)
