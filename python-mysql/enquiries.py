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

    select `customerNumber`,`customerName` from `customers`
    where `customerName` like '%{input_user}%';

"""

# print(sql)
cursor.execute(sql)

for each in cursor:
    print(each)

# Qn3 part 2&3
input_user_CN =input('enter a customer number:')
print(f'searching for {input_user_CN}')

sql = f"""

    select `orderNumber`,`orderDate` from `orders`
    where `customerNumber` like '{input_user_CN}'

"""

cursor.execute(sql)

for i in cursor:
    print (i)

# QN3 part 4 & 5
input_user_ON =input('enter an order number:')
print(f'searching for {input_user_ON}')

sql = f"""

    select `productName`,`productDescription`,`orderDate`, `orderdetails`.`orderNumber` from `orders`
    join `orderdetails` on `orders`.`orderNumber`=`orderdetails`.`orderNumber`
    join `products` on `orderdetails`.`productCode` =`products`.`productCode`
    where `orderdetails`.`orderNumber` like '{input_user_ON}'

"""

cursor.execute(sql)

for j in cursor:
    print (j)