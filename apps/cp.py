from apps.app import App
from files import File


class CP(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'cp'

    @staticmethod
    def get_description():
        return 'Copy file.'

    def call(self, *args, **kwargs):
        if len(args) <= 1:
            self.terminal.print('cp: missing destination file operand')
            return
        source = args[0]
        destination = args[1]

        file = self.terminal.path.get_file_by_path(source)

        folder = self.terminal.path.get_folder_by_path(destination)

        if file is not None:
            if folder is not None:
                if folder.add_file(file):
                    return
                else:
                    self.terminal.print('cp: file %s already exists' % file.name)
            else:
                self.terminal.print('cp: destination doesn\'t exist')
        else:
            self.terminal.print('cp: source file doesn\'t exist')