from .app import App


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
        dir = args[0]

        if dir == '..':
            if self.console.path.parent is not None:
                self.console.path = self.console.path.parent
                return
        dirlist = [x for x in dir.split('/') if x]

        if len(dirlist) > 0:
            for sub in self.console.path.subfolders:
                if sub.name == dirlist[0]:
                    self.console.path = sub



