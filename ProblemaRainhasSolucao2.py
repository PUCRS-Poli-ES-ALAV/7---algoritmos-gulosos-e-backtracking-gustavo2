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

def rainha_recur(tabuleiro, i, j):
    n = tabuleiro.shape[0]
    verif = True
    if i == n:
        return tabuleiro, False
    if j == n:
        return tabuleiro, True
    if verificar_rainha(tabuleiro, [i,j]):
        tabuleiro[i,j] = 1
        tabuleiro, verif = rainha_recur(tabuleiro,0,j+1)
    else:
        tabuleiro, verif = rainha_recur(tabuleiro,i+1,j)
    if verif == False:
        tabuleiro[i,j] = 0
        tabuleiro, verif = rainha_recur(tabuleiro,i+1,j)
    return tabuleiro, verif


def n_rainhas(n):
    if n < 3:
        print("Tamanho deve ser maior que 3!")
        return tabuleiro
    tabuleiro = np.zeros((n,n))
    tabuleiro,verif = rainha_recur(tabuleiro,0,0)
    return tabuleiro


tabuleiro = n_rainhas(5)
print(tabuleiro)