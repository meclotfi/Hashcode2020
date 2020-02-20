F = open("a_example.in", "r")
Max = int((F.readline().split())[0])
print(Max)
exapmles_dict = F.readline().split()
exapmles_dict = [int(x) for x in exapmles_dict]
print(exapmles_dict)


def sum(l):
    y = 0
    for x in l:
        y = y+x
    return y


def min_indice(diff):
    min = diff[0]
    i = 0
    ind_min = 0
    for x in diff:
        if(x < min):
            min = x
            ind_min = i
        i = i+1
    return ind_min


def adjust():
    actu = sum(exapmles_dict)-Max
    print(actu)
    diff = []
    while(actu > 0):
        actu = sum(exapmles_dict)-Max
        diff = [abs(actu-x) for x in exapmles_dict]
        min_i = min_indice(diff)
        exapmles_dict[min_i] = 0


def nb_type():
    i = 0
    for x in exapmles_dict:
        if (x > 0):
            i = i+1
    return i


def types_order():
    t = ""
    i = 0
    for x in exapmles_dict:
        if x > 0:
            t = t+" "+str(i)
        i = i+1
    return t[1:]


adjust()
file = open("a_result.in", "w")
file.write(str(nb_type())+"\n")
file.write(types_order())
file.close()
