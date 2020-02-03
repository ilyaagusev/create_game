import os


def make_directory(directory_name):
    current_directory = os.getcwd()
    new_directory_name = os.path.join(current_directory, directory_name)
    os.makedirs(new_directory_name, exist_ok=True)
    return new_directory_name
