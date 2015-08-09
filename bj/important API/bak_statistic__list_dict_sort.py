#!/usr/bin/python2.6 
#coding=utf-8

import sys
import os

url_dic = {}
open_id_dic = {}
DEBUG = 0
alph = 60 # 60 ��
def statistic_by_time(filepath):
    regex='\t'
    cnt = 0
    err_cnt = 0
    with open(filepath,'r') as fp:
        for line in fp:
            cnt += 1
            line = line.strip()
            if not line:
                continue
            cols = line.split(regex)
            if len(cols) != 7:
                #print "Error line: %s" % (line)
                err_cnt += 1
                continue
            eles = cols[-3].split("##")
            if len(eles) < 2:
                open_id = eles[0]
            else:
                open_id = eles[1]
            if open_id not in open_id_dic:
                open_id_dic[open_id] = []
            #open_id_dic[open_id].append(int(cols[-2])) # time  TypeError: sequence item 0: expected string, int found
            open_id_dic[open_id].append(cols[-2]) # time �ں����ʹ�õط��� intȥ

            #print cols[5],open_id
        print "Lines Numbers : %d   ERROR LINEs : %d" % (cnt,err_cnt)

def load_file(filename):
    regex='\t'
    cnt = 0
    with open(filename,'r') as fp:
        for line in fp:
            cnt += 1
            line = line.strip()
            if not line:
                continue
            cols = line.split(regex)
            if len(cols) != 7:
                print "Error line: %s" % (line)
                continue
            url_dic[cols[0]] = url_dic.get(cols[0],0) + 1 # cols[0] ---- url
            #print cols[0]
        print "Lines Numbers : %d" % (cnt)


def delete_chongfu(filename):
    regex='\t'
    cnt = 0
    new_filename = filename + "_new"
    print new_filename
    fw = open(new_filename,'w')
    with open(filename,'r') as fp:
        for line in fp:
            #cnt += 1
            line = line.strip()
            if not line:
                continue
            cols = line.split(regex)
            if len(cols) != 7:
                print "Error line: %s" % (line)
                continue
            if cols[0] in url_dic:
                cnt += 1
            else:
                fw.write(line + "\n")
            
            #print cols[0]
        print "Lines Numbers : %d" % (cnt)
    fw.close()

def statistic_write_results(filename):
    dir_path = "/search/yapeng/check_data/lhb_zyp/out_arts"
    if not  os.path.exists(dir_path):
        os.mkdir(dir_path)
    current_path = os.path.join(dir_path,filename)
    with open(current_path,'w') as fw:
        for open_id,time_list in open_id_dic.items():
            # ����
            time_list.sort()
            fw.write(open_id + "\t" + str(len(time_list)) + "\t" + '-'.join(time_list) + "\n")

def statistic_results_group_write_old(filename):
    dir_path = "/search/yapeng/check_data/lhb_zyp/out_arts_group"
    if not  os.path.exists(dir_path):
        os.mkdir(dir_path)
    current_path = os.path.join(dir_path,filename)
    with open(current_path,'w') as fw:
        for open_id,time_list in open_id_dic.items():
            # ����
            time_list.sort()
            group_list = []
            if int(time_list[-1]) - int(time_list[0]) < alph:
                group_list.append('-'.join(time_list))
            else:
                time_list_len = len(time_list)
                start = 0
                for i in range(1,time_list_len):# [1,len)
                    if int(time_list[i]) - int(time_list[i-1]) > alph:
                        group_list.append('-'.join(time_list[start:i])) # [start,i) ���±�
                        start = i
                # �������һ��
                group_list.append('-'.join(time_list[start:i]))
            fw.write(open_id + "\t" + str(len(time_list)) + "\t" + '\t'.join(group_list) + "\n")


