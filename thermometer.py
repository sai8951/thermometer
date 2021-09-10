import random
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', title='偽装体温計')

@app.route('/normal', methods=["GET"])
def normal():
    ten = 3
    one = 6
    point = random.randint(0,7)
    return render_template('normal.html', title='平熱体温計', ten=ten, one=one, point=point)

@app.route('/fake', methods=["GET"])
def fake():
    ten = 3
    one = random.choice([7,8,9])
    if one == 7:
        point = random.randint(5,9)
    elif one == 9:
        point = random.randint(0,3)
    else:
        point = random.randint(0,9)
    return render_template('fake.html', title='仮病体温計', ten=ten, one=one, point=point)

if __name__ == "__main__":
    app.run(debug=True)