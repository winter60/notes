我们去很多网站上 去下载视频，解析出的地址 是m3u8格式视频， 使用 普通的下载方式下载就是一个m3u8文件。里面装的是一段一段的视频。一方面，不做特殊处理播放器可能播放不了，另一方面该格式可能是加密格式。使用普通的方式下载下来，基本播放不了。

网上有许多这样的方法，这里我介绍我喜欢的几种方法吧。




# 方法1：使用youtube-dl下载m3u8视频
1. 安装 youtube-dl
在python环境下，使用pip命令安装`pip install youtube-dl`, 
这里需要python环境，没有的可以百度一下。

2. 在目标位置打开终端，使用下载命令 `youtube-dl -o "名称.mp4" "https://m3u8地址" `
3. 如果有多个url地址， 可拼接成这样
```
youtube-dl -o "名称1.mp4" "https://m3u8地址1" & 
youtube-dl -o "名称2.mp4" "https://m3u8地址2" & 
youtube-dl -o "名称3.mp4" "https://m3u8地址3" & 

```


# 方法2：使用 M3U8批量下载器
来自于52pojie逍遥大神，https://www.52pojie.cn/thread-1216473-1-1.html
1. 安装该文件(目前只知道windows版)
2. 普通操作
   

 ![](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20201024_2020-10-24-18-05-50.png)
 ![](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20201024_2020-10-24-18-07-39.png)


3. 可添加多个地址和文件名一起下载
4. 也可导入配置文件下载("基本" ->  "导入配置")
    配置文件格式
    名称(或参数名),链接(或参数值)、一行一条、英文逗号分割

    例如
    希望将目录更改为D盘，下载2个文件后改为E盘，则配置内容应是
```
    #OUT,D:\
    第一个文件名,第一个链接
    第二个文件名,第二个链接
    #OUT,E:\
    第三个文件名,第三个链接
```

以上是如何下载，但可能不知道m3u8地址怎么获取。
# 如何获取m3u8地址
1. 一般方法, `document.querySelector('video').querySelector('source[src*=".m3u8"],source[type*="video/mp4"]').src;`

获取页面video元素下 source元素src为m3u8的，这里只取其中一个
2.  使用插件的方法 , Media download helper 或者

![](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20201024_2020-10-24-18-15-59.png)


![](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20201024_2020-10-24-18-16-49.png)

# 自动复制增强
对于方法1 ， 可以将这串地址加入 浏览器书签
```javascript
javascript:(function(){    var content = "";    var url = document.querySelector('video').querySelector('source[src*=".m3u8"],source[type*="video/mp4"]').src;    var title ="名称随便取";    content = "youtube-dl -o \"" + title + ".mp4\" " + "\"" + url + "\" & " ;    var aux = document.createElement("input");    aux.setAttribute("value", content);    document.body.appendChild(aux);    aux.select();    document.execCommand("copy");    document.body.removeChild(aux);})()
```

对于方法2，  ， 可以将这串地址加入 浏览器书签
```javascript
javascript:(function(){    var content = "";    var url = document.querySelector('video').querySelector('source[src*=".m3u8"],source[type*="video/mp4"]').src;    var title = "名称随便取";    content =  title + "," + url ;    var aux = document.createElement("input");    aux.setAttribute("value", content);    document.body.appendChild(aux);    aux.select();    document.execCommand("copy");    document.body.removeChild(aux);})()
```

![](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20201024_2020-10-24-18-21-46.png)

之后再将 复制好的内容粘贴到终端执行即可。
或者粘贴到方法2的配置文件中，再使用方法2的导入配置 执行。

个人使用方法记录一下（侵删）。



