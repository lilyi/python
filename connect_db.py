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

  # 執行SQL statement
  cursor = db.cursor()
  cursor.execute(sql)

  # 撈取多筆資料
  results = cursor.fetchall()

  # 迴圈撈取資料
  for record in results: 
      col1 = record[0]
      col2 = record[1]
    
      print ("%s, %s" % (col1, col2))

  # 關閉連線
  db.close()

except MySQLdb.Error as e:
  print ("Error %d: %s" % (e.args[0], e.args[1]))
  
