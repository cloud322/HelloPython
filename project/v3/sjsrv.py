
class SungJukService:

    sjdb=[] #성적데이터 저장하는 리스트
    #[(no,n,k,e,m,t,a,g,r),(no,n,k,e,m,t,a,g,r),(no,n,k,e,m,t,a,g,r)]

    #성적처리 총점 평균 학점 계산
    def computeSungJuk(self, sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        grd_list = 'FFFFFDCBAA'
        var = int(sj.avg / 10)
        sj.grd = grd_list[var]

    #성적데이터 추가
    def addSungJuk(self,sj):
        self.computeSungJuk(sj)
        sj.sjno = len(self.sjdb)+1
        self.sjdb.append(sj)    #리스트에 성적데이터 추가
        print(sj.to_str())      #추가된 성적데이터확인

    #전체 성적데이터조회
    def getSungJuk(self):
        # for sj in self.sjdb:
        #     print(sj.to_str())
        str_list = []
        for sj in self.sjdb:
            str_list.append(sj.to_str_list())
        return str_list

    def getOneSungJuk(self, no):
        result = ''
        for sj in self.sjdb:        #sjdb 에서 성적데이터를 하나씩순환
            if sj.sjno == no:       #만일 학생번호와 차즌 번호가 일치하면
                result = sj.to_str()
                break
        return result

    def modifySungJuk(self, sj):
        self.computeSungJuk(sj)                 #재개산
        self.sjdb[int(sj.sjno)-1]=sj            #성적데이터수정
        return self.sjdb[int(sj.sjno)-1].to_str #수정된 데이터 확인
    
