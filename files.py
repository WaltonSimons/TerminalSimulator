

class Folder(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

        self.subfolders = []

    def add_subfolder(self, sub):
        sub.parent = self
        self.subfolders.append(sub)

    def list_directory(self, indent=0):
        print('    '*indent + '/' + self.name)
        for sub in self.subfolders:
            sub.list_directory(indent + 1)

    def __str__(self):
        this = '/%s' % self.name
        return self.parent.__str__() + this if self.parent else this