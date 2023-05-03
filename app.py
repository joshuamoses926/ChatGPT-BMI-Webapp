from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        weight_unit = request.form['weight_unit']
        height_unit = request.form['height_unit']

        if weight_unit == 'lb':
            weight = weight * 0.453592  # convert to kg
        if height_unit == 'in':
            height = height * 2.54  # convert to cm

        height = height / 100  # convert to meters if height is in cm

        bmi = round(weight / (height ** 2), 2)
    return render_template('index.html', bmi=bmi)
