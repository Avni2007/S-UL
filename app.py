from flask import Flask, render_template, request
from model import predict_performance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = request.form['hours']
        attendance = request.form['attendance']
        prev_marks = request.form['prev_marks']

        marks, result = predict_performance(hours, attendance, prev_marks)

        return render_template('index.html',
                               prediction=marks,
                               result=result)
    except:
        return render_template('index.html',
                               prediction="Error",
                               result="Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)
    