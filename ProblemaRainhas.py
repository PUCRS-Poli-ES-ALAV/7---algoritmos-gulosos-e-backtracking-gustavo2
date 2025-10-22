# O problema das N-rainhas consiste em encontrar uma combinação possível de N rainhas num tabuleiro de dimensão N por
# N tal que nenhuma das rainhas ataque qualquer outra. Duas rainhas atacam-se uma à outra quando estão na mesma linha,
# na mesma coluna ou na mesma diagonal do tabuleiro. Na figura que se segue pode ver-se as posições atacadas
# por uma rainha colocada num tabuleiro de dimensão 7 por 7 e ao lado uma possível solução para esse mesmo tabuleiro.
import numpy as np

def verificar_rainha(tabuleiro, posicao):
    n = tabuleiro.shape[0]
    atual = posicao.copy()

    while(atual[1] >= 0):
        print(atual)
        if tabuleiro[atual[0], atual[1]] == 1:
            return False
        atual[1] -= 1
    atual = posicao.copy()

    while(atual[1] <= n-1):
        print(atual)
        if tabuleiro[atual[0], atual[1]] == 1:
            return False
        atual[1] += 1
    atual = posicao.copy()

    while(atual[0] >= 0):
        print(atual)
        if tabuleiro[atual[0], atual[1]] == 1:
            return False
        atual[0] -= 1
    atual = posicao.copy()

    while(atual[0] <= n-1):
        print(atual)
        if tabuleiro[atual[0], atual[1]] == 1:
            return False
        atual[0] += 1
    atual = posicao.copy()
    return True

def n_rainhas(n):
    i,j = 2,2
    tabuleiro = np.zeros((n,n))
    tabuleiro[4,2] = 1
    if verificar_rainha(tabuleiro, [i,j]):
        tabuleiro[i,j] = 1
    print(tabuleiro)
    return tabuleiro

tabuleiro = n_rainhas(5)