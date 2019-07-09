import pandas_datareader as web
from datetime import datetime
import pandas as pd
import csv
import os
import pymysql


db = pymysql.connect(host='localhost', port = 3306, user='root',passwd='1234',db='myflaskapp',charset='utf8')
sql = 'INSERT IGNORE INTO coin_yahoo_daily(High , Low , Open, Close, Volume , AdjClose ,date) VALUES ("{}","{}","{}","{}","{}","{}","{}")'
cur = db.cursor()
cur.execute("DROP table if exists coin_yahoo_daily;")
cur.execute("create table coin_yahoo_daily  ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, High decimal(9,2),   Low decimal(9,2),   Open decimal(9,2),   Close decimal(9,2),   Volume decimal(9,2),  AdjClose decimal(9,2), date varchar(100)) ;")

start = '2019-05-01'
end = datetime.now()

BTC = web.DataReader('BTC-USD','yahoo',start,end)


now = datetime.now().minute

if os.path.exists("btc" + str(now)+".csv"):
    os.remove("btc"+str(now)+".csv")
    BTC.to_csv("btc" + str(now) +".csv",mode='w')
else :
    BTC.to_csv("btc"+str(now)+".csv",mode='w')

csv_data = csv.reader(open("btc"+str(now)+".csv"))

row_count =0

for row in csv_data:
    if row_count == 0:
        row_count +=1
    else :
        high = row[1]
        low = row[2]
        opendata = row[3]
        closedata = row[4]
        volume = row[5]
        adjclose = row[6]
        date = row[0]
        cur.execute(sql.format(high,low,opendata,closedata,volume,adjclose,date))
        db.commit()
cur.close()