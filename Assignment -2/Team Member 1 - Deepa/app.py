from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Home_page1')
def Home_page1():
   return render_template('Home_page1.html')

@app.route('/About_page1')
def About_page1():
   return render_template('About_page1.html')

@app.route('/signUp_page1')
def signUp_page1():
   return render_template('signUp_page1.html')


@app.route('/signIn_page1')
def signIn_page1():
   return render_template('signIn_page1.html')

if __name__=='__main__':
   app.run(debug=True)