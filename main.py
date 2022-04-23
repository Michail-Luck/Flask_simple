from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = 'Олег'
    age = 23
    phone_number = "8 800 535 35 35 "
    e_mail = "oleg@mail.com"
    return render_template('/templates/index.html', name = name, age = age, phone_number = phone_number, e_mail = e_mail)


if __name__ == "__main__":
    app.run()









