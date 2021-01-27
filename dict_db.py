"""
dict_database
author:fancy
email:
date:20210121
"""
import pymysql


class Dict_db:
    def __init__(self):
        self.kwargs = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "database": "stu",
            "charset": "utf8"
        }
        self.connect()

    # 完成数据库连接
    def connect(self):
        #生成连接 对象
        self.db = pymysql.connect(**self.kwargs)

    # 建立游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭
    def close(self):
        #self.cur.close()
        self.db.close()

    # 注册
    def register(self,user,password):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        user_info =[user,password]
        try:
           sql = "insert into user(user,password)" \
                 "values (%s,%s)"
           self.cur.execute(sql,user_info)
           self.db.commit()
           return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return None

    # 登录
    def login(self,user,password):
        """
        :param user:  用户名
        :param password:  密码
        :return: bool
        """
        user_info = [user, password]
        sql = 'select * from user ' \
              'where user=%s and password=%s '
        self.cur.execute(sql, user_info)
        user_result = self.cur.fetchone()
        #self.db.commit()
        if user_result:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
    #user = User()
    #print(user.register("fancy3", "123456789"))
    #user.close()
