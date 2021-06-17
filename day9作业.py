'''
    1.打开工作簿
    2.选择选项卡
    3.获取表格数据
技术：
    1.xlrd
'''

import xlrd
# 1.打开工作簿
xs = xlrd.open_workbook(filename=r"E:\day\day09\任务\12月份衣服销售数据.xlsx", encoding_override=True)

# 2.获取表格
tab = xs.sheet_by_name("12月份各种服饰销售情况")

# 3.获取页面数据行、列数据
rows = tab.nrows  # 获取多少行数据
cols = tab.ncols  # 获取多少列数据

day_sales = []  # 每日销售额
day_volume = []  # 每日销售多少件

sales_data = {}  #字典

def dictionaries(name,y):
    #如果过有同名的上传到字典，加数
    if name in sales_data.keys():
        sales_data[name]+=y
        return 0
    #字典没有的话，新增
    sales_data[name]=y
    return 0

for row in range(rows-1):
    data = tab.row_values(row+1)  # row_values(index) 获取一整行数据，自动放到列表里
    y = (data[2]) * (data[4])
    name = data[1]

    #把数据放到字典
    status = dictionaries(name,y)

    day_sales.append(y)
    day_volume.append(int(data[4]))

i = 0  # 每次循环+1  30之后不循环
h = 0  # 求一个月销售总和
d = 0  # 求一个月卖出多少件
p = 0  # 求每日销售数量

# 求和，求平均
while i < len(day_sales):
    h = h + day_sales[i]
    d = d + day_volume[i]
    i = i+1
p = d / len(day_volume)
print("总销售额为：",int(h),"元")
print("平均每日销售量为：", int(p),"件")
print("羽绒服本月销售占比:",int((sales_data["羽绒服"]/h)*100),"%")
print("牛仔裤本月销售占比:",int((sales_data["牛仔裤"]/h)*100),"%")
print("风衣本月销售占比:",int((sales_data["风衣"]/h)*100),"%")
print("皮草本月销售占比:",int((sales_data["皮草"]/h)*100),"%")
print("T血本月销售占比:",int((sales_data["T血"]/h)*100),"%")
print("衬衫本月销售占比:",int((sales_data["衬衫"]/h)*100),"%")



