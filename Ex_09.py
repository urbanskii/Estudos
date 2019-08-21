def change_temperature(f):
    c = (5*(f-32)/9)
    return c


if __name__ == '__main__':
    input_temp = float(input('Digite a temperatura em graus Farenheit: '))
    return_temp = change_temperature(input_temp)
    print(str('{:9.2f}'.format(return_temp)))

