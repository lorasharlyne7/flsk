from flask import Flask, render_template,send_from_directory
app = Flask(__name__, static_url_path='/static')

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


if __name__ == "__main__":
    app.run()