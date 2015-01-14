from flask import Flask,request,url_for,redirect,render_template,session,flash



app=Flask(__name__)


@app.route("/")
def index():
    return render_template("play.html")

if __name__=="__main__":
   app.debug=True
   app.secret_key="hello"
   app.run(host="0.0.0.0",port=8000)
