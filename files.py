

class Folder(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

        self.subfolders = []
        self.files = []

    def add_subfolder(self, sub):
        if not self.file_exists(sub.name):
            sub.parent = self
            self.subfolders.append(sub)
            return True
        return False

    def remove_subfolder(self, sub):
        self.subfolders.remove(sub)

    def add_file(self, file):
        if not self.file_exists(file.name):
            file.parent = self
            self.files.append(file)
            return True
        return False

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

    def get_subfolder(self, name):
        if name == '..':
            return self.parent if self.parent is not None else self
        for subfolder in self.subfolders:
            if subfolder.name == name:
                return subfolder
        return None

    def get_file(self, name):
        for file in self.files:
            if file.name == name:
                return file
        return None

    @staticmethod
    def get_root_folder(folder):
        return folder.get_root_folder(folder.parent) if folder.parent is not None else folder

    def get_folder_by_path(self, path):
        from_root = path[0] == '/'
        current_folder = self.get_root_folder(self) if from_root else self
        path = path.split('/')

        if from_root:
            path = path[2:]

        for name in path:
            if current_folder:
                current_folder = current_folder.get_subfolder(name)
            else:
                return False
        return current_folder

    def get_file_by_path(self, path):
        not_local = len(path.rsplit('/', 1)) > 1
        if not_local:
            path, file_name = path.rsplit('/', 1)
            folder = self.get_folder_by_path(path)
        else:
            file_name = path
            folder = self
        return folder.get_file(file_name) if folder is not None else None

    def __str__(self):
        this = '/%s' % self.name
        return self.parent.__str__() + this if self.parent else this


class File(object):

    def __init__(self, name, file_format, parent=None):
        self.name = name
        self.file_format = file_format
        self.parent = parent
