from files import Folder
from terminal import Terminal


class Host(object):

    def __init__(self, user, name, password):
        self.name = name
        self.terminal = Terminal(user, self, Folder('home'))
        self.password = password
        self.network = None

    def connect(self):
        self.terminal.run()
