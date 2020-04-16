import pymysql
import os

conn =pymysql.connect(
    host='localhost',
    user=os.environ.get('C9_USER'),
    password='',
    database='classicmodels'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)

input_user = input('enter a country:')
print(f'searching for {input_user}')

sql = f"""

    select `customerNumber`,`customerName`,`country`,`city` from `customers`
    where `country` like '%{input_user}%';

"""

# print(sql)
cursor.execute(sql)

for each in cursor:
    print(each)