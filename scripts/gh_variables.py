def main():

    import os

    input_token = os.environ.get('INPUT_TOKEN')
    secret_token = os.environ.get('SECRET_TOKEN')

    print([input_token, secret_token])


if __name__ == '__main__':
    main()
