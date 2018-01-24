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