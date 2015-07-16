#!/usr/bin/python2.6 
#-*-encoding:utf-8-*-

# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
def open_excel(file= 'test.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#����������ȡExcel����е�����   ����:file��Excel�ļ�·��     colnameindex����ͷ���������е�����  ��by_index���������
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #����
    ncols = table.ncols #����
    colnames =  table.row_values(colnameindex) #ĳһ������ 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#�������ƻ�ȡExcel����е�����   ����:file��Excel�ļ�·��     colnameindex����ͷ���������е�����  ��by_name��Sheet1����
def excel_table_byname(file= 'test.xlsx',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #���� 
    colnames =  table.row_values(colnameindex) #ĳһ������ 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():
   ''' 
   tables = excel_table_byindex()
   for row in tables:
       print row
   '''
   tables = excel_table_byname()
   for row in tables:
       print row

#thread threading mutithreading
from time import ctime , sleep
import threading

def music(func):
    for i in range(2):
        print "I was listening to %s. %s" % (func, ctime())
        sleep(4)

def move(func):

    for i in range(2):
        print "I was at %s... %s" % (func, ctime())
        sleep(5)

def my_threads():
    threads = []
    t1 = threading.Thread(target=move,args=('������',))
    t2 = threading.Thread(target=music,args=('�����ǵ���˫��',))
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print "all is over %s" % ctime()

if __name__=="__main__":
    #main()
    '''
    music('�����ǵ���˫��')
    move('������')
    print "all over %s" % ctime()�����ǵ���˫��
    '''
    my_threads()
