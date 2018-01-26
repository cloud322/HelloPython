#qna8 qna10 qna11 qna12 qna17  qna18 qna19 qna20
#함수 이름짓기
#파스칼 표기법 : 첫 letter 대문자로 JoinMember
#카멜 표기법 : 첫 letter 소문자 joinMember
#스네이크표기법 : 소문자 _ 기호이용 join_member
#헝가리안 표기 : 자료형을 의미하는 접두사 이용 strName

# #8
# def compareroom(w,h,p):
#     return p/(w*h)
#
# roomA =compareroom(2.5,3,27)
# roomB =compareroom(2,4,30)
#
# if roomA<roomB:
#     print('a')
# else:
#     print('B')
#
# #10
# def computeProfit():
#     c=int(input('뷸변'))
#     v=int(input('가변'))
#     s=int(input('잉여'))
#
#     return (c+v)/s
#
# print(computeProfit())
#
# def getExRate(country):
#     rate=0
#     if country == 'US':
#         rate =1070
#     elif country == 'EU':
#         rate =1300
#     return rate
#
#
# buyUS = 780 * getExRate('US')
# buyEU = 650*getExRate('EU')
# if buyUS > buyEU:
#     print('buy EU')
# else:
#      print('buy US')
#
# #12
#
# def runRadi(radius):
#     pi =3.141592
#     return radius*pi
#
# studentA = runRadi(100)
# studentB = runRadi(90)
#
# print('A는 B 보다 %d 만큼 더 뜀' % (studentA-studentB))
#
# #17
#
# def intCal():
#     num1 = int((input('num1')))
#     num2 = int((input('num2')))
#     fmt = '%d+%d=%d \n %d+%d=%d \n'
#     fmt += '%d*%d=%d \n %d/%d=%d \n'
#     fmt += '%d**%d=%d \n'
#     print(fmt % (num1,num2,num1+num2,\
#                  num1,num2,num1+num2,\
#                  num1,num2,num1*num2,\
#                  num1,num2,num1/num2,\
#                  num1,num2,num1**num2))
#
# intCal()
#
# #18
# def computeTax():
#
#     tax=0
#     isMarried = input('(y/n)')
#     if isMarried.lower() == 'y':
#         print('Married')
#         salary = int(input('salary'))
#         if salary < 3000:
#             tax= salary * 0.1
#         else:
#             tax = salary * 0.25
#     elif isMarried.lower() == 'n':
#         print('NOT Married')
#         salary = int(input('salary'))
#         if salary < 6000:
#             tax=salary * 0.1
#         else:
#             tax=salary * 0.25
#     else:
#         print('only Y or N')
#     fmt = ' 결혼여부 : %s, 연봉 : %d, 세금 : %.2f'
#     print(fmt % (isMarried, salary, tax))
#
# computeTax()
#
#
#
#
# #19윤년
#
# def isLeapYear():
#     year = int(input('윤년 여부 알고싶은 년도 입력'))
#     isleap = '윤년아님'
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         isleap = '윤년'
#     print('%d는 %s' %(year,isleap))
#
# isLeapYear()
#
# #20
# import random
# def lotto():
#     lotto = str(random.randint(100,999))
#     lucky = input('번호입력')
#     match = 0
#     prize = '다음에'
#
#     for i in [0, 1, 2]:
#         for j in [0, 1, 2]:
#             if (lucky[i] == lotto[j]):
#                 match+=1
#     if match ==3: prize = '1등'
#     elif match == 2: prize = '2등'
#     elif match == 1: prize = '3등'
#     print(lucky,lotto,prize)
#
# lotto()


#30

