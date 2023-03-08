import os


class CustomConvert:
    def __init__(self):
        self._file_list = ['CHANGELOG.md', 'RELEASE-NOTES.md']

    def main(self):

        file_name = self._file_present()
        if not file_name:
            print('File "CHANGELOG.md" or "RELEASE-NOTES.md" not found!')
            return

        with open(os.path.abspath(os.getcwd())+file_name, 'r') as file:
            print('File path: ', os.path.abspath(os.getcwd())+file_name)
            for line in file.readlines():
                print(line)

    def _file_present(self):
        main_dir = os.listdir(os.getcwd())
        for file in self._file_list:
            if file in main_dir:
                return file
