def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>>contar_caracteres('marcos')
    {'a':'1', 'c':'1', 'm':'1', 'o':'1', 'r':'1', 's':'1',}
    >>>> contar_caracteres('banana')
    {'a': '3', 'b': '1', 'n': '2',}

    :param s: string a ser contada
    :return:
    """

    resultado={}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('Marcos'))
    print()
    print(contar_caracteres('banana'))
    print()
    print(contar_caracteres('macarronada'))
    print()
    print(contar_caracteres('555555555555555'))
    print()
    print(contar_caracteres('999_999_999**500'))
    print()