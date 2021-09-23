import re

REGEX_NUMBER = r"[-| ]{1}[0-9]+"
REGEX_FOR = r"^.*for.*\(.*\)"


def read_file(file_path):
    file = open(file_path, "r")
    return file.readlines()


def find_all_number(file_content):
    counter = 1
    for line in file_content:
        result = re.search(REGEX_FOR, line)
        if result is not None:
            numb = re.findall(REGEX_NUMBER, line)
            ref_numb = []
            for num in numb:
                if len(num.split(' ')) > 1:
                    ref_numb.append('$' + num.split(' ')[1])
                else:
                    ref_numb.append('$' + num)
                counter += 1
            print_line = line.replace(' ', '')
            print(print_line)
            print(ref_numb)


if __name__ == '__main__':
    path_files = ["example/example2.c", "example/example3.c", "example/example_4.c"]
    for path_file in path_files:
        file_content = read_file(path_file)
        find_all_number(file_content)

