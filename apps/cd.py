from apps.app import App


class CD(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'cd'

    @staticmethod
    def get_description():
        return 'Changes current directory.'

    def call(self, *args, **kwargs):
        dir = args[0]

        if dir == '..':
            if self.terminal.path.parent is not None:
                self.terminal.path = self.terminal.path.parent
                return
        dirlist = [x for x in dir.split('/') if x]

        if len(dirlist) > 0:
            for sub in self.terminal.path.subfolders:
                if sub.name == dirlist[0]:
                    self.terminal.path = sub



