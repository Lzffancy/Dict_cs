"""
dict_client
author:fancy
email:
date:20210121
"""


class Handle():
    def do_regis_c(self):
        pass

    def do_login_c(self, file_name):
        pass

    def do_quer_c(self, file_name):
        pass

    def do_exit_c(self):
        pass

class View():
    def __init__(self):
        self.handle = Handle()
    def menu01(self):
        menu01 = '1'
        print("====welcome to online_dict ====")
        print("1.register\n2.login\n3.exit\n")
        print("=============================")
        select =input("01,input your choice:")
        self.select(menu01,select)

    def menu02(self):
        menu02 = '2'
        print("===========Qurey=============")
        print("1.find word\n2.history\n3.exit\n")
        print("=============================")
        select = input("02,input your choice:")
        self.select(menu02,select)

    def select(self,menu,select):
        if menu == '1':
            if select == '1':
                if self.handle.do_regis_c():
                   self.menu02()
                else:
                   print("name already used")
                   self.menu01()
            elif select == '2':
                if self.handle.do_login_c():
                   self.menu02()
                else:
                   print("incorect name or password")
                   self.menu01()
            elif select == '3':
                pass
            else:
                print("not find select",select)
        elif menu == '2':
            if select == '1':
               self.do_quer_c('')
               self.menu02()
            elif select == '2':
                pass
                self.menu02()
                pass
            elif select == '3':
                self.menu01()
            else:
                print("not find select",select)
        else:
            print("not find")


    def main(self):
        while 1:
            self.menu01()

if __name__ == '__main__':
    v = View()
    v.main()