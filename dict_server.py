"""
dict_server
author:fancy
emil:
date:20210121
"""

from socket import *
from multiprocessing import Process
import sys, os, time


class Handle:
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.addr = addr

    def requset_decode(self):
        # 解协议,区分type
        while 1:
            data = self.connfd.recv(1024).decode()
            print(data, self.addr)
            temp = data.split(' ')
            # req_type = temp[0]
            # req_data = temp[1]
            # 先判断是不是退出请求,（异常退出和正常EXIT）
            if not temp or temp[0] == "EXIT":
                print("EXIT", self.addr)
                break
            elif temp[0] == "REGISTER":
                self.do_regis_s(temp[1])
            elif temp[0] == "LOGIN":
                self.do_login_s(temp[1])
            elif temp[0] == "QUER":
                self.do_quer_s()

    def do_regis_s(self):
        pass
    def do_login_s(self,file_name):
        pass
    def do_quer_s(self, file_name):
        pass
    def do_exit_s(self):
        pass


class MultiProC(Process):
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.handle = Handle(connfd, addr)
        self.addr = addr
        super().__init__(daemon=True)

    def run(self):
        self.handle.requset_decode()
        self.connfd.close()
        print("Thread close", self.addr)


class ServerReady:
    def __init__(self):
        self.ADDR = ('0.0.0.0', 65535)
        # 以下两句　也可单独封装为　一个方法 返回一个socket
        self.sock_tcp = socket(AF_INET, SOCK_STREAM)
        self.sock_tcp.bind(self.ADDR)

    def s_activate(self):
        self.sock_tcp.listen(20)
        print("Listen the port", self.ADDR)
        while 1:
            # 循环等待　客户端connect ,返回　客户端连接套接字　和　客户端地址
            try:
                connfd, addr = self.sock_tcp.accept()
                print("Connect from", addr)

            # 服务器端用键盘　退出　^D
            except KeyboardInterrupt:
                print("server exit!")
                sys.exit()
            t = MultiProC(connfd, addr)
            t.start()


if __name__ == '__main__':
    sever = ServerReady()
    sever.s_activate()
