"""
二级菜单
"""

class View():
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
                self.menu02()
            elif select == '2':
                self.menu02()
            elif select == '3':
                pass
            else:
                print("not find select",select)
        elif menu == '2':
            if select == '1':
                pass
            elif select == '2':
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