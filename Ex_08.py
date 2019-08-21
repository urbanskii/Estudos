def salary_calc(hourly_gain, worked_hours):
    return hourly_gain * worked_hours


if __name__ == '__main__':
    hourly_gain = int(input('How much do you earn per hour?: '))
    worked_hour = int(input('Hours work int the month?: '))

    print(salary_calc(hourly_gain, worked_hour))