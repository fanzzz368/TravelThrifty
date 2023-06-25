from flask import Flask, render_template


app = Flask(__name__, static_folder='static')

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/questionnaire')
def questionnaire_page():
    return render_template('questionnaire.html')


@app.route('/creators')
def creator_page():
    return render_template('creators.html')

@app.route('/cindy')
def cindy():
    return render_template('TravelThrifty.html')

if __name__ == '__main__':
    app.run()