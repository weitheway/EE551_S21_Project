import datetime
from flask import Flask, render_template, request, url_for, 
import db 

app = Flask(__name__)

db.create_tables()

@app.route("/home" , methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        db.create_entry(entry_content, datetime.datetime.today().strftime("%m/%d %H:%M:%S"))
    return render_template("home.html", entries=db.retrieve_entries())

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(debug=True)