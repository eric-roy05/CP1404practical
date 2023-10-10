import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6


def generate_quick_pick():
    """Generate a single quick pick."""
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK))


def display_quick_picks(num_quick_picks):
    """Display the specified number of quick picks."""
    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2}".format(number) for number in quick_pick))


def main():
    num_quick_picks = int(input("How many quick picks? "))
    display_quick_picks(num_quick_picks)


main()
