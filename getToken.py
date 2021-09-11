def get_token():
    try:
        with open("personal-access-token.txt") as f:
            contents = f.read()

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


def main():
    if get_token():
        print("OK!")


if __name__ == "__main__":
    main()