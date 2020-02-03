import os
import profile_generator
import directory_maker
import file_operations


def make_charsheet(directory_path, number, profile_data):
    filename = 'charsheet-{0}.svg'.format(number)
    filepath = os.path.join(directory_path, filename)
    file_operations.render_template(
        'charsheet.svg', filepath, profile_data)


def main():
    new_directory = directory_maker.make_directory('charsheets')
    counter = 0
    for number in range(10):
        counter += 1
        profile_data = profile_generator.generate_profile()
        make_charsheet(new_directory, counter, profile_data)


if __name__ == "__main__":
    main()
