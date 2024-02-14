def decimal_to_octal(number:int)-> str:
    '''
    decimal number to octal number (by recursion)
    :param number:interger (base dec)
    :return: string (base octal)
    '''
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(number//8) +str(number%8)
    # octal=" "
    # while number > 0:
    #     octal = str(number % 8) + octal
    #     number = number // 8

    return octal
n = int(input("Input decimal number : "))
print(decimal_to_octal(n))