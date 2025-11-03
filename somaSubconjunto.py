"""
Problema da Soma dos Subconjuntos

O problema da soma dos subconjuntos é um problema de ciência da computação que 
consiste em verificar se, dado um conjunto de inteiros, existe um subconjunto não-vazio cuja soma é zero. 

Por exemplo, no conjunto {-7, -3, -2, 5, 8}, a resposta é sim, pois o subconjunto {-3, -2, 5} resulta em uma soma de zero. 

1- Faça um método que recebe um conjunto de inteiros e retorna um subconjunto cuja soma seja zero;
2- Altere o método para que retorne todos subconjuntos cuja soma seja zero;
3- Analise a complexidade de ambas as soluções.

"""

def subconjunto(a):
    return percorre(a, 0, [])
    

def percorre(a, index, sc):
    if len(sc) > 0:
        soma_atual = sum(sc)
        if soma_atual == 0:
            return sc
    
    if index >= len(a):
        return None

    if len(a) == 0:
        return None
    
    temp_com_elemento = sc.copy()
    temp_com_elemento.append(a[index])
    resultado_com = percorre(a, index + 1, temp_com_elemento)
    if resultado_com is not None:
        return resultado_com
    
    resultado_sem = percorre(a, index + 1, sc)
    if resultado_sem is not None:
        return resultado_sem
    
    return None

print("Resultado:")
print(subconjunto([-7, -3, -2, 5, 8]))

print("\n" + "="*60)
print("CASOS DE TESTE PARA VALIDAR O ALGORITMO")
print("="*60)

# Teste 1: Caso básico com solução
print("\nTeste 1 - Caso original:")
resultado1 = subconjunto([-7, -3, -2, 5, 8])
print(f"Conjunto: [-7, -3, -2, 5, 8]")
print(f"Resultado: {resultado1}")
if resultado1:
    print(f"Soma: {sum(resultado1)}")

# Teste 2: Conjunto com zero
print("\nTeste 2 - Conjunto com zero:")
resultado2 = subconjunto([0, 1, -1, 2])
print(f"Conjunto: [0, 1, -1, 2]")
print(f"Resultado: {resultado2}")
if resultado2:
    print(f"Soma: {sum(resultado2)}")

# Teste 3: Apenas números positivos (sem solução)
print("\nTeste 3 - Apenas positivos:")
resultado3 = subconjunto([1, 2, 3, 4])
print(f"Conjunto: [1, 2, 3, 4]")
print(f"Resultado: {resultado3}")
if resultado3:
    print(f"Soma: {sum(resultado3)}")

# Teste 4: Apenas números negativos (sem solução)
print("\nTeste 4 - Apenas negativos:")
resultado4 = subconjunto([-1, -2, -3, -4])
print(f"Conjunto: [-1, -2, -3, -4]")
print(f"Resultado: {resultado4}")
if resultado4:
    print(f"Soma: {sum(resultado4)}")

# Teste 5: Par de números opostos
print("\nTeste 5 - Números opostos:")
resultado5 = subconjunto([5, -5, 3, 7])
print(f"Conjunto: [5, -5, 3, 7]")
print(f"Resultado: {resultado5}")
if resultado5:
    print(f"Soma: {sum(resultado5)}")

# Teste 6: Conjunto vazio
print("\nTeste 6 - Conjunto vazio:")
resultado6 = subconjunto([])
print(f"Conjunto: []")
print(f"Resultado: {resultado6}")
if resultado6:
    print(f"Soma: {sum(resultado6)}")

# Teste 7: Um único elemento zero
print("\nTeste 7 - Único elemento zero:")
resultado7 = subconjunto([0])
print(f"Conjunto: [0]")
print(f"Resultado: {resultado7}")
if resultado7:
    print(f"Soma: {sum(resultado7)}")

# Teste 8: Três elementos que somam zero
print("\nTeste 8 - Três elementos:")
resultado8 = subconjunto([-2, 1, 1])
print(f"Conjunto: [-2, 1, 1]")
print(f"Resultado: {resultado8}")
if resultado8:
    print(f"Soma: {sum(resultado8)}")

# Teste 9: Múltiplas soluções possíveis
print("\nTeste 9 - Múltiplas soluções:")
resultado9 = subconjunto([-1, 1, -2, 2])
print(f"Conjunto: [-1, 1, -2, 2]")
print(f"Resultado: {resultado9}")
if resultado9:
    print(f"Soma: {sum(resultado9)}")

# Teste 10: Elementos duplicados
print("\nTeste 10 - Elementos duplicados:")
resultado10 = subconjunto([2, 2, -2, -2, 1])
print(f"Conjunto: [2, 2, -2, -2, 1]")
print(f"Resultado: {resultado10}")
if resultado10:
    print(f"Soma: {sum(resultado10)}")

# Teste 11: Conjunto maior
print("\nTeste 11 - Conjunto maior:")
resultado11 = subconjunto([-5, -3, -1, 2, 4, 6])
print(f"Conjunto: [-5, -3, -1, 2, 4, 6]")
print(f"Resultado: {resultado11}")
if resultado11:
    print(f"Soma: {sum(resultado11)}")

# Teste 12: Solução que usa todos os elementos
print("\nTeste 12 - Todos os elementos:")
resultado12 = subconjunto([-1, -1, 1, 1])
print(f"Conjunto: [-1, -1, 1, 1]")
print(f"Resultado: {resultado12}")
if resultado12:
    print(f"Soma: {sum(resultado12)}")
    
# Teste 13: Caso especial com um positivo
print("\nTeste 13 - Um positivo entre negativos:")
resultado13 = subconjunto([-1, -2, -3, 6])
print(f"Conjunto: [-1, -2, -3, 6]")
print(f"Resultado: {resultado13}")
if resultado13:
    print(f"Soma: {sum(resultado13)}")

# Teste 14: pula um
print("\nTeste 14 - Pula um:")
resultado14 = subconjunto([-1, -2, -3, 4])
print(f"Conjunto: [-1, -2, -3, 4]")
print(f"Resultado: {resultado14}")
if resultado14:
    print(f"Soma: {sum(resultado14)}")

print("\n" + "="*60)
print("FIM DOS TESTES")
print("="*60)