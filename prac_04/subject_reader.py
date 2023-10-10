FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data


def display_subject_details(data):
    """Display subject details."""
    for subject_info in data:
        subject_code, lecturer, num_students = subject_info
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()
