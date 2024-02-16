memo=[0,1]
count=0
def fibo_memoization(n:int)-> int:

    '''
    fibonacci function by recursion with memoization
    :param n: integer number
    :return: integer number
    '''
    global memo ,count

    for i in range(0,n+1):
        memo.append(memo[i]+memo[i+1])
        count+=1
    return memo[n-1],count

n=int(input("Int number: "))

print(fibo_memoization(n))
