from apps.app import App
from files import Folder


class RM(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'rm'

    @staticmethod
    def get_description():
        return 'Removes directory or file.'

    def call(self, args):
        remove_name = args[0]
        directory_exists = remove_name in [folder.name for folder in self.console.path.subfolders]
        if directory_exists:
            for sub in self.console.path.subfolders:
                if sub.name == remove_name:
                    self.console.path.remove_subfolder(sub)
        else:
            print('rm: cannot remove \'%s\': No such file or directory' % remove_name)
