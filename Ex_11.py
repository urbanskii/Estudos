def calc_numbers(ni_01,ni_02,nr_03):
    a = ((2*ni_01) + (ni_02/2))
    b = (3 * ni_01) + nr_03
    c = nr_03**3
    return a, b, c


if __name__ == '__main__':
    input_ni01 = int(input('Digite 1 numero inteiro: '))
    input_ni02 = int(input('Digite 1 numero inteiro: '))
    input_ni03 = float(input('Digite 1 numero Real: '))

    print(calc_numbers(input_ni01, input_ni02, input_ni03))
