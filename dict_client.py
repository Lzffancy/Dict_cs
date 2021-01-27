"""
dict_client
author:fancy
email:
date:20210121
"""
from socket import *
ADDR = ("127.0.0.1",8882)

class Handle():
    #建立socket,连接服务器
    def __init__(self):
        self.sock = self.__create_socket()
    def __create_socket(self):
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect(ADDR)
        return sock

    def __query_encode(self,type,data01,data02):
    #按照协议 编辑数据格式
       temp =("%s %s %s"%(type,data01,data02)).encode()
       self.sock.send(temp)
       return temp

    def do_regis_c(self,name,password):


        self.__query_encode('REGISTER',name,password)
        result = self.sock.recv(128).decode()
        if result == 'OK':
            return True
        else:
            return False
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
        print("========================%s=====")
        select = input("02,input your choice:")
        self.select(menu02,select)


    def select(self,menu,select):
        if menu == '1':
            #注册
            if select == '1':
                name = input("name:")
                password = input("password:")
                if " " in name or " " in password:
                    print("用户名密码不能有空格")
                    self.menu01()

                if self.handle.do_regis_c(name,password):
                   print(" registration success!")
                   self.menu02()
                else:
                   print("name already used")
                   self.menu01()
            #登录
            elif select == '2':
                if self.handle.do_login_c():
                   self.menu02()
                else:
                   print("incorect name or password")
                   self.menu01()
            #退出
            elif select == '3':
                pass
            else:
                print("not find select",select)
        elif menu == '2':
            #查单词
            if select == '1':
               self.do_quer_c('')
               self.menu02()
            #查历史
            elif select == '2':
                pass
                self.menu02()
            #上一级页面
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