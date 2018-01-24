#성적처리 클래스 작성
# class SungJuk:
#     def __init__(self, name, kor, eng, mat):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.mat = mat
#     def getTotal(self):
#         tot = self.kor + self.eng + self.mat
#         return tot
#
#
#     def getAverage(self):
#         avg = self.getTotal() / 3
#         return avg
#
#
#     def getGrade(self):
#         grdlist = 'FFFFFDCBAA'
#         var = int(self.getAverage() / 10)
#         grd = grdlist[var]
#         return grd

# sj=SungJuk('지현',99,99,99)
# print(sj.getTotal())
# print(sj.getAverage())
# print(sj.getGrade())


class SungjukV0:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

class SungJukService:
    def getTotal(self,sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self,sj):
        avg = self.getTotal() / 3
        return avg

    def getGrade(self,sj):
        grdlist='FFFFFDCBAA'
        var = int(self.getAverage()/10)
        grd = grdlist[var]
        return grd

sjsrv = SungJukService()
sj1 = SungjukV0('지현',99,98,97)
print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)
print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))
print(sjsrv.getGrade(sj1))
