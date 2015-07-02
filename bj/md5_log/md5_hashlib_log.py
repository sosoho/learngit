#!/usr/bin/python2.6 
#-*-encoding:utf-8-*-
##
# @file md5_hashlib.py
# @Synopsis  
# @author zyp 

# @version yitian.8
# @date 2015-07-02


import hashlib
import types
import datetime
import base64
import sys

log = sys.stdout

def md5_str(string):
    # check the type
    if type(string) is types.StringType:
        #create the md5 instance and generate the md5_str
        m = hashlib.md5()
        m.update(string)
        #����ʮ�����������ַ���
        return m.hexdigest()
    else:
        return ''

def base64_encode(string):
    if type(string) is types.StringType:
        return base64.encodestring(string)
    else:
        return ''

def base64_decode(string):
    if type(string) is types.StringType:
        return base64.decodestring(string) # ��ʮ������
    else:
        return ''


def md5_attr():
    #����
    #print hashlib.algorithms    #('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')    �г����м����㷨
    print >> log, "in md5_attr..."
    h = hashlib.new('md5')
    print h.digest_size         #16 ������ɢ�е��ֽڴ�С�� 
    print h.block_size          #64 The internal block size of the hash algorithm in bytes

def submit_md5():
    print >> log, "in submit_md5..."
    name = 'YT_����_yitian_����'
    time_now = datetime.datetime.now()
    time_format = time_now.strftime("%Y%m%d")
    print time_format
    str_name = "%s%s" % (name, time_format)
    pwd_name = md5_str(str_name)
    print pwd_name


def mytest_md5():
    log = sys.stdout
    print >> log, "in mytest_md5..."
    test_str = "����"
    md5_pwd = md5_str(test_str)
    print md5_pwd,len(md5_pwd)
    print "%s md5 is : %s" % ( test_str, md5_str(test_str) )
    print "[abc] is %s" % md5_str(['abc'])

def mytest_base64():
    #root_log, this_file = log_conf()
    #root_log.error(this_file + "***TEST*****")
    log_file = log_conf()
    log_file.error("***TEST IN log_file***")
    log_file.warn("****warning***")
    log_file.debug("***debug***")
    log = sys.stdout
    print >> log, "in mytest_base64..."
    test_str = "����_PKU"
    base64_pwd = base64_encode(test_str)
    print base64_pwd,len(base64_pwd)
    print "%s base64 is : %s" % ( test_str, base64_encode(test_str) )
    print "[abc] is %s" % base64_encode(['abc'])
    text_str = base64_decode(base64_pwd)
    print >> log, "%s %s" % (test_str, text_str)

# more useful log for python models
import logging
import logging.config
import os
logging.conf_path = './conf/logging.conf'
def log_conf():
    logging.config.fileConfig(logging.conf_path)
    this_file = os.path.join(os.getcwd(),__file__)
    root_log = logging.getLogger('root')
    root_log.debug(this_file + " -- root_log debug...")
    root_log.warn(this_file + "-- root_log warn...")
    #return root_log, this_file

    my_log = logging.getLogger('myfile')
    my_log.info(this_file + " -- my_log info...")
    my_log.warn(this_file + " -- my_log warn...")
    my_log.error(this_file + " -- my_log error....")    
    return my_log
if (__name__ == "__main__"):
    submit_md5()
    mytest_md5() 
    md5_attr()
    mytest_base64()
    log_conf()
   





