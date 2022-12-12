from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/outros')
def outros():
    return render_template("outros.html")


@app.route('/portifolio')
def portifolio():
    return render_template("portifolio.html")

if __name__ == '__main__':
    app.run(debug = True)