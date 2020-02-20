F = open("a_example.txt", "r")
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
        critere[lib[0]] = (a+b+c)/3
        if(critere[Max_criter_id] < critere[lib[0]]):
            Max_criter_id = lib[0]
    return critere, Max_criter_id


result_dict = []


def add_result(lib_id):
    sended_books = Libraries[lib_id][4]
    result_dict.append([lib_id, len(sended_books), sended_books])


def update_libraries(cr_id):
    list = Libraries[cr_id][4]
    for lib in Libraries.values():
        lib[4] = [x for x in lib[4] if x not in list]


def main():
    jour_restans = days_scan
    while(jour_restans > 0):
        cr, cr_max_id = score_normalization()
        jour_restans = jour_restans-Libraries[cr_max_id][1]
        add_result(cr_max_id)
        update_libraries(cr_max_id)


main()
print(result_dict)
print(Libraries)
# traitement ici


file = open("a_result.txt", "w")
file.write("result")
file.close(),
