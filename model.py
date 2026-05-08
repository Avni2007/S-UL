import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

# Load dataset
data = pd.read_csv("student_data.csv")

# Features & Target
X = data[['StudyHours', 'Attendance', 'PrevMarks']]
y_marks = data['FinalMarks']

# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X, y_marks)

# Create Pass/Fail column
data['Result'] = data['FinalMarks'].apply(lambda x: 1 if x >= 40 else 0)
y_result = data['Result']

# Train Logistic Regression
log_model = LogisticRegression()
log_model.fit(X, y_result)

# Prediction function
def predict_performance(hours, attendance, prev_marks):
    hours = float(hours)
    attendance = float(attendance)
    prev_marks = float(prev_marks)

    marks = lr_model.predict([[hours, attendance, prev_marks]])[0]
    result = log_model.predict([[hours, attendance, prev_marks]])[0]

    return round(marks, 2), "Pass" if result == 1 else "Fail"
    