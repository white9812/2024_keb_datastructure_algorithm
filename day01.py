import random
answer=random.randrange(100)
number=int(input())
if number==answer :
    print ("정답입니다. 시도횟수 ",1)
elif number!=answer:
        print("틀렸습니다. 숫자를 다시 입력하세요.")
        count=0
        while(number1!=answer):
            number1=int(input())
            count++
            print("틀렸습니다. 시도횟수 ", count)

            break number