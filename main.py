from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/notebooks/driver')
def driver_eda():
    return render_template('driver_eda.html')

@app.route('/notebooks/assignment')
def client_eda():
    return render_template('assignment_eda.html')

@app.route('/notebooks/trip')
def trip_classify():
    return render_template('trip_classification.html')

@app.route('/notebooks/client')
def client():
    return render_template('client.html')

if __name__ == '__main__':
    app.run(debug=True)