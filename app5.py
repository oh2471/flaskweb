import pymysql

db = pymysql.connect(host='localhost', port = 3306, user='root',passwd='1234',db='myflaskapp',charset='utf8')

try:
    with db.cursor() as cursor:
        sql='''
        CREATE TABLE hash (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                   Data VARCHAR(20) NOT NULL,
                   Domain VARCHAR(10) NOT NULL,
                   IP VARCHAR(10) NOT NULL,
                   CC VARCHAR(10) NOT NULL,
                   ASN VARCHAR(10) NOT NULL,
                   Autom_system_name VARCHAR(10) NOT NULL,
                   Virus_Total_MD5 VARCHAR(10) NOT NULL,
                   PRIMARY KEY(id));
        '''

        cursor.execute(sql)
        db.commit()

finally:
    cursor.close()