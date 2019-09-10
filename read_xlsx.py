import xlrd  #引入模块
 
def label2class(label):
    
    global out
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

     
    nrows=worksheet.nrows  #获取该表总行数

     
    ncols=worksheet.ncols  #获取该表总列数



    for i in range(nrows):
        #循环打印每一行
        if label==worksheet.cell_value(i,0):
            object = worksheet.cell_value(i,2)
            classi = worksheet.cell_value(i,3)

            classx=worksheet.cell_value(i,4)
            print(type(classx))
            print(classx)
            t=0
            if classx=="干垃圾":
                t=1
                #print("gan")
            if classx=="湿垃圾":
                t=2
                #print("shi")
            if classx=="可回收垃圾":
                t=3
                #print("huishou")
            if classx=="有害垃圾":
                t=4
                #print("youhai")
            #print(t)
            out={"object":object,"classi":classi,"classx":classx,"t":t}
            break
    #print("没有这个货")
            
    return out     



