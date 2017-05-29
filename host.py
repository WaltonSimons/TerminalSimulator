from files import Folder
from terminal import Terminal


class Host(object):

    def __init__(self, user, name, password, folder = Folder('home')):
        self.name = name
        self.main_folder = folder
        self.terminal = Terminal(user, self, self.main_folder)
        self.password = password
        self.network = None

    def connect(self):
        self.terminal.run()
