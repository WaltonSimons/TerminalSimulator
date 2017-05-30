from apps.app import App
from files import File


class CF(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'cf'

    @staticmethod
    def get_description():
        return 'Create new file.'

    def call(self, *args, **kwargs):
        args = args[0].split()
        if len(args) <= 1:
            self.terminal.print('cf: please specify file format')
            return
        file_name = args[0]
        file_format = args[1]
        file_exists = self.terminal.path.file_exists(file_name)
        if not file_exists:
            self.terminal.path.add_file(File(file_name, file_format, self.terminal.path))
        else:
            self.terminal.print('cf: cannot create directory ‘%s’: File exists' % file_name)
