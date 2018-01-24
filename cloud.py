import random

#19윤년

def isLeapYear():
    year = int(input('윤년 여부 알고싶은 년도 입력'))
    isleap = '윤년아님'
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        isleap = '윤년'
    print('%d는 %s' %(year,isleap))



#20
import random
def lotto():
    lotto = str(random.randint(100,999))
    lucky = input('번호입력')
    match = 0
    prize = '다음에'

    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if (lucky[i] == lotto[j]):
                match+=1
    if match ==3: prize = '1등'
    elif match == 2: prize = '2등'
    elif match == 1: prize = '3등'
    print(lucky,lotto,prize)



#계산기
def intCal():
    num1 = int((input('num1')))
    num2 = int((input('num2')))
    fmt = '%d+%d=%d \n %d+%d=%d \n'
    fmt += '%d*%d=%d \n %d/%d=%d \n'
    fmt += '%d**%d=%d \n'
    print(fmt % (num1,num2,num1+num2,\
                 num1,num2,num1+num2,\
                 num1,num2,num1*num2,\
                 num1,num2,num1/num2,\
                 num1,num2,num1**num2))


