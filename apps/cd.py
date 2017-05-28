from apps.app import App


class CD(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'cd'

    @staticmethod
    def get_description():
        return 'Changes current directory.'

    def call(self, args):
        current_path = self.console._path[1:]
        if args[0] == '..':
            self.console._path = '/' + '/'.join(current_path.split('/')[:-1])
        else:
            self.console._path = '/' + '/'.join(filter(bool, args[0].split('/')))
