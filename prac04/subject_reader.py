"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        lists = list(line.split(","))
        data.append(lists)
    input_file.close()
    return data


def display_data(data):
    """Displays data in a list."""
    longest_name = get_longest_name(data)
    for i in data:
        print(f"{i[0]} is taught by {i[1]:<{longest_name}} and has {i[2]} students")


def get_longest_name(data):
    """Gets the longest name in a list of lists."""
    longest_name = 0
    for i in data:
        if len(i[1]) > longest_name:
            longest_name = len(i[1])
    return longest_name


main()