print('--성적처리프로그램--')
name = input('name??')
kor= int(input('kor??'))
eng = int(input('eng??'))
mat = int(input('mat??'))

def getddd():
    pass
#나중에 pass - dummy code

def getTotal():
    tot = kor + eng + mat
    return tot
def getAverage():
    avg = tot / 3
    return avg
def getGrade():
    avg = getAverage()
    grd = 'F'
    if avg >=90:
        grd ='A'
    elif avg >=80:
        grd ='B'
    elif avg >= 70:
        grd ='C'
    elif avg >=70:
        grd ='D'
    return grd


tot=getTotal()
print(tot)
avg=getAverage()
print(avg)
grd=getGrade()
print(grd)

fmt ='%s %d %d %d %d %.2f %s'
print(fmt %(name,kor,eng,mat,getTotal(),getAverage(),getGrade()))

