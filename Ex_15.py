def monthly_salary(sal_hour, hour_worked):
    gross_salary = sal_hour*hour_worked
    tax_rate = gross_salary*0.11
    inss_tax = gross_salary*0.08
    syndicate = gross_salary*0.05
    net_salary = gross_salary - tax_rate - inss_tax - syndicate

    return gross_salary, tax_rate, inss_tax,syndicate,net_salary


if __name__ == '__main__':
    result = []
    input_sal_hour = float(input('Put how much you earn per hour: '))
    input_hour_worked = float(input('Put the amount of hours worked in the month: '))
    result = (monthly_salary(input_sal_hour, input_hour_worked))

    print('Gross Salary: ' + str('{:9.2f}'.format(result[0])))
    print('Tax rate(IR): ' + str('{:9.2f}'.format(result[1])))
    print('INSS: ' + str('{:9.2f}'.format(result[2])))
    print('Syndicate: ' + str('{:9.2f}'.format(result[3])))
    print('Net salary: ' + str('{:9.2f}'.format(result[4])))