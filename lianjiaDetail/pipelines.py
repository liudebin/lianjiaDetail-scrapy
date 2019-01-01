# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from msysqlDb import mysqlHadler


class LianjiaPipeline(object):
    def process_item(self,item,spider):
        dbObject = mysqlHadler().dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE test")
        # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
        sql = "update  rent_detail_lianjia set price_content = %s, tags= %s,house_type= %s," \
              " sub_way= %s,house_comment= %s,upload_date= %s,square= %s,direction= %s,base_info= %s ," \
              " community_code = %s, community = %s,  community_link = %s" \
              " , rent_status = CASE WHEN rent_status = -1 THEN 0 ELSE rent_status END" \
              " where house_code = %s"
        # sql = "update rent_detail_lianjia set community_code = %s, community = %s,  community_link = %s where house_code = %s"
        try:
            cursor.execute(sql, (item['price_content'], item['tags'], item['house_type'],
                                 item['sub_way'], item['house_comment'], item['upload_date'], item['square'],
                                 item['direct'], item['base_info_str'], item['community_code'], item['community'],
                                 item['community_link']
                                 ,
                                 item['house_code']))
            # cursor.execute(sql, (item['community_code'], item['community'], item['community_link'], item['house_code']))
            cursor.connection.commit()
        except BaseException as e:
            print("ERROR>>>>>>>>>>>>>" , e , "<<<<<<<<<<<<<ERROR")
            dbObject.rollback()
        return item

