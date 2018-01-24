#이름 국어 영어 수학 총점 평균
print('--성적처리프로그램--')
name = input('name??')
kor= int(input('kor??'))
eng = int(input('eng??'))
mat = int(input('mat??'))
tot=kor+eng+mat
avg=tot/3
grd='F'
if avg >=90:
    grd= 'A'
elif avg >=80:
    grd ='B'
elif avg >= 70:
    grd ='C'
elif avg >=70:
    grd ='D'


print(tot)
print(avg)

print('{0}, {1}, {2}, {3},{4},{5:.1f}'.format(name, kor,eng,mat,tot,avg))
print('이름=%s,국어=%d,영어=%d,수학=%d,총점=%d,평균=%.2f,학점=%s ' %(name, kor,eng,mat,tot,avg,grd))