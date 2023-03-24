with open("ex4.txt", 'r')as f:
    Lst = f.readline().split()
    Lalf = f.readline().split()
    L = []
    aux = f.readline()
    while aux:
        L.append(aux.strip().split())
        aux = f.readline()
    init = L[len(L)-2][0]
    fin = L[len(L)-1]
cuv = input("Dati cuvantul pe care doriti sa il testam: ")
print(init,fin)

aux = [init]
L2 = [aux]
max = 0

for i in range(len(cuv)):
    j = 0
    while j < len(L):
        faux = j
        aux = j
        if L[j][0] == L2[-1][-1] and L[j][1] == cuv[i]:
            while L[faux+1][0] == L2[-1][-1] and L[faux+1][1] == cuv[i]:
                L2.append([L2])
                faux = faux + 1
            aux2 = faux
            for k in range (len(L2)):
                if len(L2[k]) > max:
                    max = len(L2[k])
            for k in range(len(L2)):
                if len(L2[k]) == max and aux <= aux2:
                    L2[k].append(L[aux][2])
                    aux += 1
                    # j = aux2
        j += 1
print(L2)



