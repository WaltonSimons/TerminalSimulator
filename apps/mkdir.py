from apps.app import App


class MkDir(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'mkdir'

    @staticmethod
    def get_description():
        return 'Make new directory.'

    def call(self, args):
        from files import Folder
        new_dir = args[0]
        directory_exists = new_dir in [folder.name for folder in self.console.path.subfolders]
        if not directory_exists:
            self.console.path.add_subfolder(Folder(new_dir))
        else:
            print('mkdir: cannot create directory ‘%s’: File exists' % new_dir)
