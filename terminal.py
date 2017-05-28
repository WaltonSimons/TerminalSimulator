import apps


class Terminal(object):
    def __init__(self, user, host):
        self.running = True
        self.commands = {}
        self.user = user
        self.host = host

        self._path = '/'
        self._prompt = '>'
        self.load_commands()

    def path(self):
        return self._path

    def prompt(self):
        return '%s@%s %s %s ' % (self.user, self.host, self.path(), self._prompt)

    def load_commands(self):
        self.commands = dict(
            [(cls.get_command(), cls(self)) for name, cls in apps.__dict__.items() if isinstance(cls, type)])

    def run(self):
        while self.running:
            full_command = input(self.prompt())
            l = full_command.split()
            if len(l) > 0:
                command, args = l[0], l[1:]
                if command in self.commands:
                    self.commands[command].call(args)
                else:
                    print('Unrecognized command %s.' % command)

