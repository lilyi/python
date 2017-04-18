# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:52:41 2017

@author: Lily
"""

# coding=UTF-8

import MySQLdb

try:
  db = MySQLdb.connect("qnap.dev","root","root","yen_nas",charset='utf8')
  sql = "SELECT * FROM `qtip_product_specs` WHERE `field_id` = 757"
#  sql = "SELECT page_type, page_id, count(*) as total_votes FROM `page_helpful` where page_type='tutorial' group by `page_type`, `page_id` order by total_votes desc"

  # 執行SQL statement
  cursor = db.cursor()
  cursor.execute(sql)

  # 撈取多筆資料
  results = cursor.fetchall()
#  print(results)
  # 迴圈撈取資料
  for record in results: 
      page_type = record[0]
      page_id = record[1]
      total_votes = record[2]
      
    
      print ("%s, %s, %s" % (page_type, page_id, total_votes))

  # 關閉連線
  db.close()

except MySQLdb.Error as e:
  print ("Error %d: %s" % (e.args[0], e.args[1]))
  
