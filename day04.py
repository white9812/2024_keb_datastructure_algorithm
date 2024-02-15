## 함수 선언 부분 ##
def palindrome(pStr) :
    # print(pStr)
    if len(pStr) <= 1 :
        return True

    if pStr[0] != pStr[-1] :
        return False

    return palindrome(pStr[1:len(pStr)-1]) # 슬라이싱


## 전역 변수 선언 부분 ##
strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번주 주번이 너야", "살금 살금"]
a='봄봄'
print(a[1:len(a)-1])
## 메인 코드 부분 ##

for testStr in strAry :
    print(testStr, end = '--> ' )
    testStr = testStr.lower().replace(' ','') #"주유소의소유주" 이런식으로 띄어쓰기 사라짐
    if palindrome(testStr) :
        print('O')
    else :
        print('X')
