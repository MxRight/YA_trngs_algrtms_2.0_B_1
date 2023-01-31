r, i, c = int(input()), int(input()), int(input())

dict_it = {0: 3 if r != 0 else c, 1: c, 4: 3 if r != 0 else 4, 6: 0, 7: 1}

if i in dict_it:
    print(dict_it[i])
else:
    print(i)
