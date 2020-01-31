import os


def make_directory(directory_name):
    current_directory = os.getcwd()
    new_directory_name = '{0}\{1}'.format(current_directory, directory_name)
    os.makedirs(new_directory_name)
    return new_directory_name
