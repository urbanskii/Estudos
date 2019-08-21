def show_average(result_01, result_02, result_03, result_04):
    """
    This program returns to bimonthly grades

    :param result_01: Receive a grad number1
    :param result_02: Receive a grad number2
    :param result_03: Receive a grade number3
    :param result_04: Receive a grade number4
    :return:
    """
    return (result_01 + result_02 + result_03 + result_04)/4


if __name__ == '__main__':
    print(show_average(65, 45, 79, 96))