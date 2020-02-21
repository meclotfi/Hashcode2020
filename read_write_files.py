F = open("f_libraries_of_the_world.txt", "r")
line1 = F.readline().split()
# total number of books
Books_number = int(line1[0])
# total number of libraries
library_number = int(line1[1])
# max days to scan
days_scan = int(line1[2])
# each book score
books_scores = [int(x) for x in F.readline().split()]
# libraies and thier content
Libraries = {}  # libraries information
# initialization of libraries
nb_lib = 0

print("simulation")


def sum_score(l):
    sum = 0
    for x in l:
        sum = sum+books_scores[x]
    return sum


i = 0
t = F.readline().split()
Max_score_lib = 0
Books_per_day_Max = 0
sign_up_Max = 0
while (t != []):

    l1 = [int(x) for x in t]
    t = F.readline().split()
    books_in_lib = [int(x) for x in t]
    # calculer somme de score pour chaque library
    score = sum_score(books_in_lib)
    if(score > Max_score_lib):
        Max_score_lib = score
    if(Books_per_day_Max < l1[2]):
        Books_per_day_Max = l1[2]
    if(sign_up_Max < l1[1]):
        sign_up_Max = l1[1]

    Libraries[i] = [l1[0], l1[1], l1[2], score, books_in_lib]
    i = i+1
    t = F.readline().split()
# saving the initial copy
Libraries_copy = Libraries


def score_normalization():
    critere = {}
    Max_criter_id = 0

    for lib in Libraries.items():

        a = lib[1][3]/Max_score_lib
        b = lib[1][2]/Books_per_day_Max
        c = 1-(lib[1][1]/sign_up_Max)
        critere[lib[0]] = (a+b+c)
        if(a == 0):
            critere[lib[0]] = 0
        if(critere[Max_criter_id] < critere[lib[0]]):
            Max_criter_id = lib[0]
    return critere, Max_criter_id


def Recalul_parameters():
    global Max_score_lib, Books_per_day_Max, sign_up_Max
    Max_score_lib = 1
    Books_per_day_Max = 1
    sign_up_Max = 1
    for lib in Libraries.items():

        a = lib[1][3]
        if(a > Max_score_lib):
            Max_score_lib = a
        b = lib[1][2]
        if(b > Books_per_day_Max):
            Books_per_day_Max = b
        c = 1-(lib[1][1]/sign_up_Max)
        if(c > sign_up_Max):
            sign_up_Max = c


result_string = " "


def string(list):
    string = ""
    for x in list:
        string = string+" "+str(x)
    return string[1:]


def takeSecond(elem):
    return elem[1]


def sort_book_list(list):
    score = []
    res = []
    i = 0
    for x in list:
        score.append((x, books_scores[x]))
    score.sort(key=takeSecond, reverse=True)
    if(len(score) != 0):
        while(i/len(score) < 0.5):
            res.append(score[i][0])
            i = i+1
    return res


def add_result(lib_id):
    result_string = ""
    sended_books = sort_book_list(Libraries[lib_id][4])
    result_string = result_string+str(lib_id)+" " +\
        str(len(sended_books))+"\n"+string(sended_books)+"\n"

    return result_string


def update_libraries(cr_id):
    global Libraries
    list = Libraries[cr_id][4]
    for lib in Libraries.values():
        lib[4] = [x for x in lib[4] if x not in list]
        lib[3] = sum_score(lib[4])
    print(len(Libraries.items()))


nb_lib = 0
str_res = ""


def main():
    str_res = ""
    nb_lib = 0
    jour_restans = days_scan
    while(jour_restans > 0):

        cr, cr_max_id = score_normalization()
        jour_restans = jour_restans-Libraries[cr_max_id][1]
        str_res = str_res+add_result(cr_max_id)
        update_libraries(cr_max_id)
        nb_lib = nb_lib+1
    return str(nb_lib)+"\n"+str_res


# traitement ici

file = open("e_result.txt", "w")
file.write(main())
file.close()
