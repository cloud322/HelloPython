import sys
from . import sjsrv,sjvo

class SungJukV3Main:


    sjsrv=sjsrv.SungJukService()

    #메뉴표시
    def displayMenu(self):
        str_list =[]
        str_list.append(" -= 성적 처리 프로그램 v2 =- \n")
        str_list.append("-----------------------\n")
        str_list.append(" 1 : 새로운 성적데이터 추가 \n")
        str_list.append(" 2 : 전체 성적데이터 조회 \n")
        str_list.append(" 3 : 성적데이터 상세 조회 \n")
        str_list.append(" 4 : 성적데이터 수정 \n")
        str_list.append(" 5 : 성적데이터 삭제 \n")
        str_list.append(" 0 : 성적처리프로그램 종료 \n")
        str_list.append("-----------------------\n")
        str_list.append("실행할 작업을 선택하세요 >> ")

        print(''.join(str_list))

    #메뉴에떄른 함수정의
    def newSungJuk(self):
        str_list = []
        str_list.append("\n\n추가할 석적데이터를 입력")
        str_list.append("\n데이터 입력순서는 이름/국어/영어/수학 ")
        str_list.append("\n예? 지현 99 99 99")
        print(''.join(str_list))
        n,k,e,m =input('').split()
        #성적데이터를 한줄에서 공백으로 구분해서 입력받음

        sj = sjvo.SungJuk(n,int(k),int(e),int(m))

        #성적객체를 추가함
        self.sjsrv.addSungJuk(sj)
        print('\n성적 데이터가 성공적으로 추가!!\n\n')

    def showSungJuk(self):
        str_list =[]
        str_list.append('\n\n-= 전체데이터 출력 =- \n')    #리스트형태로 결과가 return 된것을 for 문으로 다시 하나씩 순환하며출력
        for sj in self.sjsrv.getSungJuk():
            str_list.append(sj)
        str_list.append('\n\n')

        print(''.join(str_list))


    def showOneSungJuk(self):
        no = input('\n검색할 성적번호를 입력하세요\n>> ')

        str_list = []
        str_list.append('\n\n-= 상세 성적 데이터 =-')
        str_list.append(self.sjsrv.getOneSungJuk(int(no)))
        str_list.append(('\n\n'))

        print(''.join(str_list))

    def updateSungJuk(self):
        no = input('\n수정할 성적번호를 입력하세요\n>> ')

        str_list = []
        str_list.append("\n\n수정할 석적데이터를 입력")
        str_list.append("\n데이터 입력순서는 이름/국어/영어/수학 ")
        str_list.append("\n예? 지현 99 99 99")

        print(''.join(str_list))

        n, k, e, m = input('').split()
        sj = sjvo.SungJuk(n, int(k), int(e), int(m))
        sj.sjno = int(no)
        self.sjsrv.modifySungJuk(sj)
        print('수정 완료')



    def deleteSungJuk(self):
        no = input('\n삭제할 성적번호를 입력하세요\n>> ')
        self.sjsrv.removeSungJuk(int(no))
        print('삭제 성공')
    def exitSungJuk(self):
        sys.exit()

    #파이선자료구조중 dictionary 이용
    #메뉴분기시 실행할 함수를 객체형태로 저장
    menus = {'1':newSungJuk,'2':showSungJuk,'3':showOneSungJuk,'4':updateSungJuk,'5':deleteSungJuk,'0':exitSungJuk}

    #메뉴선택후 처리
    def selectMenu(self):
        menu = input('')
        # if menu ==1: newSungJuk()
        # elif menu ==2: showSungJuk()
        # elif menu ==3: showOneSungJuk()
        # elif menu ==4: updateSungJuk()
        # elif menu ==5: deleteSungJuk()
        # elif menu ==0: exitSungJuk()
        self.menus[menu](self)
