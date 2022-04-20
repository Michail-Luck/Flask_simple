from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = 'Олег'
    age = 23
    return render_template('main.html', name = name, age = age)


if __name__ == "__main__":
    app.run()









