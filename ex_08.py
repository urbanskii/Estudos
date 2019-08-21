
def monthly_salary(sal_hour, hour_worked):
    return sal_hour*hour_worked


if __name__ == '__main__':
    input_sal_hour = float(input('Put how much you earn per hour: '))
    if input_sal_hour.isnumeric() == False:
        print('Digite um valor numerico')
    input_hour_worked = float(input('Put the amount of hours worked in the month: '))
    print(monthly_salary(input_sal_hour, input_hour_worked))

