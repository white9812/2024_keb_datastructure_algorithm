import time
def factorial(number) -> int:
    '''
    factorial by repetition
    :param number: number (int)
    :return: factorial result (int)
    '''
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result


# def factorial(number) -> int:
#     '''
#     factorial by recursion
#     :param number: number (int)
#     :return: factorial result (int)
#     '''
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
def nCr(n, r) -> int:
    '''
    조합 함수
    :param n:
    :param r:
    :return:
    '''
    start = time.time()
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    end = time.time()
    print(f"소요시간: {end - start}")
    return int(numerator / denominator)
#단일 책임의 원칙이 망가짐
#지금 이 함수는 조합을 구하면서 시간까지 재고 있음
#개방 페쇄의 원칙 데코레이터가 나와야함
#수정에는 닫혀있고 확장에는 열려있어야함
#따라서 nCr 함수를 건들이지 않고 데코레이터를 통해서 입히기
