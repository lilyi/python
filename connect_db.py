# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:52:41 2017

@author: Lily
"""

# coding=UTF-8

import MySQLdb
import statistics
import csv

def main():
    type_name = ['tutorial', 'faq']
    for each in type_name:
        try:
    #        db = MySQLdb.connect(host="10.8.2.125",user="marketing_query",passwd="WStFfFDSrzzdEQFW",db="web_analytics",charset='utf8')
            db = MySQLdb.connect("qnap.dev","root","root","web_analytics",charset='utf8')
    #        sql = "SELECT * FROM `qtip_product_specs` WHERE `field_id` = 757"
            sql = "SELECT page_type, page_id, count(*) as total_votes FROM `page_helpful` where page_type='%s' group by `page_id` order by total_votes desc" % each
    #        sql = "SELECT page_id, count(*) as unhelpful_count FROM `page_helpful` WHERE `page_type` = 'tutorial' AND `page_id` IN (137,184,253,15,246) AND helpful = 0 group by page_id"    
    #        執行SQL statement
            cursor = db.cursor()
            cursor.execute(sql)        
    #        撈取多筆資料
            all_results = cursor.fetchall()   
    #        print(results)
    #        迴圈撈取資料
    #        page_type = []
    #        page_id = []
            total_votes = []
            all_data = []
            all_dict = {}
            for record in all_results: 
                all_data.append(record[:])
                all_dict[str(record[1])] = record[0], record[2]
    #            page_type.append(record[0])
    #            page_id.append(record[1])
                total_votes.append(record[2]) 
            med = statistics.median(total_votes)
    #        print(med)
            all_pID = []
            for i in all_data:
                if i[2] >= med:
                   all_pID.append(str(i[1]))
    #        print(all_pID, len(all_pID), len(all_dict))
            all_pID2 = ','.join(all_pID)
            sql2 = "SELECT page_id, count(*) as unhelpful_count FROM `page_helpful` WHERE `page_type` = 'tutorial' AND `page_id` IN (%s) AND helpful = 0 group by page_id" % all_pID2
            cursor.execute(sql2)
            unhelpful_results = cursor.fetchall()
    #        print(len(res))
    #        print(d)
            unhelpful_pID = []
            unfelpful_count = []
            percent = []
            unhelpful_data = []
            result = []
            for i in unhelpful_results:
                unhelpful_data.append(i[:])
                unhelpful_pID.append(str(i[0]))
                unfelpful_count.append(i[1])
                per = round(100*(i[1]/all_dict[str(i[0])][1]),2)
                percent.append(per)
                result.append([str(i[0]), per])
            top10 = sorted(result, key = lambda x : x[1], reverse=True)[:10]
            print(top10)
            
            with open('unhelpful_%s.csv' % each, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['page_id','unhelpful (%)'])
                writer.writerows(top10)
    #        關閉連線
            db.close()
        
        except MySQLdb.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
  
if __name__ == '__main__':
    main()