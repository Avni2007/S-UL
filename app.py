import os
from flask import Flask, render_template, request, jsonify
from model import predict_performance

app = Flask(__name__)

# Camera is not initialized at startup — deferred to avoid crashes in
# cloud environments (Railway) where no physical camera is present.
cap = None


@app.route('/health')
def health():
    """Health check endpoint for Railway and other platforms."""
    return jsonify({"status": "ok"}), 200


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
    except Exception:
        return render_template('index.html',
                               prediction="Error",
                               result="Invalid Input")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)