import apps
from files import Folder
from colorama import Fore, Back, Style

Fore.BOLD = '\033[1m'


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
        return (Fore.BOLD + Fore.GREEN + '%s@%s' + Fore.BLUE + ' %s' + Style.RESET_ALL + ' %s ') % (
        self.user, self.host.name, self.path_string(), self._prompt)

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
                    self.commands[command].call(self.get_args_and_kwargs(args[0] if args else ''))
                else:
                    self.print('Unrecognized command %s.' % command)

    def print(self, msg):
        print(msg)

    @staticmethod
    def get_args_and_kwargs(string):
        l = string.split()
        kwargs = dict()
        args = []
        for arg in l:
            if arg[0] == '-':
                argval = arg[1:].split('=')
                if len(argval) > 1:
                    kwarg, value = arg[1:].split('=')
                    kwargs[kwarg] = value
                else:
                    kwargs[argval[0]] = True
            else:
                args.append(arg)
        return args, kwargs
