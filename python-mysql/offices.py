import pymysql
import os

conn =pymysql.connect(
    host='localhost',
    user=os.environ.get('C9_USER'),
    password='',
    database='classicmodels'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)

input_user = input('enter an office code:')
print(f'searching for {input_user}')

sql = f"""

    select `officeCode`,count(*) from `employees`
    where `officeCode` = '{input_user}'
    group by `officeCode`

"""

# print(sql)
cursor.execute(sql)

print(cursor)

for each in cursor:
    print(each)