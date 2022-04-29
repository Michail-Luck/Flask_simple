from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/contacts/")
def contacts():
    context = {"Имя":[], "Статус":[], "Номер":[]}
    with open('main_base.csv', 'r') as csvfile:
        text = csv.reader(csvfile, delimiter=';')
        for row in text:
            context["Имя"].append(row[0])
            context["Статус"].append(row[1])
            context["Номер"].append(row[2])
    return render_template('contacts.html', context_names = context["Имя"],
                           context_status = context["Статус"],
                           context_phone = context["Номер"], num = len(context["Имя"]))

@app.route("/")
def index():
    name = 'Олег'
    age = 27
    phone_number = "8 800 535 35 35 "
    e_mail = "oleg@mail.com"
    return render_template('index.html', name = name, age = age, phone_number = phone_number, e_mail = e_mail)

@app.route("/create_new_contact/", methods=['GET','POST'])
def create_new_contact():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method =='POST':
        input_name = request.form['input_name']
        input_status = request.form['input_status']
        input_phone = request.form['input_phone']
        with open('main_base.csv', 'a+') as f:
            f.write(f'{input_name};{input_status};{input_phone};\n')
        return render_template('form.html')

if __name__ == "__main__":
    with open('main_base.csv', 'w') as f:
        f.write('')
    app.run(debug=True, port=5001)







