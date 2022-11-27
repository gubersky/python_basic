import string


def decorator(func):
    def wrapper(*args, **kwargs):
        while True:
            print("Password must contains minimum 1 number, letter, special character and length at least 8 characters")
            password = func(*args, **kwargs)
            if password is None:
                print("Wrong data: spaces and tabs are not accepted for the password!\n")
            elif len([i for i in password if i.isdigit()]) == 0:
                print("Password must contains minimum 1 number\n")
            elif len([i for i in password if i.isalpha()]) == 0:
                print("Password must contains minimum 1 letter\n")
            elif not any([1 if i in string.punctuation else 0 for i in password]):
                print("Password must contains minimum 1 special character\n")
            elif len(password) < 8:
                print("Password length must contains at least 8 characters\n")
            else:
                print("Password accepted:", password)
                break
            return func

    return wrapper


@decorator
def user_password():
    password = input("Please enter the password: ")
    if len(password) == 0 or password.count("\t") or password.count(" "):
        return None
    else:
        return password


if __name__ == '__main__':
    user_password()
