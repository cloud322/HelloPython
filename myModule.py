#module 사용
# 프로그램구성하는독립적인(함수 /클래스) 단위를 각가 정의하고 관리하는 방법
#자주사용하는 일반적인 긴으은 모듈로 한번 만들어 두면
#필요할떄 마다 도입해서 활용할 수 있다
#모듈 : 관련성있는 데이터를, 함수, 클래스

#모듈사용하려면 import 명령어로
#인터프리터에게 사용여부를 알려야

#import Lab03
import math
#import random as r
from random import randint   #모듈명 아예줄여쓰기
from math import pi, sqrt #ㅊㅊ
# from math import *    #비추
import cloud
#import cloud.Hello as ch

from cloud.Hello import sayHello

#모듈 호출 할떄

# print(math.pi)
print(pi)
# print(math.sqrt(4))
print(sqrt(4))
# print(r.randint(1,10))
print(randint(1,10))

#import  모듈이름 as 별칭
#함수호출시 모듈 명까지 기술하는 것은 왠지 불편
#from 모듈명 import 함수명

#사용자가 만들 모듈을 다른 파일에서 참조하려면
#두파일이 모두 같은 위치에 있어야함 즉 프로젝트 내에서 서로 참조 하려면
#이 파일들은 같은 위치에 저장되어 있어야 함

#한편 python IDE 나 다른프로젝트에서 모듈을 참조하려면
#pythonPath 가 정의한 위치에 모듈을 저장해둔다
#python 설치위치 나 python 설치위치/Lib

#cloud.isLeapYear()

#python package
#다수의 개발자가 만든 모듈 이름이 서로 같을 경우
#python 에서는 패키지라는 개념을 이용해서 해결
# 연산자 . 를 이용해서 모듈을 계층적 디렉토리로 관리
#파이썬에서 디렉토리가 패키지로 인식하려면
#__init__.py 반드시있어야함



sayHello()