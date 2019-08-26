def weight_out_calc(fished):
    weight_fished_extra = (fished-50)
    fine_weight = weight_fished_extra * 4
    return weight_fished_extra, fine_weight


if __name__ == '__main__':
    result=[]
    input_fished_weight = float(input('Type the quantity of weight fished: '))
    result = weight_out_calc(input_fished_weight)
    print('Result of exceeded fished weight: ' + str(result[0]))
    print('The fine aplicated for the exceed of fished weight: ' + str(result[1]))
