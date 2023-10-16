def main():
    """Read Wimbledon champions data, process, and display information."""
    data = read_data("wimbledon.csv")

    champion_counts, country_set = process_data(data)

    display_champion_counts(champion_counts)
    display_countries(country_set)


def read_data(filename):
    """Read data from the file and return a list of lists: [Champion, Country]."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            champion, country, count = line.strip().split(',')
            data.append([champion, country])
    return data


def process_data(data):
    """Process data and return champion counts and a set of countries."""
    champion_counts = {}
    country_set = set()

    for champion, country in data:
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
        country_set.add(country)

    return champion_counts, country_set


def display_champion_counts(champion_counts):
    """Display champions and their win counts."""
    print("Wimbledon Champions:")
    for champion, count in champion_counts.items():
        print(f"{champion} {count}")


def display_countries(country_set):
    """Display countries in alphabetical order."""
    countries = sorted(country_set)
    print("\nThese countries have won Wimbledon:")
    print(', '.join(countries))


main()
