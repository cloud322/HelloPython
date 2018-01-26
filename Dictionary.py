#딕셔너리 : 매핑 자료구조
#키에 값을 연결시키는 방식으로 데이터를 다루는 방법 제공
#키는 저장된 데이터를 식별하기 위한 번호나 이름
#값은 각 키에 연결되어 저장된 데이터
#따라서 , 키만 알면 데이터를 바로 찾을 수있음
#딕셔너리는 {}  에 키:값 형태로 이용
#키:값 이 여러개 존재 할경우 , 로 구분

menu={'1':'newSungJuk', 2:'showSungjuk','abc':'modifySungJuk'} #키는 다양한 자료형 가능

book={'bookid':'1', 'bookname':'축구의역사','publisher':'굿스포츠','price':'7000'
    ,'bookid':'2', 'bookname':'축구아는여자','publisher':'나무수','price':'13000'
    ,'bookid':'3', 'bookname':'축구의이해','publisher':'대한미디어','price':'22000'
    ,'bookid':'4', 'bookname':'골프바이블','publisher':'대한미디어','price':'35000'
    ,'bookid':'5', 'bookname':'피겨교본','publisher':'굿스포츠','price':'8000'}


order={'orderid':'1', 'custid':'1','bookid':'1','saleprice':'6000','orderdate':'2007-01'}

customer={'custid':'1', 'name':'박지성','address':'영국 맨체스터','phone':'000-5000-0001'
         ,'custid':'2', 'name':'김연아','address':'대한민국 서울','phone':'000-6000-0001'
         ,'custid':'3', 'name':'장미란','address':'대한민국 강원도','phone':'000-7000-0001'
         ,'custid':'4', 'name':'추신수','address':'미국 클리브랜드','phone':'000-8000-0001'
         ,'custid':'5', 'name':'박세리','address':'대한민국 대전','phone':'000-9000-0001'}

print(book)
books_list=[]
books_list.append(book)     #생성한 딕셔너리를 배열에 저장
books_list.append(book)
books_list.append(book)
print(books_list)


#딕셔너리 처리 메서드
print('1'in book)       #딕셔너리에서 in 연산자는 key를 검색
print('bookid'in book)

print(book['bookid'])   #딕셔너리에 키로 검색
print(book['bookname'])
print(book['price'])
#print(book['pricee'])   #존재하지 안ㄶ는 키 검색시 오류
print(book.get('bookname'))
print(book.get('booknamee'))#존재하지 안ㄶ는 키 검색시 None 출력

bkname = book['bookname']   #키로 검색후 값출력
print(bkname)

print(book.get('bookid'))
book['bookid'] = 99       #키로 값 수정
print(book.get('bookid'))

print(book)
book.update({'판형':'3x4'})   #새로운 키 값 추가/수정
print(book)

del book['판형']              #기존 키 삭제
print(book)

# book.clear()                #모든키 삭제
print(book.keys())              #모든키 출력
print(book.values())            #모든값 출력
print(book.items())             #모든 키:값 을 튜플로 출력
items=book.items()       #모든 키:값을 튜플 리스트로 출력
print(list(items))


