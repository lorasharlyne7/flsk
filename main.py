from flask import Flask, render_template,send_from_directory,request
app = Flask(__name__, static_url_path='/static')
import psycopg2

try:
    conn = psycopg2.connect("dbname='myduka' user='postgres' host='localhost' password='12345'")
except:
    print("Cannot connect to the database")

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/l')
def login():
    return render_template('login.html')
@app.route('/ass')
def ass():
    return render_template('ass.html')
@app.route('/bab')
def baby():
    return render_template('baby.html')
@app.route('/bas')
def base():
    return render_template('base.html')
@app.route('/caroo')
def carousel():
    return render_template('carousel.html')
@app.route('/divider')
def divs():
    return render_template('divs.html')
@app.route('/empt')
def empty():
    return render_template('empty.html')
@app.route('/1')
def index1():
    return render_template('index1.html')
@app.route('/lynn')
def lynn():
    return render_template('lynn.html')
@app.route('/s')
def sharl():
    return render_template('sharl.html')
@app.route("/sign_up",methods=['POST'])
def sign_up():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    cr=conn.cursor()
    data_sql_query="""INSERT INTO users(name,email,password) VALUES(%s,%s,%s)"""
    values=name,email,password
    cr.execute(data_sql_query,values)
    conn.commit()
    return ("Welcome, "+ name+ " your email adress "+email+" has been registered")
@app.route("/signin", methods=['GET'])
def signin():
    email= request.form["email"]
    password=request.form["password"]
    cr=conn.cursor()
    email_db_query="""SELECT email from users WHERE email=%s"""
    value=email
    cr.execute(email_db_query,value)
    db_email=cr.fetchall()
    print(db_email)
    password_db_query="""SELECT password FROM users WHERE email=%s"""
    val=email
    cr.execute(password_db_query,val)
    db_password=cr.fetchall()
    if email==db_email and password==db_password:
        return render_template("index.html")
    else:
        return("incorrect login details")


if __name__ == "__main__":
    app.run()