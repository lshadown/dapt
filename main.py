import re

REGEX_NUMBER = r"[-| ]{1}[0-9]+"
REGEX_FOR = r"^.*for.*\(.*\)"

global numbers_list_        # wszystkie listy w liniach danego pliku
global numbers_list_all     # lista wszystkich listy 3 plików


def read_file(file_path):
    file = open(file_path, "r")
    return file.readlines()


def find_all_number(file_content):
    counter = 1
    numbers_list = []
    for line in file_content:
        result = re.search(REGEX_FOR, line)
        if result is not None:
            numb = re.findall(REGEX_NUMBER, line)
            ref_numb = []
            numbers_list.append(ref_numb)
            for num in numb:
                if len(num.split(' ')) > 1:
                    ref_numb.append('$' + num.split(' ')[1])
                else:
                    ref_numb.append('$' + num)
                counter += 1
            print_line = line.replace(' ', '')
            print(print_line)
            print(ref_numb)
    numbers_list_all.append(numbers_list)


def valid():
    # poszczegolne listy w danych liniach musza miec ta sama dlogusc
    return(True)


if __name__ == '__main__':
    path_files = ["example/example2.c", "example/example3.c", "example/example_4.c"]
    numbers_list_all = []
    for path_file in path_files:
        file_content = read_file(path_file)
        find_all_number(file_content)
    print(numbers_list_all)

