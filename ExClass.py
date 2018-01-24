#class
#변수와  그것과 관련된 함수를 하나의 이름으로 정의한 것

#class 정의
# class 이름
#   클래스변수
#   생성자
#   함수정의(method)

#python 에서 생성자나 메서드 정의시 암시적으로 첫번쟤 매개변수가 self로 지정되어있음
#self 는 항상 객체 자신을 가르키는 의미로 사용

#클래스 맴버변수는 생성자를 통해서 정의
#파이썬에서는 객체로 생성된 후에도 맴버변수를 추가할수 있음(비추)

class HelloPython:
    def sayHello(self):
        print('Hello hello')

print(HelloPython)
print(type(HelloPython))

# HelloPython.sayHello()
py = HelloPython()
py.sayHello()

class Animal:
    type = '동물' #클래스수준변수
    def __init__(self,name,age): #객체 자신을 가리키는 의미로 self 사용
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')

#slef =JAVA의 this
#객체선언 및 사용 : 객체명 메서드
#tiger = Animal()
tiger = Animal('',0)
print(tiger.eat())
print(tiger.type)
print(Animal.type)

tiger.name ='tiger'
tiger.age= 65
tiger.gender= 'M'

print(tiger.name)
print(tiger.age)
print(tiger.gender) #실행중 tiger 객체에 맴버변수 추가함

# zebra =Animal('얼룩',45)
# print(zebra.gender)

#클래스 상속
#class 클래스명 (부모클래스명)
#      클래스정의
class Tiger(Animal):
    def eat(self):
        print('호랑이는 고기고기')
class Zebra(Animal):
    def eat(self):
        print('호랑이는 고기고기')

t1=Tiger('호랑호랑',12)
t1.name
t1.eat()

z1=Zebra('지현',10)
z1.eat()

animals =[z1,t1]#객체지향의 다향성을 이용
for ani in animals:
    print(ani.name)
    ani.eat()
