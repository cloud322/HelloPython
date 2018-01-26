#python 자료규조
#List: sequence 자료구조를 사용
#sequence :순서가 있는 데이터 구조 의미
#리스트 , 투플,레인지,문자열 등ㅇ이 sequence

#python 에서 자료구조를 의미하는 접미사를 변수명에 사용
list1_list = []
list2_list = [1,2,3,4,5]
list3_list = ['a','b','c']
list4_list = ['a','b','c',1,2,3,4,5]

print(1 in list1_list)
print(1 not in list1_list)

print(len(list2_list))

msg= 'hello world!!!!!!'
#연결연산
print(list1_list+list2_list)
#반복연산
print(list2_list*2)
#요소의 특정값 참조 : index 사용
print(msg[4], msg[9])
print(list2_list[2])

#요소값 변경 index,= 사용

list2_list[2] = -3
print(list2_list)

socsec=[1,2,3,4,5,6,1,2,3,4,5,6,7]
if socsec[6]==1:
    print('M')
else:
    print('F')

for i in range(0,6):
    print(socsec[i], end=' ')

#특정범위내 요소들을 추출할때는 슬라이스를 사용 [i:j]
print(socsec[0:5])
print(socsec[:6])
print(socsec[6:]) #생년월일제외나머지
print(socsec[:]) #모두

print(socsec[0:6:2])    #홀수자리만
print(socsec[::-1]) #역순

print(socsec[0:100:2])
# print(socsec[100])  #IndexError: list index out of range

#리스트관련 통계함수
print(sum(list2_list))
print(min(list2_list))
print(max(list2_list))

#리스트가 주어지면 이것의 중간위체에 잇는 요소값을 출력

import math
import statistics
list = [1,2,3,4,5]
size = len(list)
mid = int(size/2)
print(list[mid])
print(list[mid-1:mid+1])

def listcenter(list):
    size = len(list)
    mid = int(size / 2)
    if size%2 ==0:
        print(list[mid - 1:mid + 1])
    else:
        print(list[mid])

listcenter([1,2,3])
listcenter([1,2,3,4])

#list 조작함수
#요소추가 append
list = [1,2,3,4,5,]
list.append(9)
list.append(8)
print(list)

#요소추가 insert
list.insert(6,7)
print(list)

#요소제거 remove    욎쪽부터
list.remove(9)
print(list)

#요소제거 pop
list.pop(5)
print(list)
list.pop()      #마지막요소
print(list)

#모두제거
list.clear()
print(list)

#####튜플 Tuple
#리스트 자료구조와 유사하지만 한번 입력한 자료는 변경 불가
#즉 요소추가는 가능 /수정삭제 불가능
#튜플은 () 이용
#튜플 생성시 단일 요소는 요소뒤에 ,를 추가

t=[1,2,3]   #리스트
t=(1,2,3)
t = (1,'a',True)
t=(1)       #숫자
t=(1,)      #단일요소로 구성된 튜플

days = ('일','월','화','수','목','금','토')
print(days)     #요일을 튜플로 정의하고 출력

print(days[3])
print(len(days))
print(days[3:])     #슬라이스

# days[3] = 'wed'     #튜플 값변경 불가!


#####집합 set
#저장된 데이터를 순서에따라 관리하지 않고
#중복을 허용하지 않는 자료구조
#집합은 {} 을 이용
#집합의 개념에 따라 합 교 차집합이 지원

t=[1,1,1,1]
print(t)
t=(1,1,1,1)
print(t)
t={1,1,1,1}
print(t)

t=[1,1,1,3,5,6,7,3,3,2,5,7,8,9]
print(t)
t =set(t)       #리스트를집합으로변환
print(t)

#집합 정의
#1월중 교육받는 날을 집합으로 정의
edu = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 }
동물 = {'사자', '늑대','호랑이','얼룩말'}
육상동물= {'기린','여우','사슴'}
해상동물={'아기상어','엄마상어','아빠상어'}
조류={'새','비둘기','부엉'}

print(len(동물))      #길이
print('여우'in 조류)      #검색 in 연산자
print('여우'in 육상동물)      #검색 in 연산자
# print(동물[2])      #index 연산 : 3번쨰 동물은

print(육상동물.union(해상동물))         #합집합
print(육상동물|해상동물)                #합집합

새로운동물 =육상동물|해상동물
print(새로운동물.intersection(해상동물))#교집합
print(새로운동물&해상동물)              #교집합

print(새로운동물.difference(해상동물))  #차집합
print(새로운동물-해상동물)              #차집합

print(새로운동물.symmetric_difference(해상동물)) #대칭차집합
print(새로운동물^해상동물)

#집합에서 제공하는 메서드
동물.add('인간')
print(동물)
동물.discard('인간')
print(동물)

동물.add('인간')
print(동물)
동물.remove('인간')
print(동물)

동물.add('인간')
print(동물)
동물.pop()
print(동물)
동물.clear()
print(동물)

###패킹 언패킹
#패킹 packing : 여러 데이터를 변수 하나에 묶어 담기
#언패킹unpacking : 변수에 담긴 데이터를 여러 변수에 풀어 놓기

numbers = (1,2,3,4,5)   #튜플생성(packing)
a,b,c,d,e = numbers     #튜플에 저장된 데이터를 언패킹(unpacking)
print(c)

numbers = 1,2,3,4,5     #패킹시 () 생략가능
# x,y,z = numbers         #unpacking 시 데이터수 = 변수수 일치해야함
x,y,*z = numbers         #unpacking 시 변수갯수 불일치시 처리방법
print(z)

a,b,c = 1,2,3 #변수 초기화 패킹 언패킹 사용


#연습문제
# x=[1,2,3,4,5,6,7,8,9]
#
# print(x)
# x.append(10)
# print(x)
# x.extend([11,12])

def myRange(start,end,hop=1):
    retVal =start

    while retVal <=end:
        yield retVal
        retVal += hop
hap = 0
for i in range(1,5,2):      #결과 : 9 #종료값이 포함된 range 함수작성
    hap+=i                  #결국 리스트형태의 갑이 출력
print(hap)


def myRange2(start,end,hop=1):
    retVal =start

    while retVal <=end:
        # yield retVal
        # return retVal ??   #중간 계사결과를 출력 또는 처리
        yield retVal        #실행중에 계산된 값은 generator 타입에 저장해둠
        retVal += hop


myRange2(1,5,2)
a= myRange2(1,5,2)      #yield 로넘긴 데이터는 순환 형식의 generator 타입 생성
print(a)

print( next(a))             #generator 타입에 저장된 값은 literator 형식으로 다룰 수 있음
print( next(a))             #literator 는 리스트에 저장된 객체를 하나씩 순환하며
print( next(a))             #하나씩 꺼내 사용하는 자료구조

for i in a:
    print(i)