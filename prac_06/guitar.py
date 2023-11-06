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


def main():
    """Get user guitar and display details."""
    print("My guitars!")

    guitars, current_year, i = [], 2023, 1
    name = input("Name: ")
    while name:
        year, cost = int(input("Year: ")), float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
