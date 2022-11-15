from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__,static_folder="static")

@app.route("/DonorLogin")
def DonorLogin():
    return render_template("DonorLogin.html")

@app.route("/DonorSignup")
def DonorSignup():
    return render_template("DonorSignup.html")

@app.route("/RecipientLogin")
def RecipientLogin():
    return render_template("RecipientLogin.html")

@app.route("/RecipientSignup")
def RecipientSignup():
    return render_template("RecipientSignup.html")

@app.route("/InchargeLogin")
def InchargeLogin():
    return render_template("InchargeLogin.html")

@app.route("/InchargeSignup")
def InchargeSignup():
    return render_template("InchargeSignup.html")


if __name__=="__main__":
    app.run(port=5000,debug=True)