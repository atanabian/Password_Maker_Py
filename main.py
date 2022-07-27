import random


class Errors(Exception):
    pass


class PasswordLenLow(Errors):
    pass


def Password_Maker(password_len: int):
    try:

        if password_len <= 4:
            raise PasswordLenLow

        password_Symbols = ['?', ')', '(', '-', '_', '2', '3', '4', '5', '6', '7', '8',
                            '9', '0', '!', '@', '#', '$', '%', '^', '&', '.', '*']
        password = ''
        random.shuffle(password_Symbols)

        for i in range(password_len):

            password = password + password_Symbols[i]

        return password

    except TypeError as Error:
        print(Error)

    except PasswordLenLow:
        print("You can't have a password with 5 or shorter digit")


print(Password_Maker(3))
