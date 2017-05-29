from apps.app import App


class SSH(App):

    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'ssh'

    @staticmethod
    def get_description():
        return 'Connects to another host.'

    def call(self, args):
        user, hostname = args[0].split('@')
        host = self.terminal.host.network.get_host(hostname)
        if host is not None:
            if host.terminal.user == user:
                password = input('%s@%s password:' % (user, hostname))
                if password == host.password:
                    host.connect()
                else:
                    self.terminal.print('Invalid password.')
            else:
                self.terminal.print('No such user.')
        else:
            self.terminal.print('ssh: Could not resolve hostname %s: Name or service not known' % hostname)
