import apps


class Terminal(object):
    def __init__(self):
        self.running = True
        self.commands = {}
        self._prompt = '>'
        self.load_commands()

    def prompt(self):
        return self._prompt + ' '

    def load_commands(self):
        self.commands = dict(
            [(cls.get_command(), cls(self)) for name, cls in apps.__dict__.items() if isinstance(cls, type)])

    def run(self):
        while self.running:
            full_command = input(self.prompt())
            l = full_command.split()
            command, args = l[0], l[1:]
            if command in self.commands:
                self.commands[command].call(args)
            else:
                print('Unrecognized command %s.' % command)


terminal = Terminal()
terminal.run()
