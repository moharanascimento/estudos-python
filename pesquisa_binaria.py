def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista)-1
    tentativas = 0

    while baixo <= alto:
        meio = int((baixo+alto)/2)
        chute = lista[meio]
        tentativas += 1

        if chute == item:
            return meio, tentativas
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None

minha_lista = [1,3,5,7,9,10,14,16,19,20]

print(pesquisa_binaria(minha_lista,10)) 