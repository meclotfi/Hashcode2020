F = open("a_example.txt", "r")
line1 = F.readline().split()
Books_number = int(line1[0])
library_number = int(line1[1])
days_scan = int(line1[2])
books_scores = [int(x) for x in F.readline().split()]
print(books_scores)
Libraries = {}
i = 0
t = F.readline().split()
while (t != []):

    l1 = [int(x) for x in t]
    print(l1)
    t = F.readline().split()
    books_in_lib = [int(x) for x in t]
    Libraries[i] = [l1[0], l1[1], l1[2], books_in_lib]
    i = i+1
    t = F.readline().split()
print(Libraries)
# traitement ici

file = open("a_result.txt", "w")
file.write("result")
file.close(),
