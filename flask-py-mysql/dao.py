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

def get_employees_filtered(conn, user_input_fn, user_input_ln):

    sql = "select * from `employees` where 1"
    cursor = data.create_cursor(conn)
    
    if user_input_fn != "":
        
        sql = sql + f" and `firstName`='{user_input_fn}' "
        print(sql)

    if user_input_ln != "":
        sql = sql + f" and `lastName`='{user_input_ln}' "

    cursor.execute(sql)

    return cursor

def get_employees_fn(conn):

    sql = "select `firstName` from `employees` "
    cursor = data.create_cursor(conn)
    cursor.execute(sql)

    return cursor

def get_employees_ln(conn):

    sql = " select `lastName` from `employees`"
    cursor_ln = data.create_cursor(conn)
    cursor_ln.execute(sql)

    return cursor_ln