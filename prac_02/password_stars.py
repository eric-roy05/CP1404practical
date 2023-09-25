def main():
    password = get_password()
    hide_password(password)


def hide_password(password):
    print(len(password) * '*')


def get_password():
    password = input("Password (More that 7 characters): ")
    min_password_length = 7
    while len(password) < min_password_length:
        print("Invalid input")
        password = input("Password (More that 7 characters): ")
    return password


main()
