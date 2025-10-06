def problema_troco(moedas, valor):
    moedas.sort(reverse=True)
    result = []
    total_value = 0

    atual = valor
    for m in range(len(moedas)):
        if m > atual:
            continue
        div = atual // moedas[m]
        atual = atual % moedas[m]
        for i in range(div):
            result.append(moedas[m])
    if atual != 0:
        return None
    return result


moedas = [2, 5, 10]
valor = 17
resultado = problema_troco(moedas, valor)

print(resultado)