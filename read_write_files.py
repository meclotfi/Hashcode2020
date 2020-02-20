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
variable
#

file = open("a_result.txt", "w")
file.write("result")
file.close(),
