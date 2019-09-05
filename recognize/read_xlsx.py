import xlrd  #引入模块
 
def label2class(label):
    
    URL="./物体识别label返回值.xlsx"
    #打开文件，获取excel文件的workbook（工作簿）对象
    workbook=xlrd.open_workbook(URL)  #文件路径

    '''对workbook对象进行操作'''
     
    #获取所有sheet的名字
    #names=workbook.sheet_names()
    #print(names) #['各省市', '测试表']  输出所有的表名，以列表的形式
     
    #通过sheet索引获得sheet对象
    worksheet=workbook.sheet_by_index(0)
    #print(worksheet)  #<xlrd.sheet.Sheet object at 0x000001B98D99CFD0>
     
    #通过sheet名获得sheet对象
    #worksheet=workbook.sheet_by_name("")
    #print(worksheet) #<xlrd.sheet.Sheet object at 0x000001B98D99CFD0>
     
    #由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
    #sheet0_name=workbook.sheet_names()[0]  #通过sheet索引获取sheet名称
    #print(sheet0_name)  #各省市
     
    '''对sheet对象进行操作'''
    #name=worksheet.name  #获取表的姓名
    #print(name) #各省市
     
    nrows=worksheet.nrows  #获取该表总行数
    #print(nrows)  #32
     
    ncols=worksheet.ncols  #获取该表总列数
    #print(ncols) #13


    for i in range(nrows):
        #循环打印每一行
        if label==worksheet.cell_value(i,0):
            object = worksheet.cell_value(i,2)
            classi = worksheet.cell_value(i,3)
            if worksheet.cell_value(i,4)!=None:
                classx=worksheet.cell_value(i,4)
            out={"object":object,"class":classi,"classx":classx}
            break
    #print("没有这个货")
            
    return out     
    #['各省市', '工资性收入', '家庭经营纯收入', '财产性收入', ………………]
    #['北京市', '5047.4', '1957.1', '678.8', '592.2', '1879.0，…………]
    #col_data=worksheet.col_values(0)  #获取第一列的内容
    #print(col_data)

#print(label2class(10))    #通过坐标读取表格中的数据
    #cell_value1=sheet0.cell_value(0,0)
    #cell_value2=sheet0.cell_value(1,0)
    #print(cell_value1)  #各省市
    #print(cell_value2)   #北京市
     
    #cell_value1=sheet0.cell(0,0).value
    #print(cell_value1) #各省市
    #cell_value1=sheet0.row(0)[0].value
    #print(cell_value1)  #各省市

