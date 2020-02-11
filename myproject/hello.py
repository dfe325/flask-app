from flask import Flask, request, url_for, redirect, render_template
#peewee
#sqlalchemy
#restul APP w flask
#https://www.youtube.com/watch?v=9MHYHgh4jYc

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        value = request.form["input"]
        return redirect(url_for(".user", input=input))
    else:
        return render_template("index.html")

@app.route("/<input>")
def user(input):
    return f"<h1>{input}!!! Hello!!</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()
