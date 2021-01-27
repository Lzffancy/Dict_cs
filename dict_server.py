"""
dict_server
author:fancy
emil:
date:20210121
"""

from socket import *
from multiprocessing import Process
import sys, os, time
from dict_db import Dict_db



class Handle:
    def __init__(self, connfd, addr):
        self.connfd = connfd
        self.addr = addr
        self.db = Dict_db()

    def requset_decode(self):
        # 解协议,区分type
        while 1:
            data = self.connfd.recv(1024).decode()
            print(data, self.addr)
            temp = data.split(" ")
            if not data or data == "EXIT":
                print("client exit", self.addr)
                break
            elif temp[0] == "REGISTER":
                self.do_regis_s(temp[1],temp[2])
            elif temp[0] == "LOGIN":
                self.do_login_s(temp[1],temp[2])
            elif temp[0] == "QUER":
                self.do_quer_s(temp[1])

    def do_regis_s(self,name,password):
        # if not
        self.connfd.send(b'FAIL')
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
        self.db = Dict_db()
        #不等待子线程，子随父线程退出而退出
        super().__init__(daemon=True)

    def run(self):
        # 每个线程单独创建 数据库游标
        self.db.create_cursor()
        self.handle.requset_decode()
        self.connfd.close()
        print("process close", self.addr)


class ServerReady:
    def __init__(self):
        self.db = Dict_db()
        self.ADDR = ('0.0.0.0', 8882)
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
                self.db.close()
                self.sock_tcp.close()
                sys.exit()
            # 创建进程
            t = MultiProC(connfd, addr)
            t.start()


if __name__ == '__main__':
    sever = ServerReady()
    sever.s_activate()
