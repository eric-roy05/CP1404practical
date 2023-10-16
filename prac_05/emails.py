"""
Emails
Estimate: 15 minutes
Actual:   30 minutes
"""


def main():
    """Store users' emails and names in a dictionary and print them out."""
    user_data = {}

    email = input("Email: ").strip()

    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation == '' or confirmation == 'y':
            user_data[email] = name
        else:
            name = input("Name: ").strip().title()
            user_data[email] = name

        email = input("Email: ").strip()

    print("\nName and Email:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from an email address."""
    username = email.split('@')[0]
    name_parts = username.split('.')
    return ' '.join(name_parts).title()


main()
