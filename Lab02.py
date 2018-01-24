
import random
print(random.random())
print(random.randint(1,10))
print(ord('a'))
print(chr(65))

# #18
# isMarried = input('(y/n)')
# if isMarried.lower() == 'y':
#     print('Married')
#     salary = int(input('salary'))
#     if salary<3000:
#         print('tax:%d' %(salary*0.1))
#     else:
#         print('tax:%d' %(salary * 0.25))
# elif isMarried.lower() == 'n':
#     print('NOT Married')
#     salary = int(input('salary'))
#     if salary < 6000:
#         print('tax:%d' %(salary * 0.1))
#     else:
#         print('tax:%d' %(salary * 0.25))
# else:
#     print('only Y or N')
#
# #19윤년
# year =int(input('윤년 여부 알고싶은 년도 입력'))
#
# if year%4==0 and year%100 != 0 or year%400 ==0:
#     print('{0}은 윤년',year)
# else:
#     print('{0}은 윤년아님', year)




#20
lotto = input('put in Three digit number')
guess = str(random.randint(1, 1000))

print(guess)
print(lotto)



if lotto[0] == guess[0] and lotto[1] == guess[1] and lotto[2] == guess[2]:
    print('oooo')
elif lotto[0] != guess[0] and lotto[1] == guess[1] and lotto[2] == guess[2] or \
        lotto[0] == guess[0] and lotto[1] != guess[1] and lotto[2] == guess[2] or \
        lotto[0] == guess[0] and lotto[1] == guess[1] and lotto[2] != guess[2]:
    print('only 2')
elif lotto[0] != guess[0] and lotto[1] != guess[1] and lotto[2] == guess[2] or \
        lotto[0] == guess[0] and lotto[1] != guess[1] and lotto[2] != guess[2] or \
        lotto[0] != guess[0] and lotto[1] == guess[1] and lotto[2] != guess[2]:
    print('only 1')
else:
    print('none')

# lotto = str(random.randint(100, 999))
# print(lotto)
# lucky = str(input('복권 숫자 3자리를 입력하세요\n'))
#
# match = 0;
#
# if lotto[0] == lucky[0] or lotto[0] == lucky[1] or lotto[0] == lucky[2]:
#     match += 1
# if lotto[1] == lucky[0] or lotto[1] == lucky[1] or lotto[1] == lucky[2]:
#     match += 1
# if lotto[2] == lucky[0] or lotto[2] == lucky[1] or lotto[2] == lucky[2]:
#     match += 1
#
# msg = '꽝이군요! 다음 기회에!'
# if match == 3:
#     msg = '모두 일치! 상금 1백만원!'
# if match == 2:
#     msg = '2개 일치! 상금 1만원!'
# if match == 1:
#     msg = '1개 일치! 상금 1천원!'
#
# print(msg)

#21
n = int(input('?'))

if n <10 and n>=1:
    for i in range(1,20):
        print('%d*%d=%d' % (n,i,n*i))
else:
    print('only1~9')

#숫자만입력받기  문자- ASCII 코드값 ord
dan = input('출력할단')
if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
    print('구구단출력')
else:
    print('숫자만')


#22


lower = input('to UPPER')
if ord(lower[0]) >= ord('a') and ord(lower[0]) <= ord('z'):
    print(lower.upper())
else:
    print('ONLY lower')


#23
key = random.randint(1,100)
while True:
    lucky = int(input('1-100 number'))
    if key ==lucky:
        print('bingo')
        break
    elif key< lucky:
        print(' too high')
    else:
        print('too low')

