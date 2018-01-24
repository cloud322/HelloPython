#1 print 를 이용 다음 내용 출력
print('*   *    **   ****   ****   *   *')
print('*   *   *  *  *   *  *   *  *   *')
print('*****  *    * ****   ****    * *')
print('*   *  ****** *   *  *   *    *')
print('*   *  *    * *    * *    *   *')


print('//\\* \  *  * \"    * *    * *    *   *')
#2
name = '지현'
weight =45
age = 14

print('이름{0}, 몸무계{1}, 나이{2}'.format(name,weight,age))

#3
x=1
y=1
z=1

p=3*x
3*x+y

x+y/7

3*x+y/z+2
print(p)
#4

x, y = 4, 8

print(x)
print(y)

x *= y
print(x)
print(y)
x, y = 4, 8
x -= y
print(x)
print(y)

#5
x=3
print(x+7==10)

#6
print((-32+95)*12/3)
print((3*4-((-27+67)/4))**8)
print((512+1968-432)/(2**4)+128)
print(256==2**8)
print(50+50<=10*10)
print(90!=10**2-1)

#7
x=2.5
y=-1.5
m=18
n=4
print(x+n*y-(x+n)*y)
print(m/n+m%n)
print(5*x-n/5)
print(1-(1-(1-(1-(1-n)))))

#8

print(27/(2.5*3))
print(30/(4*2))

#9

print(3+4.5*2+27/8)
print(True or False and 3<4 or not(5==7)) #T
print(True or (3<5 and 6>=2))   #T
# print(not True >'A') #X
# print(7%4+3-2/6*'Z') #x
# print('D'+1+'M'%2/3) #X
print(5.0/3+3/3)
print(53%21<45/18)
print((4<6) or True and False or False and (2>3))
print(7-(3+8*6+3)-(2+5*2))

#10

#30억 15억

잉여가치액 = 45
불변자본 = 30
가변자본 = 15

이윤율 = 잉여가치액/(불변자본 + 가변자본)
print(이윤율)

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print("This is the first sentence. \
This is the second sentence."
'This is the first line\nThis is the second line')

#11
print(1069*780)
print(1307*650)

#12
#2 3.14 r
r=100/2
rr=110/2
a=2*3.14*r
b=2*3.14*rr
print(a)
print(b)
print(b-a)

#13
print("Check out this line  ")
# print("//hello there"+'9'+7)
print("//hello there"+'9')
# print('H'+'I'+"is"+1+ "more example")
print('H'+'I'+"is"+'1'+ "more example")
# print('H'+6.5+'I'+"is"+1+ "more example")
print('H'+'6.5'+'I'+"is"+'1'+ "more example")
print("print both of us", "me Too")
print("Reverse"+ 'I'+ 'T')
# print("Nonot here is" + 1 + "more example")
print("Nonot here is" + '1' + "more example")
# print("Here is"+ 10*10)
print("Here is"+ '10*10')
# print("Notxis"+True)
print()
print
# print("How about this one"++'?'+'Huh?')
print("How about this one"+'?'+'Huh?')

#14

print(True and False and True or True)
print(True and True and True and False)
print((True and False) or (True and not False) or (False and not False))
print((2<3)or(5>2) and not(4==4) or 9!=4)
print(6==9 or 5<6 and 8<4 or 4>3)


#15
print(27/13+4)
print(27/13+4.0)
print(42.7%3+18)
print((3<4) and 5/8)
print(True and 5/8)
print(False and 5/8)
print(23/5+23/5.0)
# print(2.0+'a')
# print(2+'a')
print('a'+'b')
# print('a'/'b')
print('a' and not 'b')
# print((double)'a' / 'b')

#16
#++ -- 지원 xx
n=3
print(++n)
#print("n=="+ n)
#print(--n)
#print("n=="+n)

17
n1=int(input('첫번째정수'))
n2=int(input('두번째정수'))
print(int(n1)+int(n2),int(n1)-int(n2),int(n1)*int(n2),int(n1)/int(n2))
print('%d+%d=%d' % (n1,n2,n1+n2))
print('%d-%d=%d' % (n1,n2,n1-n2))
print('%d*%d=%d' % (n1,n2,n1*n2))
print('%d/%d=%f' % (n1,n2,n1/n2))

flag = input('(Y/N)')
if flag == 'Y':print(':)')
elif flag == 'N' :print(':(')
else:print('re')


flag = input('(Y/N)')
if flag == 'Y':

    print(':)')
    price = int(input('whats the price?'))
    if price>10000:
        print('TOO EXPENSIVE')
    else:
        print('BUY~')

elif flag == 'N':
    {
    print(':(')
    }
else:
    print('only Y or N')

print(ord('a'))
print(chr(65))
import random
print(random.random())
print(random.randint(1,10))