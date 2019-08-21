def ideal_weight(height,gender):
    if gender == 'Male':
        return (72.7*height) - 58
    else:
        return (62.1*height) - 44.7


if __name__ == '__main__':
    gender_input = input('Type your gender: ')
    height_input = float(input('Type your height: '))
    print('Your ideal weight: ')
    print(ideal_weight(height_input, gender_input))

