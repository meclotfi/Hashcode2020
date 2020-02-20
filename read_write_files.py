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
while (t != []):

    l1 = [int(x) for x in t]
    print(l1)
    t = F.readline().split()
    books_in_lib = [int(x) for x in t]
    # calculer somme de score pour chaque library
    score = sum_score(books_in_lib)
    if(score > Max_score_lib):
        Max_score_lib = score
    if(Books_per_day_Max < l1[2]):
        Books_per_day_Max = l1[2]

    Libraries[i] = [l1[0], l1[1], l1[2], score, books_in_lib]
    i = i+1
    t = F.readline().split()

print(Books_per_day_Max)


def score_normalization():
    for lib in Libraries.items:
        lib[3] = lib[3]/Max_score_lib


print(Libraries)
# traitement ici


file = open("a_result.txt", "w")
file.write("result")
file.close(),
