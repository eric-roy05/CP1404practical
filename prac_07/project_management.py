import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __lt__(self, other):
        """Comparison based on priority ."""
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, " \
               f"completion: {self.completion}%"


def load_projects(filename):
    """Load project from text file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, start_date, priority, estimate, completion = line.strip().split(',')
                projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects


def save_projects(filename, projects):
    """Save project to a text file."""
    with open(filename, 'w') as file:
        for project in projects:
            file.write(
                f"{project.name},{project.start_date},{project.priority},{project.estimate},{project.completion}\n")


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    filter_date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(filter_date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > filter_date]
        display_projects(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))
    print("Project added.")


def update_project(projects):
    """Update completion % and/or priority of a project."""
    display_projects(projects)
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
        print(f"{project.name} updated.")
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid project number.")


def main():
    projects = load_projects("projects.txt")
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            projects = load_projects("projects.txt")

        elif choice == 's':
            save_projects("projects.txt", projects)

        elif choice == 'd':
            display_projects(projects)

        elif choice == 'f':
            filter_projects_by_date(projects)

        elif choice == 'a':
            add_new_project(projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()
