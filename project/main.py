# import project.v3.main
# sjv3= project.v3.main.SungJukV3Main()

from project.v3.main import SungJukV3Main
sjv3 = SungJukV3Main()


while True:
    sjv3.displayMenu()
    sjv3.selectMenu()
