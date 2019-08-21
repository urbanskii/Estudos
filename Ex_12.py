def ideal_weight(height):
    return (72.7*height) - 58


if __name__ == '__main__':
    input_height = float(input('Enter your height to calculate your ideal weight: '))
    print('Your ideal weight: ')
    print(ideal_weight(input_height))