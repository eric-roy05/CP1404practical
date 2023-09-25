def main():
    """Display menu, process input, and perform actions."""
    choice = open_menu()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid input")
        choice = open_menu()
    print("Farewell Bullfrog.")

def get_valid_score():
    """Prompt for and return a valid score (0-100 inclusive)."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def print_result(score):
    """Print the result based on the provided score."""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    """Print stars equal to the provided score."""
    print('*' * score)

def open_menu():
    """Display a menu and return user's choice (uppercase)."""
    print("(G)et a valid score (0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    return input(">>> ").upper()

main()
