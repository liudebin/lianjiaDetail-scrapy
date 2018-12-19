# coding=utf-8
from msysqlDb import mysqlHadler

dbObject = mysqlHadler().dbHandle()
cursor = dbObject.cursor()
cursor.execute("USE test")
# sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
sql = "select link from rent_detail_lianjia ;"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    for row in results:
        link = row[0]

        # 打印结果
        print "fname=%s" % \
              (link)
except BaseException as e:
    print("ERROR>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<ERROR")

