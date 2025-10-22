# O problema das N-rainhas consiste em encontrar uma combinação possível de N rainhas num tabuleiro de dimensão N por
# N tal que nenhuma das rainhas ataque qualquer outra. Duas rainhas atacam-se uma à outra quando estão na mesma linha,
# na mesma coluna ou na mesma diagonal do tabuleiro. Na figura que se segue pode ver-se as posições atacadas
# por uma rainha colocada num tabuleiro de dimensão 7 por 7 e ao lado uma possível solução para esse mesmo tabuleiro.
import numpy as np

def verificar_rainha(tabuleiro, posicao):
    n = tabuleiro.shape[0]
    i,j = posicao

    while(j >= 0):
        if tabuleiro[i, j] == 1:
            return False
        j -= 1
    i,j = posicao

    while(i>=0 and j>=0):
        if tabuleiro[i, j] == 1:
            return False
        i -= 1
        j -= 1
    i,j = posicao

    while(i<n and j>=0):
        if tabuleiro[i, j] == 1:
            return False
        i += 1
        j -= 1
    return True
    

def n_rainhas(n):
    tabuleiro = np.zeros((n,n))
    return busca(0, 0, tabuleiro)

def busca(i, j, tabuleiro):
    if j >= len(tabuleiro):
        return tabuleiro
    aux = 0
    while(aux < len(tabuleiro)):
        newtab = tabuleiro.copy()
        check = verificar_rainha(tabuleiro, (aux,j))
        if check:
           newtab[aux][j] = 1
           res = busca(aux, j+1, newtab)
           if res is not None:
               return res
        aux += 1
    return None


# teste = np.zeros((5,5))
# teste[1,1] = 1

print(n_rainhas(10))