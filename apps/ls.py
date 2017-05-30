from apps.app import App
from colorama import Fore, Back, Style


class LS(App):
    def __init__(self, terminal):
        super().__init__(terminal)

    @staticmethod
    def get_command():
        return 'ls'

    @staticmethod
    def get_description():
        return 'Lists subfolders and files.'

    def call(self, *args, **kwargs):
        self.terminal.print(
            Fore.BLUE +
            '    '.join(
                [(
                    '    '.join([f.name for f in self.terminal.path.subfolders])
                 + Style.RESET_ALL
                ),
                (
                    '    '.join([f.name for f in self.terminal.path.files])
                )]
            )
        )