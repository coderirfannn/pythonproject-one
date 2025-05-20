from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/service")
def service():
    return render_template("services.html")



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




app.run(debug=True)