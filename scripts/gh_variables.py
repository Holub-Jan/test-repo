def main():
    from pathlib import Path
    import sys
    path_root = Path(__file__).parents[2]
    sys.path.append(str(path_root))
    from change_log_reader.change_log_reader import CHReader

    import os

    email = os.environ.get('USER_EMAIL')
    description = os.environ.get('DESCRIPTION')
    username = os.environ.get('USERNAME')
    test_var = os.environ.get('TEST_VAR')
    repo = os.environ.get('REPO')
    print(repo)
    print('Email: ', email)
    print('Description: ', description)
    print('Username: ', username)
    print('Test_var: ', test_var)
    chreader = CHReader(['CHANGELOG.md', 'RELEASE-NOTES.md'])

    ch_data = chreader.get_transcript()
    file_name = chreader.get_file_name()
    print(file_name)

    if not ch_data:
        description = 'Nasazení nové konfigurace aplikace'
    else:
        latest_version = ch_data[0]
        version = latest_version.version
        if latest_version.features and latest_version.bug_fixes:
            description = f'Přidání nových fukncí a opravení chyb s verzí {version}'
        elif not latest_version.features and latest_version.bug_fixes:
            description = f'Opravení chyb s verzí {version}'
        elif latest_version.features and not latest_version.bug_fixes:
            description = f'Přidání nových fukncí s verzí {version}'

    print(description)


if __name__ == '__main__':
    print('this here', sys.path)
    main()
