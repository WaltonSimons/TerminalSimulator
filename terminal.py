import apps
from files import Folder


class Terminal(object):
    def __init__(self, user, host, path=Folder('home')):
        self.running = True
        self.commands = {}
        self.user = user
        self.host = host
        self.path = path

        self._prompt = '>'
        self.load_commands()

    def path_string(self):
        return str(self.path)

    def prompt(self):
        return '%s@%s %s %s ' % (self.user, self.host, self.path_string(), self._prompt)

    def load_commands(self):
        self.commands = dict(
            [(cls.get_command(), cls(self)) for name, cls in apps.__dict__.items() if
             isinstance(cls, type) and issubclass(cls, apps.App) and cls.__name__ is not 'App'])

    def run(self):
        while self.running:
            full_command = input(self.prompt())
            l = full_command.split(' ', 1)
            if len(l) > 0:
                command, args = l[0], l[1:]
                if command in self.commands:
                    self.commands[command].call(args)
                else:
                    print('Unrecognized command %s.' % command)
