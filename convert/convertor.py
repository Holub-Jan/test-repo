import os
import sys
from pydantic import BaseModel


class Version(BaseModel):
    version: str
    features: bool
    bug_fixes: bool


class CustomConvert:
    def __init__(self):
        self._file_list = ['CHANGELOG.md', 'RELEASE-NOTES.md']

    def get_transcript(self):
        file_name = self._file_present()
        if not file_name:
            print('File "CHANGELOG.md" or "RELEASE-NOTES.md" not found!')
            return None

        with open(os.path.abspath(os.getcwd())+'/'+file_name, 'r') as file:
            versions = self._save_logic(file)

        return versions

    def _save_logic(self, file):
        version = None
        features = False
        bugs = False
        versions = list()

        for line in file.readlines():
            line = line.strip('\n')
            line_cat = self._line_cat(line)

            if line_cat == 'version':
                if version is not None:
                    block = Version(version=version, features=features, bug_fixes=bugs)
                    versions.append(block)
                    features = False
                    bugs = False
                version = line[3:]
            elif line_cat == 'features':
                features = True
            elif line_cat == 'bugs':
                bugs = True

        block = Version(version=version, features=features, bug_fixes=bugs)
        versions.append(block)
        return versions

    def _file_present(self):
        main_dir = os.listdir(os.getcwd())
        for file in self._file_list:
            if file in main_dir:
                return file

    @staticmethod
    def _line_cat(line: str):
        if len(line) > 0 and line[:2] != '* ':
            if line[:3] == '## ':
                return 'version'
            elif line[:4] == '### ':
                if line[4:] == 'Features':
                    return 'features'
                elif line[4:] == 'Bug Fixes':
                    return 'bugs'


if __name__ == "__main__":
    pass
