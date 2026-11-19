from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "Achee6phIexoh8dagiQuew0ephuga4Ih"

@app.route('/')
def index():
    redirect(url_for("index"))
    return render_template("index.html")

@app.route('/<name>')
def page(name):
    return render_template(f'{name}')

if __name__ == "__main__":
    app.run(debug=True)