from flask import Flask, render_template, request, redirect, url_for
import os
import data
import dao

app = Flask(__name__)

def get_connection():
    return data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')

@app.route('/')
def index():

    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    cursor = dao.get_offices(conn)
    
    return render_template('index.template.html', cursor=cursor)



@app.route('/show_employees_in_office/<office_code>')
def show_employees(office_code):

    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    cursor = dao.get_employees(conn, office_code)
    
    return render_template('employees.html', cursor=cursor)

@app.route('/employees', methods=['GET', 'POST'])
def display_employees():

    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')

    # get the SQL data for selecting employees first name/last name at dropdown
    cursor_fn = dao.get_employees_fn(conn)
    cursor_ln = dao.get_employees_ln(conn)
    cursor_ct = dao.get_employees_ct(conn)
    cursor_jt = dao.get_employees_jt(conn)

    # get user input at dropdown for firstname and lastname when user submit via button
    user_input_fn = ""
    user_input_ln = ""
    user_input_ct = ""
    user_input_jt = ""

    if request.method == 'POST':
        user_input_fn = request.form.get('firstName')
        user_input_ln = request.form.get('lastName')
        user_input_ct = request.form.get('country')
        user_input_jt = request.form.get('jobTitle')

    # get SQL data for table with filters to display on employees_only.html
    cursor = dao.get_employees_filtered(conn, user_input_fn, user_input_ln, user_input_ct, user_input_jt)
    saved_list = list(cursor)
    # print('--------hello------')
    # print(saved_list)
    

    return render_template('employees_only.html', saved_list=saved_list, cursor_fn = cursor_fn , cursor_ln=cursor_ln, cursor_ct=cursor_ct, cursor_jt=cursor_jt)






# @app.route('/employees_filters')
# def employees_filters():
    
#     conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    

#     return render_template('employees_filters.html', cursor=cursor, cursor_ln = cursor_ln)
    
    








# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)