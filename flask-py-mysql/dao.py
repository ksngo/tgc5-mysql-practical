import data

# get offices
def get_offices(conn):

    sql = """select * from `offices` where 1"""
    cursor = data.create_cursor(conn)
    cursor.execute(sql)

    return cursor

def get_employees(conn, office_code):

    sql =f""" select * from `employees` where 1 and `officeCode` = {office_code} """
    cursor = data.create_cursor(conn)
    cursor.execute(sql)

    return cursor

def get_employees_only(conn):

    sql = "select * from `employees`"
    cursor = data.create_cursor(conn)
    cursor.execute(sql)

    return cursor

def get_employees_filtered(conn, user_input_fn, user_input_ln, user_input_ct, user_input_jt):



    sql = f"""select * from `employees` 
            join `offices` on `employees`.`officeCode` = `offices`.`officeCode`
            where 1"""
    cursor = data.create_cursor(conn)
    
    print('user_input_fn : ', user_input_fn)
    if user_input_fn != "":
        
        sql = sql + f" and `firstName`='{user_input_fn}' "
        print(sql)

    print('user_input_ln : ', user_input_ln)
    if user_input_ln != "":
        sql = sql + f" and `lastName`='{user_input_ln}' "


    print('user_input_ct :', user_input_ct)
    if user_input_ct != "":
        sql = sql + f" and `country`='{user_input_ct}' "

    print('user_input_jt :', user_input_jt)
    if user_input_jt !="":
        sql = sql + f" and `jobTitle`='{user_input_jt}' "

    
    print('-------sql---------')
    print(sql)
    cursor.execute(sql)

    return cursor

def get_employees_fn(conn):

    sql = "select `firstName` from `employees` "
    cursor_fn = data.create_cursor(conn)
    cursor_fn.execute(sql)

    return cursor_fn

def get_employees_ln(conn):

    sql = " select `lastName` from `employees`"
    cursor_ln = data.create_cursor(conn)
    cursor_ln.execute(sql)

    return cursor_ln


def get_employees_ct(conn):

    sql = f"""select `country` from `employees`
            join `offices` on `employees`.`officeCode` =`offices`.`officeCode` """
    
    cursor_ct = data.create_cursor(conn)
    cursor_ct.execute(sql)

    cursor_ct = cursor_ct.fetchall()
    print(cursor_ct)

    return cursor_ct

def get_employees_jt(conn):

    sql = " select `jobTitle` from `employees` "

    cursor_jt = data.create_cursor(conn)
    cursor_jt.execute(sql)

    return cursor_jt

def get_offices(conn):

    sql = "select * from `offices` ORDER BY `officeCode` asc"

    cursor_offices= data.create_cursor(conn)
    cursor_offices.execute(sql)

    return cursor_offices

def new_offices(conn, officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory):

    sql = f"""insert into `offices` (`officeCode`,`city`,`phone`,`addressLine1`,`addressLine2`,`state`,`country`,`postalCode`,`territory`)
        values('{officeCode}','{city}','{phone}','{addressLine1}','{addressLine2}','{state}','{country}','{postalCode}','{territory}')
        """ 

    cursor = data.create_cursor(conn)
    cursor.execute(sql)
    conn.commit()