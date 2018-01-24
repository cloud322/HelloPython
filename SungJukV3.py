name_list = []
kor_list = []
eng_list = []
mat_list = []
tot_list = []
avg_list = []
grd_list = []

print('--성적처리프로그램V3--')

while True:
    idx= len(name_list) #인덱스지정

    name_list.append(input('name??'))
    kor_list.append(int(input('kor??')))
    eng_list.append(int(input('eng??')))
    mat_list.append(int(input('mat??')))


    tot_list.append(kor_list[idx] + eng_list[idx] + mat_list[idx])
    avg_list.append(tot_list[idx]/3)
    grd_list.append(avg_list[idx])

    fmt = '%s %d %d %d %d %.2f %s'
    print(fmt %(name_list[idx],kor_list[idx],eng_list[idx],mat_list[idx],tot_list[idx],avg_list[idx],grd_list[idx]))

    is_exit = input('계속할거??(y/n)')
    if is_exit =='n':
        idx+=1
        print(idx,'명의 학생성적 처리 했습니다')
        break
