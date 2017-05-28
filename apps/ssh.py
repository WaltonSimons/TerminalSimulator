from apps.app import App


class SSH(App):

    def __init__(self, console):
        super().__init__(console)

    @staticmethod
    def get_command():
        return 'ssh'

    @staticmethod
    def get_description():
        return 'Connects to another host.'

    def call(self, args):
        user, hostname = args[0].split('@')
        host = self.console.host.network.get_host(hostname)
        if host is not None:
            if host.terminal.user == user:
                password = input('%s@%s password:' % (user, hostname))
                if password == host.password:
                    host.connect()
                else:
                    print('Invalid password.')
            else:
                print('No such user.')
        else:
            print('ssh: Could not resolve hostname %s: Name or service not known' % hostname)
