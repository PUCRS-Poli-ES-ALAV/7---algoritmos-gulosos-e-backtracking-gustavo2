def escalonamento_intervalos(s, f):
    dupla = []
    h_atual = 0
    X = []

    for i in range(len(s)):
        dupla.append([i, s[i], f[i]])
        X.append(0)
    
    dupla.sort(key=lambda x: x[2])

    for x in dupla:
        if x[1] > h_atual:
            X[x[0]] = 1
            h_atual = x[2]
    
    return X
    


s = [4,6,13,4,2,6,7,9,1,3,9]
f = [8,7,14,5,4,9,10,11,6,13,12]

X = escalonamento_intervalos(s, f)
print(X)