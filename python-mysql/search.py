import pymysql
import os

conn =pymysql.connect(
    host='localhost',
    user=os.environ.get('C9_USER'),
    password='',
    database='classicmodels'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)

sql = """
    select `firstName`,`lastName`,`city` from
    employees join offices ON `employees`.`officeCode`=`offices`.`officeCode`

"""

cursor.execute(sql)

for each_employee in cursor:
    print(each_employee)