def statistic_results_group_write():
    file_path = "/search/yapeng/check_data/lhb_zyp/out_arts_group"
    with open(file_path,'w') as fw:
        for open_id,time_list in open_id_dic.items(): # ***** �ص� list -1 �Լ���ȡ****
            # ����
            time_list.sort()
            group_list = []
            if int(time_list[-1]) - int(time_list[0]) < alph:
                group_list.append('-'.join(time_list))
            else:
                time_list_len = len(time_list)
                start = 0
                for i in range(1,time_list_len):# [1,len)
                    if int(time_list[i]) - int(time_list[i-1]) > alph:
                        group_list.append('-'.join(time_list[start:i])) # [start,i) ���±�
                        start = i
                # �������һ��
                group_list.append('-'.join(time_list[start:i]))
            fw.write(open_id + "\t" + str(len(time_list)) + "\t" + '\t'.join(group_list) + "\n")



#ÿһ���ļ�һ��һ����ͳ�Ƶ�
def list_dir_old(dir_path):
    global DEBUG
    flag = 1
    if not os.path.isdir(dir_path):
        print "ERROR CMD -- not a dir Usage: python2.6 delete_dumple.py [FOLDER] EXP:python2.6 delete_dumple.py input_arts"
        exit(1)
    list_name = os.listdir(dir_path)
    for name in list_name:
        current_path = os.path.join(dir_path,name)
        if os.path.isdir(current_path):
            list_dir(current_path)
        elif os.path.isfile(current_path):
            print "file %s" % current_path
            if flag:
                # ����ÿһ���ļ�ͳ�ƽ��,ÿһ���
                statistic_by_time(current_path)
                # ����
                
                # ��ͳ�Ʋ�����Ľ������ ����������
                #statistic_write_results(name)
                
                # ��ͳ�Ʋ�����İ���ʱ�����Ľ������ --- ��������
                statistic_results_group_write(name)
                # ���ȫ�ֱ��� open_id_dic
                open_id_dic.clear()
            if DEBUG:
                flag = 0
        #print name


# ���е��ļ�����ͳ�Ƶ�****** �ص� dir*****
def list_dir(dir_path):
    global DEBUG
    flag = 1
    if not os.path.isdir(dir_path):
        print "ERROR CMD -- not a dir Usage: python2.6 delete_dumple.py [FOLDER] EXP:python2.6 delete_dumple.py input_arts"
        exit(1)
    list_name = os.listdir(dir_path)
    for name in list_name:
        current_path = os.path.join(dir_path,name)
        if os.path.isdir(current_path):
            list_dir(current_path)
        elif os.path.isfile(current_path):
            print "file %s" % current_path
            if flag:
                # ����ÿһ���ļ�ͳ�ƽ��,ÿһ���
                statistic_by_time(current_path)
            if DEBUG:
                flag = 0
        #print name
    # ��ͳ�Ʋ�����Ľ������ ����������
    #statistic_write_results(name)
    
    # ��ͳ�Ʋ�����İ���ʱ�����Ľ������ --- ��������
    statistic_results_group_write()
    # ���ȫ�ֱ��� open_id_dic
    open_id_dic.clear()


def main_quchong_26_27():
    print "����0��%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print "Usage: python2.6 delete_dumple.py [FILE] [FILE] EXP:python2.6 delete_dumple.py 20150726 20150727"
        exit(1)
    load_file(sys.argv[1])
    delete_chongfu(sys.argv[2])


def main_statistic_openid_timestamp():
    current_path = os.getcwd()
    print "����0��%s" % (sys.argv[0])
    if len(sys.argv) < 2:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage: python2.6 delete_dumple.py [FOLDER] EXP:python2.6 delete_dumple.py input_arts"
        exit(1)
    dir_path = os.path.join(current_path,sys.argv[1])
    list_dir(dir_path) # this is the main function
     

if __name__ == "__main__":
    '''����������������ʹ�ã���ִ��һ������ִ������һ������ִ�е������ǲ�һ����'''
    #main_quchong_26_27()
    main_statistic_openid_timestamp()
