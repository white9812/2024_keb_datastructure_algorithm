def print_poly(t_x,f_x) -> str:

    poly_expression = "f(x) = "

    for i in range(len(fx)):
        term=t_x[i]
        coefficient = f_x[i]
        #if coefficient !=0: <- 내 생각

        if coefficient >=0 and i !=0 :
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '


    return poly_expression


def calculation_poly(x_value, t_x,f_x) -> int:
    return_value = 0

    for i in range(len(fx)):
        term=t_x[i]
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, term)


    return return_value

tx=[300,20,0]
fx = [7,-4,5]

if __name__ == "__main__":
    print(print_poly(tx,fx))
    print(calculation_poly(int(input("x 값 : ")),tx, fx))