def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>>contar_caracteres('marcos')
    a:1
    c:1
    m:1
    o:1
    r:1
    s:1
    >>>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    :return:
    """


    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]

    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior=caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('Marcos')
    print()
    contar_caracteres('banana')
    print()
    contar_caracteres('macarronada')
    print()
    contar_caracteres('555555555555555')
    print()
