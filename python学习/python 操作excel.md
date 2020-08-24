常见读写excel 的库有以下 几个(附案例)

1. **xlwt**
2. **xlrd**
3. **xlutils**
4. **openpyxl**
5. **pandas**

# [xlwt](https://xlwt.readthedocs.io/en/latest/api.html)

主要用于对xls文件进行写入操作

```python
import xlwt

#创建workbook 
book = xlwt.Workbook()

#添加sheet页
table = book.add_sheet('Over', cell_overwrite_ok=True)
sheet = book.add_sheet('测试表')
print(type(table))
print(table)

print(type(sheet))
print(sheet)
#写入 b2单元格内容
sheet.write(1,1, '你好啊')

# 设置字体样式
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = '楷体'
font.bold = True
style.font = font

table.write(0,0, '世界吗？', style)
book.save(filename_or_stream='xlwt写入xls文件内容.xls')
```



# [xlrd](https://xlrd.readthedocs.io/en/latest/api.html)

主要用于对xls文件进行读取

```python

import xlrd
#打开workbook
data = xlrd.open_workbook('xlwt写入xls文件内容.xls')
#所有sheet页 名称
print(data.sheet_names())
table0 = data.sheets()[0]
table = data.sheet_by_index(0)

# 获取sheet页
table = data.sheet_by_name('Over')

# 已有内容的行数和列数
nrows = table.nrows
ncolumns = table.ncols
print(type(nrows), nrows)
print(type(ncolumns), ncolumns)

# 获取单元格内容的几种方式
print(table.row_values(0))

for row in range(nrows):
    print(table.row_values(row))

print(table.cell(0,0).value)
print(table.row(0)[0].value)
```





# [xlutils](https://xlutils.readthedocs.io/en/latest/)

对xlrd 和 xlwt进行了封装 ， 在使用前会先下载这两个模块的依赖

```python
import xlwt,xlrd
from xlutils.copy import copy

data = xlrd.open_workbook('xlwt写入xls文件内容.xls', formatting_info=True)
excel = copy(wb=data)#将xlrd对象拷贝转化为xlwt对象
excel.save('拷贝文件.xls')
```



# [openpyxl](https://openpyxl.readthedocs.io/en/stable/api/openpyxl.html)

不仅对xls可读写，也可对xlsx 进行处理

```python
import openpyxl
# 创建workbook
data = openpyxl.Workbook()
# 添加sheet页
data.create_sheet('first')

# 获取激活页(默认第一页)
table = data.active
#写入单元格内容
table.cell(1,1, '值')
# 保存文件
data.save('openpyxl写文件.xlsx')


# 打开文件 获取workbook
data = openpyxl.load_workbook('openpyxl写文件.xlsx')
# 获取sheet页
table = data.get_sheet_by_name('Sheet')
nrows = table.rows
ncols = table.columns

print(type(nrows))

for row in nrows:
    print(row)
    line = [col.value for col in row]
    print(line)

print(table.cell(1,1).value)

```

# [pandas](https://www.pypandas.cn/docs/reference.html)

pandas 主要用于数据分析 ，在 对excel 操作方面也是非常方便

```python
import numpy as np
import pandas as pd

# 生成数据
df = pd.DataFrame(np.random.randn(10, 4))

# 写入 excel
df.to_excel('foo.xlsx', sheet_name='Sheet1')

# 读取excel
df2 = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(df2)
```

