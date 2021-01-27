在线词典

客户端
服务端


开发文档------------------------------------------

需求分析

用户可以登录和注册

可以通过基本的图形界面print以提示客户端输入。

客户端启动后即进入一级界面，包含如下功能：登录    注册    退出
注册密码加密

用户登录后进入二级界面，功能如下：查单词  历史记录   



使用技术
tcp   IO多路复用   mySQL读写
sha256+salt


tcp
```
确定网络通信协议
                 请求类型      数据参量         返回数据参量
    注册          REGISTER      (name,password)
    登录          LOGIN         (name,password)
    查询          QUER words     word
                 QUER history
    退出          EXIT     
    
响应设计: 
    注册        OK   FAIL
    登录        OK   FAIL
    查询          
    退出        OK   FAIL
```

mysql

```
确定数据库  online_dict
表结构
user    表   pr_key      name      password
dict    表   pr_key      words     means
history 表   pr_key      word      time   user_id（外键）
```



连接部分

-tcp IO多路复用网络框架 epoll

client -- sever -- mysql
         |              |

clinet --server     epoll/tcp

server --mysql

```sql
 create table user(id int primary key auto_increment,
              name varchar(128) not null,
              password varchar(128));

```











