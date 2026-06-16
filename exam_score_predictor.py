import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("student_scores.csv")

X = data[['StudyHours', 'Attendance']]
y = data['Score']

model = LinearRegression()
model.fit(X, y)

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

prediction = model.predict([[hours, attendance]])

print(f"Predicted Exam Score: {prediction[0]:.2f}")