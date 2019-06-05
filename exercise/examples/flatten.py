liste = []
def flatten (lst):
    for i in lst :
        if (type (i)== list):
            for j in i:
                if (type (j)!=list):
                    liste.append(j)
