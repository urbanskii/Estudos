def change_temperature(c):
    f = (c*9/5) + 32
    return f


if __name__ == '__main__':
    input_temp = float(input('Digite a temperatura em Fahrenheit: '))
    return_temp = change_temperature(input_temp)
    print(str('{:9.2f}'.format(return_temp)))