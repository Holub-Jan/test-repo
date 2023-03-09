def main():
    import os
    from convert.convertor import CustomConvert

    email = os.environ.get('USER_EMAIL')
    description = os.environ.get('DESCRIPTION')
    username = os.environ.get('USERNAME')
    test_var = os.environ.get('TEST_VAR')

    print('Email: ', email)
    print('Description: ', description)
    print('Username: ', username)
    print('Test_var: ', test_var)

    cs = CustomConvert()

    cs.main()


if __name__ == '__main__':
    main()
