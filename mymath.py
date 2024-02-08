import time
def timer (func):
    def wrapper(*argc,**kwargs):
        start = time.time()
        result= func(*argc,**kwargs)
        end=time.time()
        print(f"time elapsed: {end - start}")

        return result
    return wrapper #closer는 함수 이름만 return 그래서 그냥 inner함수랑은 다름

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
@timer
def nCr(n, r) -> int: #SRP,OCP violation
    '''
    조합 함수
    :param n:
    :param r:
    :return:
    '''

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return int(numerator / denominator)
#단일 책임의 원칙이 망가짐
#지금 이 함수는 조합을 구하면서 시간까지 재고 있음
#개방 페쇄의 원칙 데코레이터가 나와야함
#수정에는 닫혀있고 확장에는 열려있어야함
#따라서 nCr 함수를 건들이지 않고 데코레이터를 통해서 입히기
