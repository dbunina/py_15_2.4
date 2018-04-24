from os import path, listdir

migrations = 'Migrations'
current_dir = path.dirname(path.abspath(__file__))


def search(search_string, file_list):
    result = []
    for file in file_list:
        if contains_in_file(file, search_string):
            result.append(file)
    return result


def contains_in_file(file, search_string):
    with open(file) as f:
        for line in f:
            if search_string in line:
                return True
    return False


def find_files_by_extension(extension):
    search_dir = path.join(current_dir, migrations)
    result = []
    for file in listdir(search_dir):
        if file.endswith(extension):
            file_path = path.join(search_dir, file)
            result.append(file_path)
    return result


if __name__ == '__main__':
    files = find_files_by_extension('.sql')
    while True:
        user_input = input('Enter string to search:')
        files = search(user_input, files)
        print('\n'.join(files))
        print('Found files: {}'.format(len(files)))
