#!/usr/bin/python2.6
#coding=utf-8

from datetime import datetime
import time
import sys
import os


def statistic_by_month(file_in,outfile):
    #outfile = "%s%s" % (str(file_in) , ".csv")
    print outfile
    fw = open(outfile,'w')
    regex = '\t'
    with open(file_in,'r') as fr:
        for line in fr:
            cnt_cishu = 0
            line = line.strip()
            if not line: continue
            #days_list = []
            eles = line.split(regex)
            try:
                days = len(eles) - 2 # ���ĵ�������������Ƶ��
                open_id = eles[0] # �Ѿ�����5����ʾ
                mon_cnt = eles[1] # һ�����ܷ�����������
                for i in range(2,len(eles)):
                    cishu = eles[i].split("#",1)[1]
                    cnt_cishu += len(cishu.split('_')) # ���ĵĴ�����һ����Է����
            except:
                print line
            avg_cishu = "%.1f" % (float(mon_cnt)/cnt_cishu)
            fw.write(open_id +","+ mon_cnt +","+ str(days) +","+ str(avg_cishu) +"\n")
            #break
    fw.close()
# ����ǳ�����statistic_fawen_byopenid_2.py ֻ��ͳ�Ƶ�ָ�겻ͬ����
def main():
    current_path = os.getcwd()
    print "����0��%s" % (sys.argv[0])
    if len(sys.argv) < 3:
        print >> sys.stderr,"ERROR CMD(main_statistic_openid_timestamp)...Usage:tatistic_fawen_byopenid.py [FOLDER_SRC] [FILE_OUT]"
        exit(1)
    file_in = os.path.join(current_path,sys.argv[1])
    file_out = os.path.join(current_path,sys.argv[2])
    if not os.path.isfile(file_in):
        print >> sys.stderr, "ERROR: %s" % (file_in)
        exit(1)
    print file_in
    statistic_by_month(file_in,file_out)


if __name__ == "__main__":
    main()


