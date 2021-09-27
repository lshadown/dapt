import re
from sympy import symbols, Eq, solve

#REGEX_NUMBER = r"[-| ]{1}[0-9]+"
REGEX_NUMBER = r"[+-]?\d+"
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
            line1 = line.replace(' ', '')
            numb = re.findall(REGEX_NUMBER, line1)
            ref_numb = []
            numbers_list.append(numb)
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
    # TODO
    # poszczegolne listy w danych liniach musza miec ta sama dlogusc
    return(True)


def multi(tile_sizes, vec):

    if tile_sizes[0][0]*tile_sizes[0][1]==int(vec[0]) and tile_sizes[1][0]*tile_sizes[1][1]==int(vec[1]) and tile_sizes[2][0]*tile_sizes[2][1]==int(vec[2]):
        return("(b1*b2)")
    else:
        return("")


def make_eq(tile_sizes, vec):

    # czy liczba zalezna jest od tile sizes (zmienna)
    result = vec.count(vec[0]) == len(vec)
    if(result):
        return str(vec[0])

    # sprawdz czy tile sizes to wynik jesli tak zwroc b1*b2, to na fix, w tym kodzie zadziala
    # jest jedna liczba ktora jest iloczynem
    res = multi(tile_sizes, vec)
    if(res == "(b1*b2)"):
        return res

    # szukamy rownan liniowych
    b1,b2,c = symbols('b1 b2 c')

    # to da sie zrobic forem
    eq1 = Eq(tile_sizes[0][0]*b1 + tile_sizes[0][1]*b2 + c,int(vec[0]))
    eq2 = Eq(tile_sizes[1][0]*b1 + tile_sizes[1][1]*b2 + c,int(vec[1]))
    eq3 = Eq(tile_sizes[2][0]*b1 + tile_sizes[2][1]*b2 + c,int(vec[2]))

    sol = solve((eq1, eq2,eq3), (b1,b2,c))
    # print(sol)  #slownik zmieniamy na str


    
    expr = "("
    for k, v in sol.items():
        if(str(k) != 'c'):
            if(v !=0):
                if expr != "(" and v > 0:  # nie b1 i dodatnie
                    expr += " + " 
                expr += str(v) + '*' + str(k)   # mozna cos poprawic np usunac 1*  lub -1* na -
        else:
            if(v > 0):  # wyraz wolny, c=0 nie dodajemy  
                expr += " + " + str(v)
            if(v < 0):
                expr += str(v)

    expr += ")"

    return(expr)



if __name__ == '__main__':
    path_files = ["example/example2.c", "example/example3.c", "example/example_4.c"]
    numbers_list_all = []
    for path_file in path_files:
        file_content = read_file(path_file)
        find_all_number(file_content)
    print(numbers_list_all)

    tile_sizes = [[31,83], [103,179], [67,149]] #dana wejsciowa, moze niech plik example te sizes ma w komentarzu

    # wykonac dla wszystkich ale jesli sa rozne, inaczej to stała
    #vec = [numbers_list_all[0][0][0],numbers_list_all[1][0][0],numbers_list_all[2][0][0]]

    # zastap liczby wyrazeniami, wyparsuj kod
    #print(make_eq(tile_sizes, vec))


    for i in range(0, len(numbers_list_all[0])):
        for j in range(0, len(numbers_list_all[0][i])):
            vec = [numbers_list_all[0][i][j],numbers_list_all[1][i][j],numbers_list_all[2][i][j]]
            print(vec)
            print(make_eq(tile_sizes, vec))
        print('---')




    #koniec

