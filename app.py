import datetime
from flask import Flask, render_template, request, url_for 
import db 

app = Flask(__name__)

db.create_tables()

@app.route("/home")
@app.route("/", methods=["GET","POST"])
def home():
    return render_template("home.html", entries=db.retrieve_entries())

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST":
        entry_content = request.form.get("content")
        db.create_entry(entry_content, datetime.datetime.today().strftime("%m/%d %H:%M:%S"))
    return render_template("admin.html", entries=db.retrieve_entries())

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(debug=True)