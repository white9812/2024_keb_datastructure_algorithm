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
else:
    print(f"you lost.Answer is {answer}")