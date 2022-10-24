from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Home_page')
def Home_page():
   return render_template('Home_page.html')

@app.route('/About_page')
def About_page():
   return render_template('About_page.html')

@app.route('/signup_page')
def signup_page():
   return render_template('signup_page.html')


@app.route('/signin_page')
def signin_page():
   return render_template('signin_page.html')

if __name__=='__main__':
   app.run(debug=True)