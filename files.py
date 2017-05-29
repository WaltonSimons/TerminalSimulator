

class Folder(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

        self.subfolders = []
        self.files = []

    def add_subfolder(self, sub):
        sub.parent = self
        self.subfolders.append(sub)

    def remove_subfolder(self, sub):
        self.subfolders.remove(sub)

    def add_file(self, file):
        file.parent = self
        self.files.append(file)

    def remove_file(self, file):
        self.files.remove(file)

    def list_directory(self, indent=0):
        print('    '*indent + '/' + self.name)
        for sub in self.subfolders:
            sub.list_directory(indent + 1)
        for file in self.files:
            print('    '*(indent + 1) + '/' + file.name)

    def file_exists(self, name):
        return name in [sub.name for sub in self.subfolders] + [file.name for file in self.files]

    def __str__(self):
        this = '/%s' % self.name
        return self.parent.__str__() + this if self.parent else this


class File(object):

    def __init__(self, name, file_format, parent=None):
        self.name = name
        self.file_format = file_format
        self.parent = parent
