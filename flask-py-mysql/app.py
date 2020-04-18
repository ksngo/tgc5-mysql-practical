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
    user_input_fn = request.form.get('firstName')
    user_input_ln = request.form.get('lastName')
    cursor = dao.get_employees_filtered(conn, user_input_fn, user_input_ln)
    
    return render_template('employees_only.html', cursor=cursor)






@app.route('/employees_filters')
def employees_filters():
    
    conn = data.get_connection('localhost', os.environ.get('C9_USER'), '', 'classicmodels')
    cursor = dao.get_employees_fn(conn)
    cursor_ln = dao.get_employees_ln(conn)

    return render_template('employees_filters.html', cursor=cursor, cursor_ln = cursor_ln)
    
    








# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)