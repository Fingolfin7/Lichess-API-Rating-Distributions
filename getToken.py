def get_token():
    try:
        TOKEN_FILE = open('personal-access-token.txt')
        contents = TOKEN_FILE.read()
        TOKEN_FILE.close()

        if contents == '':
            print('Empty file. Please fill it in with a Lichess Personal Access Token.')
            return None

        return contents

    except Exception as e:
        print('Error:')
        print(e)
        print('----------------')
        print('An error has occurred, make sure you created "personal-access-token.txt".')
        return None
