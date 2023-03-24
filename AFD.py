with open("ex", 'r')as f:
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

aux = init
L2 = [aux]
for i in range(len(cuv)):
    for k in range(len(L)):
        if aux == L[k][0] and cuv[i] == L[k][1]:
            aux = L[k][2]
            L2.append(aux)
            break

if aux not in fin:
    print("CUVANTUL NU ESTE ACCEPTAT!")
else:
    print("CUVANTUL ESTE ACCEPTAT!")
    for i in L2:
        print(f"{i}==>",end='')
    print("STOP")









