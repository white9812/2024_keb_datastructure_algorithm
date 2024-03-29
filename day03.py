# def fibo_recursion(n) :
#     '''
#     fibonacci function by recursion
#     :param n: integer number
#     :return: integer number
#     성능이 안좋음
#     '''
#     if n == 0 :
#         return 0
#     elif n == 1 :
#         return 1
#     else :
#         return fibo_recursion(n - 1) + fibo_recursion(n - 2)
#
# # print('피보나치 수 --> 0 1 ', end='')
# for i in range(0, 20) :
# 	print(fibo_recursion(i), end=' ')
#
# def fibo_repetition_my(number:int)->int:
#     '''
#
#     :param number: integer number
#     :return: integer number
#     '''
#     a=[0,1]
#     # n=int(input("Input number: "))
#         for i in range(1,number):
#             a.append(a[i]+a[i-1])
#     print(a[i]+a[i-1])


# 교수님 풀이
# a=b
# b=a+b
# return a
# 참조 때문에 안됐음 -> temp 를 쓰거나 아님 패킹 언패킹하기
# c++에서는 temp 써야함
# memo=[None for _ in range(100)] #한번 했던 계산읋 하지않기위해 메모리를 사용한다. 공간하나 씀으로써
# memo[0]=0
# memo[1]=1

# memo=[0 if i==0 else 1 if i == 1 else None for i in range(100) ]
memo=[0,1]+[None]*(100-1)
def fibo_memoization(n:int)-> int:

    '''
    fibonacci function by recursion with memoization
    :param n: integer number
    :return: integer number
    '''
    global memo
    if memo[n] is not None:
        return memo[n]
    # if n < 2:
    #     result = n
    # else:
    result = fibo_memoization(n-1)+fibo_memoization(n-2)

    memo[n]=result
    return result
n=int(input("Int number: "))
for i in range(0,n):
    print("<",i,">")
    print(fibo_memoization(i))
print(fibo_memoization(n),memo)
