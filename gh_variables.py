def main():
    import os

    email = os.environ.get('USER_EMAIL')
    description = os.environ.get('DESCRIPTION')
    username = os.environ.get('USERNAME')

    print('Email: ', email)
    print('Description: ', description)
    print('Username: ', username)


if __name__ == '__main__':
    main()
