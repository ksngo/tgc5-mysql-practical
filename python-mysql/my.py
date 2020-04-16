import pymysql
import os

conn =pymysql.connect(
    host='localhost',
    user=os.environ.get('C9_USER'),
    password='',
    database='classicmodels'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)

input_user = input('enter a string:')
print(f'searching for {input_user}')

sql = f"""

    select `productName`,`quantityInStock` from `products`
    where `productName` like '%{input_user}%';

"""

# print(sql)
cursor.execute(sql)

for each in cursor:
    print(each)