> 使用picgo + typora + github搭建个人图床

为什么使用这种方式？ 一个是某些图床收费 ， 这种不考虑， 另外免费的图床也不怎么稳定的，经常看见许多博客的图片显示的是破损的图标。采用这种方式不用考虑收费和容量的问题，如果仓库满了，再建一个呗(一般也用不了太大)

参考：[https://blog.csdn.net/m0_37903882/article/details/105417479](https://blog.csdn.net/m0_37903882/article/details/105417479)

# 说明

1. typroa客户端
2. 一个github账号
3. picgo客户端
4. 推荐插件（github-plus + rename-file）

网上大多数文章都有写前3点的 具体操作步骤 和配置， 我这里也就简单说说吧。

# 步骤一 ：新建github仓库获取Personal access tokens

新建好仓库后，单击头像菜单的settins->Developer settings->Personal access tokens->generate new token按钮 ->



![image-20200905181453215](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905181453215.png)

![image-20200905171700402](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905171700402.png)

保存好生成的token，配置picgo的时候会用到。

# 步骤二：配置picgo

[https://molunerfinn.com/PicGo/](https://molunerfinn.com/PicGo/ )中下载 Picgo客户端 图床设置中使用github图床，填入对应的用户名、仓库、分支和 刚刚保存的token ，对应的域名可使用下面的地址 。

![image-20200905172405554](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905172405554.png)

# 步骤三：配置typora

上传服务和路径选用picgo 客户端

![image-20200905172451558](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905172451558.png)



在typroa中右击图片 进行上传，即可

![image-20200905172643259](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200905172643259.png)



之前的图片地址就会由本地替换为在线地址，而picgo客户端的相册中就会多一张

![image-20200905172849019](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905172849019.png)



大概就是这样啦。另外再推荐两款插件。

# 推荐插件 github-plus

先说说为什么推荐这个插件吧。 

场景：在家和公司两台电脑 ， 都使用相同的配置 ，使用同一个图床仓库。而在相册中竟然看不到另一个客户端上传的，说明**没有进行同步**。

使用picgo自带的github图床 的问题就是 ，不能进行同步，github-plus就是解决这个问题的。



首先在插件设置栏进行搜索找到，github-plus，再进行安装。

![image-20200905173225945](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905173225945.png)

安装好后进行 配置参数![image-20200905173437618](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905173437618.png)

两台电脑上都这样配置好之后， 在其中一台上传了图片 ，在另一台pc上就可以使用 插件的更新进行同步了。

![image-20200905173642534](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905173642534.png)

# 推荐插件 rename-file

可以自定义图片的名称的名称，保存图片的路径 等，方便自己查找

命名规则：

- {y} 年，4位
- {m} 月，2位
- {d} 日期，2位
- {h} 小时，2位
- {i} 分钟，2位
- {s} 秒，2位
- {ms} 毫秒，3位(**v1.0.4**)
- {timestamp} 时间戳(秒)，10位(**v1.0.4**)
- {hash}，文件的md5值，32位
- {origin}，文件原名（会去掉后缀）
- {rand:<count>}, 随机数，<count>表示个数，默认为6个，示例：{rand：32}、{rand}
- {localFolder:<count>}, <count>表示层级 ，默认为1，示例：{localFolder:6}、{localFolder}

我的使用的是 时间戳+原名

![image-20200905175004513](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905175004513.png)

# 命令行工具 picgo-core [官网](https://github.com/PicGo/PicGo-Core)

我们使用typroa 也可以使用命令行 ，这样就不用时时刻刻占用GPU资源，在需要时才调用上传。并且和picgo 客户端一样，也有相应的插件。

这个[https://github.com/PicGo/Awesome-PicGo](https://github.com/PicGo/Awesome-PicGo) 项目中可以看到那些 插件 是否支持命令行，比如还有水印插件和压缩文件插件，这几个我还没试过，大家可以自行尝试。

![image-20200905180740570](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200905-image-20200905180740570.png)

