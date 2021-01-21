from flask import Flask, render_template, request,  url_for, redirect, session
import sqlite3 as lite


app = Flask(__name__)
app.secret_key = 'minhdang241'

@app.route('/')
def home():
    result, show_order, order_history, username, password = session.get('result'), session.get('show_order', False), session.get('order_history', []), session.get('username', ''), session.get('password', '')
    
    return render_template('demo.html', result=result, show_order=show_order, order_history=enumerate(order_history), username=username, password=password)

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    con = lite.connect('user.db')
    with con:
        cur = con.cursor() 
        query = f"SELECT * FROM USER WHERE username='{username}' AND password='{password}'"
        print(query)
        cur.executescript(query)
        try:
            cur.execute(query)
        except:
            print("Multiple queries are executed!")
        user = cur.fetchall()
        print(user)

    result = False
    show_order=False
    order_history = []
    if len(user) > 0:
        result=True
        show_order=True
        con = lite.connect('user.db')
        with con:
            cur = con.cursor() 
            query = f"SELECT * FROM ORDER_HISTORY WHERE username='{username}'"
            print(query)
            cur.execute(query)
            order_history = cur.fetchall()

    session['result'] = result
    session['show_order'] = show_order
    session['order_history'] = order_history
    session['username'] = username
    session['password'] = password
    return redirect(url_for('home'))