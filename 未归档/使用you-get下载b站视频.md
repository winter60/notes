



![image-20200912170212431](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912170212431.png)

# 为什么想要下载到本地

当我在看b站视频学习的时候，有的地方听不懂需要，反复听，这就需要重新拖动滚动条到不懂的位置或者有些视频需要反复多次看， 在线看就有些不方便。如果下载到本地的话，使用potplayer播放，就可以多开文件播放，加速播放（可超过2倍速），反复观看不占流量。

# 使用何种方式下载视频

网络上有很多关于如何从B站上下载视频的方法

我使用过的就有 

1. 唧唧
2. B站视频下载工具
3. bilibili视频下载器
4. 解析(嗅探)网址后下载(单个文件)

在写这篇文章的时候，1和2方法 好像不能用了(不知道有还能用不)。方法3还可以。方法4是一个思路，可以使用很多 视频嗅探工具（如维棠 、硕鼠、idm, ndm等） 解析出地址后，直接下载。

想要尝试的朋友们可自行搜索，下面我更喜欢命令行的方式下载 。

# 使用you-get 下载视频

使用这种方式 下载的优点是

1. 方便简洁
2. 可支持批量下载
3. 可选择格式(各种清晰度)
4. 下载b站 使用dash-flv的 速度会很快

## 步骤1：安装you-get

[官网地址](https://github.com/soimort/you-get)

有python环境的可直接使用`pip3 install you-get` 安装，其他的请参考官网

安装完后，使用方法很简单 在命令提示符输入: `you-get url地址`就可以了

参数说明：



--info`/`-i:  查看 可下载的清晰度和格式

--format: 使用 哪种格式下载

--playlist: 下载合辑

--debug: 当下载出错时可查看原因



## 步骤2: 安装ffmpeg

[官网下载地址](https://www.ffmpeg.org/download.html)

用于合并音视频，下载安装或解压后 ， 把bin目录的路径放入到环境变量

![image-20200912165741581](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912165741581.png)



**这一点很重要，不然下载后的视频和音频是分开的。当系统能找到 ffpmeg时，下载完后会自动合并音视频流。**

![image-20200912165847101](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912165847101.png)

# 步骤3: 开始下载

下面演示下下载b站上一个 视频 ， [高等数学](https://www.bilibili.com/video/BV1Eb411u7Fw)

在命令提示符中，切换到下载目录

## 下载单个视频

```powershell
you-get https://www.bilibili.com/video/BV1Eb411u7Fw
```

![image-20200912164713781](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912164713781.png)

上面没有带任何参数 ， 默认格式 为mp4 ，使用dash

我们来看一下他支持哪些清晰度和格式下载

![image-20200912165031786](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912165031786.png)

可以选择 不同的格式来进行下载 ，相应的其格式和文件和清晰度会有所变化。

只需要 带上参数 `--format=xxx`即可， 经测试 使用 dash-flv开头的速度会快一些。



## 下载合辑

前提是本身是合辑视频， 那么只需在 地址前加一个 `--playlist`参数即可

![image-20200912165527117](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200912_image-20200912165527117.png)



快速、高效、简洁，over.

you-get 还支持很多其他网站视频 的下载， 如芒果、企鹅、爱奇艺等主流视频网站(非付费视频)，各位朋友们可自行尝试。