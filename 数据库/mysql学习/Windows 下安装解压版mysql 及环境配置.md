> 本文将介绍如何在windows下安装配置mysql

1. 下载安装包
2. 配置ini文件并初始化
3. 创建mysql服务，启动关闭服务
4. 设置密码
5. 创建数据库

# 下载安装包

去官网下载社区版的版本，https://dev.mysql.com/downloads/mysql/

我这里使用的是5.7版本， 5.8有一些新的特性和用法，根据需要进行安装。

![image-20200905075343736](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905075343736.png)

选择对应的版本

![image-20200905075518656](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905075518656.png)

下载到本地解压。

# 配置ini文件并初始化

解压后在目录下新建my.ini文件，内容如下

![image-20200905080426957](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905080426957.png)

```ini
[mysql]
default-character-set=utf8

[mysqld]
port = 3306 
basedir=d:\TD\mysql-5.7.28-winx64\
datadir=d:\TD\mysql-5.7.28-winx64\data 
max_connections=200 
character-set-server=utf8 
default-storage-engine=INNODB
explicit_defaults_for_timestamp=true
```

**basedir 和datadir 配置成自己对应的目录**，其中，需要在当前目录新建一个 名为data的空文件夹

接下来以进入 bin目录，打开管理员命令行窗口， 输入命令`mysqld --initialize-insecure --user=mysql` 初始化，

接着 `mysqld install` 命令安装服务，

这样就可以 使用 `net start mysql` 和 `net stop mysql` 来启动和关闭mysql服务了。

# 设置密码

在命令行窗口 使用`mysql -u root -p`就可以进入mysql了， 默认没有密码。

```powershell
mysql>set password =password('123');
mysql>flush privileges;
```

下次打开的就需要输出密码了



# 创建数据库

在命令行输入 `show databases`可以看到当前用户有哪些数据库

![image-20200905083117581](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905083117581.png)

输入`create database 自己的库名 default charset=utf8mb4 `就可以创建 数据库了， 此时再`show databases`就可以看到多了一个数据库。

![image-20200905083900015](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905083900015.png)

使用`use 库名` 就可以在当前 进行 表的增删查改了。

另外，删除库的命令是`drop database 库名`

本文不对表相关查询 进行展开。

