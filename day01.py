import random
answer=random.randint(1,100)
chance=7
print(answer)
while chance !=0 :
    guess=int(input("Input guess number: "))
    if guess == answer:
        print(f"You win. Answer is {answer}",chance)
        break
    elif guess > answer:
        chance=chance-1
        print(f"{guess} number is bigger than answer",chance)
    else:
        chance=chance-1
        print(f"{guess} is lower than answer",chance)
        #크다 작다를 알려주는 것은 중앙값을 이용하게 하여 수학적으로 이길 수 밖에 없게 됨
        #힌트가 사라진다면 입력한 수가 맞는지 아닌지만 알게됨
        #최악의 경우 100번째 만에 알게 될 수도 있음
        #힌트가 사라지면 선형시간을 갖게 됨
else:
    print(f"you lost.Answer is {answer}")