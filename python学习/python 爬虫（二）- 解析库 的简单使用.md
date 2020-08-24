当我们在获取到网页相应内容的时候， 就会使用去解析它 过滤得到想要的内容

1. 正则re

2. lxml 库

3. Beautiful Soup

4. pyquery

5. JsonPath 

# 示例响应内容

http://quotes.toscrape.com/ 截取部分内容， 以下所有例子将以这个响应内容来示范， 假设响应的内容字符串 定义为一个变量 content

# 一、正则re

使用python 中内置的模块 re正则模块

如解析页面 上所有的名人的名字：

```Python
import re
pat = re.compile('<small class="author" itemprop="author">(.*?)</small>')
print(pat.findall(content))


```

输出：['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']

# 二、lxml库

lxml 支持xpath 的解析方式，那什么是xpath解析呢？

>> XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。 [xpath 解析方式]([https://www.runoob.com/xpath/xpath-syntax.html](https://www.runoob.com/xpath/xpath-syntax.html))

同样使用上面的例子，首先需要安装 lxml库

```Python
from lxml import etree

html = etree.HTML(content)
authors = html.xpath("//small[@class='author']//text()")
print(authors)
```



# 三、Beautiful Soup

>> BeautifulSoup也是Python的一个HTML或XML解析库，最主要的功能就是从网页爬取我们需要的数据。

首先需要安装   BeautifulSoup 解析器 `pip install beautifulsoup4`

```Python
from bs4 import BeautifulSoup

soup = BeautifulSoup(content,"lxml")
authors = soup.select('small.author')
for author in authors:
    print(author.get_text())
```

# 四、pyquery

pyquery语法与前端 jQuery的用法几乎一样

```Python
from pyquery import PyQuery as pq

doc = pq(content)
authors = doc('small.author')
for author in authors.items():
    print(author.text())
```

# 五、[JsonPath](https://goessner.net/articles/JsonPath/)

会使用jsonpath的地方 ， 一般响应的内容  是json数据 。

语法：

| **XPath**              | **JSONPath**                           | **Result**                                                   |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------ |
| `/store/book/author`   | `$.store.book[*].author`               | the authors of all books in the store                        |
| `//author`             | `$..author`                            | all authors                                                  |
| `/store/*`             | `$.store.*`                            | all things in store, which are some books and a red bicycle. |
| `/store//price`        | `$.store..price`                       | the price of everything in the store.                        |
| `//book[3]`            | `$..book[2]`                           | the third book                                               |
| `//book[last()]`       | `$..book[(@.length-1)]` `$..book[-1:]` | the last book in order.                                      |
| `//book[position()<3]` | `$..book[0,1]` `$..book[:2]`           | the first two books                                          |
| `//book[isbn]`         | `$..book[?(@.isbn)]`                   | filter all books with isbn number                            |
| `//book[price<10]`     | `$..book[?(@.price<10)]`               | filter all books cheapier than 10                            |
| `//*`                  | `$..*`                                 | all Elements in XML document. All members of JSON structure. |

这里使用  一段 json 数据

我们来获取 所有的作者 和 所有价格

```Python
import jsonpath
import json

json_str = '''
{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
'''

jc = json.loads(json_str)

jp = jsonpath.jsonpath(jc, '$..author')
print(jp)
jp = jsonpath.jsonpath(jc, '$.store..price')
print(jp)
```

输出：

['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']

[8.95, 12.99, 8.99, 22.99, 19.95]

