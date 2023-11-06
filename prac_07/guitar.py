import csv
class Guitar:
    def __init__(self, name, year, cost):
        """Initialize a Guitar instance."""
        self.name, self.year, self.cost = name, year, cost

    def get_age(self, current_year):
        """Calculate age of guitar."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Check guitar for vintage."""
        return self.get_age(current_year) >= 50

    def __str__(self):
        """Return guitar."""
        return f"{self.name} ({self.year}), worth ${self.cost:.2f}"

    def __lt__(self, other):
        """ Compare on year."""
        return self.year < other.year


def main():
    """Read guitars from file, sort, and display details."""
    guitars = []

    # Read guitars from the file
    with open('guitars.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))

    # Display guitars in the original order
    print("\nOriginal order of guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    # Sort the guitars by year (oldest to newest)
    guitars.sort()

    # Display guitars in sorted order
    print("\nGuitars, sorted by year:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    # Save the sorted list back to the file
    with open('sorted_guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()