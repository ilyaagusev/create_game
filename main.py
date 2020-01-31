import abilities_generator as ag
import directory_maker as dm
import file_operations as fo


def make_charsheet(directory_path, number, abilities):
    fo.render_template(
        'charsheet.svg',
        '{0}\charsheet-{1}.svg'.format(directory_path, number), abilities)


def main():
    new_name = dm.make_directory('charsheets')
    counter = 0
    for number in range(10):
        counter += 1
        abilities = ag.generate_abilities()
        make_charsheet(new_name, counter, abilities)


if __name__ == "__main__":
    main()
