# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:52:41 2017

@author: Lily
"""

# coding=UTF-8

import MySQLdb
import statistics
import csv
import smtplib
try:
#  db = MySQLdb.connect(host="10.8.2.125",user="marketing_query",passwd="WStFfFDSrzzdEQFW",db="web_analytics",charset='utf8')
  db = MySQLdb.connect("qnap.dev","root","root","web_analytics",charset='utf8')
#  sql = "SELECT * FROM `qtip_product_specs` WHERE `field_id` = 757"
  sql = "SELECT page_type, page_id, count(*) as total_votes FROM `page_helpful` where page_type='tutorial' group by `page_id` order by total_votes desc"
#SELECT page_id, count(*) as unhelpful_count FROM `page_helpful` WHERE `page_type` = 'tutorial' AND `page_id` IN (137,184,253,15,246) AND helpful = 0 group by page_id

  # 執行SQL statement
  cursor = db.cursor()
  cursor.execute(sql)

  # 撈取多筆資料
  results = cursor.fetchall()   
#  print(results)
  # 迴圈撈取資料
  page_type = []
  page_id = []
  total_votes = []
  L = []
  d = {}
  for record in results: 
      L.append(record[:])
      d[str(record[1])] = record[0], record[2]
      page_type.append(record[0])
      page_id.append(record[1])
      total_votes.append(record[2]) 
  med = statistics.median(total_votes)
  print(med)
  pID = []
  for i in L:
      if i[2] >= med:
         pID.append(str(i[1]))
  print(pID, len(pID), len(d))
  pID2 = ','.join(pID)
  sql2 = "SELECT page_id, count(*) as unhelpful_count FROM `page_helpful` WHERE `page_type` = 'tutorial' AND `page_id` IN (%s) AND helpful = 0 group by page_id" % pID2
  cursor.execute(sql2)
  res = cursor.fetchall()
  print(len(res))
  print(d)
  page_ID = []
  unfelpful_count = []
  percent = []
  L2 = []
  R = []
  for i in res:
      L2.append(i[:])
      page_ID.append(str(i[0]))
      unfelpful_count.append(i[1])
      per = round(100*(i[1]/d[str(i[0])][1]),2)
      percent.append(per)
      R.append([str(i[0]), per])
  top10 = sorted(R, key = lambda x : x[1], reverse=True)[:10]
  print(top10)

  with open('eggs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['page_id','unhelpful (%)'])
    writer.writerows(top10)
  
  
    
  # 關閉連線
  db.close()

except MySQLdb.Error as e:
  print ("Error %d: %s" % (e.args[0], e.args[1]))
  
