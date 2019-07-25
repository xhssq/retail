import xlrd
import numpy
#comments = []
def extract(inpath):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    print(nrows)
    ncols = table.ncols  # 获取列号
    comments = open(r"result.txt","w",encoding='utf-8')
    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result = alldata[2]  # 取出表中第1列数据
        #comments.append(result)
        print(result)
        comments.write(result)
inpath = 'fulian4Data.xlsx'  # excel文件所在路径
extract(inpath)
