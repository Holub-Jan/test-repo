import os


class CustomConvert:
    def __init__(self):
        self._file_list = ['CHANGELOG.md', 'RELEASE-NOTES.md']

    def main(self):
        print('curr path stuff', os.listdir(os.getcwd()))

        print('curr path: ', os.path.abspath(os.getcwd()))
