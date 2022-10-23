from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
@app.route('/HomePage')
def HomePage():
   return render_template('HomePage.html')

@app.route('/About_Page')
def About_Page():
   return render_template('About_Page.html')

@app.route('/SignUp_Page')
def SignUp_Page():
   return render_template('SignUp_Page.html')


@app.route('/SignIn_page')
def SignIn_page():
   return render_template('SignIn_page.html')

if __name__=='__main__':
	app.run(debug=True)