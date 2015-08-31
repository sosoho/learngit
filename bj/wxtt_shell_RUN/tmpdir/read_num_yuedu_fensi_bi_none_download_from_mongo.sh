#!/bin/bash
#-*-coding:gbk

#下载类别体系以及对应的关键词和账号
#mysql -h 10.134.78.228 -udarrenan -pdarrenan db_personalized_reading --default-character-set=gbk -e "select id,first_level_topic,\
#	second_level_topic,third_level_topic,type,keyword_account,level,info from t_list_page" > t_list_page.tmp
#awk 'NR<10{print $0}' t_list_page.tmp > t_list_page.txt
#dos2unix t_list_page.txt
#rm -f t_list_page.tmp


#mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.count();" > t_zyp.tmp
#mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.find().limit(10).forEach(printjson);" > t_zyp.tmp
# the second one can select from mongo
#mongo 10.134.44.83:27026/WeiXinRecom  -eval "db.weixin_articles.find({"status":0}).limit(2).forEach(printjson);" > t_zyp.tmp
#awk 'NR>2{print $0}' t_zyp.tmp > t_zyp.txt
#dos2unix t_zyp.txt
#rm -f t_zyp.tmp 


# db.weixin_articles.find({"page_time":{$gt:1439135999},"page_time":{$lte:1439395199}},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).sort({"account_openid":1}).count()
FILENAME=read_num_yuedu_fensi_bi
#CMD="db.weixin_articles.find({},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).sort({"account_openid":1,"page_time":1}).forEach(printjson);"
CMD="db.weixin_articles.find({},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).limit(10).sort({"account_openid":1}).forEach(printjson);"
# $gt can not use ,because it conflit with shell ${}
#CMD="db.weixin_articles.find({"page_time":{"\$gt":1439135999},"page_time":{"\$lte":1439395199}},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).sort({"account_openid":1}).count();"
#CMD="db.weixin_articles.find({"page_time":{"gt":1439135999},"page_time":{"lt":1439395199}},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).limit(10);"
mongo 10.136.20.106:27070/WeiXinRecom  -eval "${CMD}" > ${FILENAME}".tmp"
#mongo 10.136.20.106:27070/WeiXinRecom  -eval "db.weixin_articles.find({},{"account_openid":1,"page_time":1,"read_num":1,"yuedu_fensi_bi":1}).limit(100).forEach(printjson);" > t_zyp.tmp
awk 'NR>2{print $0}' ${FILENAME}".tmp" > input_tmp/${FILENAME}".json"
# need to awk 'BEGIN{print "["} { if(match($0,"}")) {print $0","} else{print $0} }  END{print "]"}' tmp.samp; use this above
#awk 'BEGIN{print "["} NR>2 {if(match($0,"}")){print $0","} else{print $0}} END{print "]"}' ${FILENAME}".tmp" > ${FILENAME}".txt"
# and you need to delete the last "," nearest the last "}" in the file by yourself. Why do not use python to read mongo???
dos2unix input_tmp/${FILENAME}".json"
rm -f ${FILENAME}".tmp"



##----- download the first_level_topic and second_level_topic by the first_level_topic
#file_name="first_level_topic"
## the third one for select topic1 and subtopic_1 attrs
#mysql -h 10.134.78.228 -udarrenan -pdarrenan db_personalized_reading --default-character-set=gbk -e "select first_level_topic from \
#    t_first_level_topic where first_level_topic not like '%fq%'" > ${file_name}".tmp"
#awk 'NR>=2 {print $0}' ${file_name}".tmp" > ${file_name}".txt"
#dos2unix ${file_name}".txt"
#rm -f ${file_name}".tmp"
#
#f_name="second_level_topic"
## the third one for select topic1 and subtopic_1 attrs
#if [ -f ${file_name}".tmp" ]
#then
#    rm -rf ${file_name}".tmp"
#fi
#cat ${file_name}".txt" | while read zhu
#do
#    mysql -h 10.134.78.228 -udarrenan -pdarrenan db_personalized_reading --default-character-set=gbk -e "select second_level_topic from \
#        t_second_level_topic where first_level_topic='${zhu}' and second_level_topic not like '%f%'" >> ${f_name}".tmp"
#done
#awk 'NR>=2 {if(match($0,"second_level_topic"))print "zhu-sub";else print $0}' ${f_name}".tmp" > ${f_name}".txt"
#dos2unix ${f_name}".txt"
#rm -f ${f_name}".tmp"
