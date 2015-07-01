#!/usr/bin/python
#-*-coding:gbk

import sys
import os
import pdb

'''
ȫ��/���ת��
http://www.pythonclub.org/python-scripts/quanjiao-banjiao
'''
def strQ2B1(ustring):
    '''���ַ���ȫ��ת���'''
    rstring = ""
    ustring = ustring.decode("gbk","ignore")
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring.encode("gbk","ignore")

def strB2Q(ustring):
    '''���ַ������תȫ��'''
    rstring = ""
    ustring = ustring.decode("gbk","ignore")
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code<0x0020 or inside_code>0x7e: 
            rstring += uchar
        if inside_code==0x0020:
            inside_code=0x3000
        else:
            inside_code+=0xfee0
        rstring += unichr(inside_code)
    return rstring.encode("gbk","ignore")

