import random


def main():
    user_score = get_valid_score()
    user_result = calculate_result(user_score)

    print(f"User's result: {user_result}")

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)

    print(f"Random score: {random_score}")
    print(f"Random result: {random_result}")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def calculate_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
