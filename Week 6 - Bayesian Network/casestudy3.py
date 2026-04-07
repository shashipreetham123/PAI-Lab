from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

df = pd.read_csv("dataset.csv")
df['Hours_Studied'] = df['Hours_Studied'].astype(int)
df['Study_Level'] = 'High'

df.loc[df['Hours_Studied'] <= 10, 'Study_Level'] = 'Low'

df.loc[(df['Hours_Studied'] > 10) & (df['Hours_Studied'] <= 16), 'Study_Level'] = 'Medium'

df['Attendance_Level'] = 'High'
df.loc[df['Attendance'] < 75, 'Attendance_Level'] = 'Low'
df.loc[(df['Attendance'] >= 75) & (df['Attendance'] <= 90), 'Attendance_Level'] = 'Medium'

df['Sleep_Level'] = 'High'
df.loc[df['Sleep_Hours'] < 5, 'Sleep_Level'] = 'Low'
df.loc[(df['Sleep_Hours'] >= 5) & (df['Sleep_Hours'] <= 7), 'Sleep_Level'] = 'Medium'

df['Marks_Level'] = 'High'
df.loc[df['Exam_Score'] <= 50, 'Marks_Level'] = 'Low'
df.loc[(df['Exam_Score'] > 50) & (df['Exam_Score'] <= 65), 'Marks_Level'] = 'Medium'

X = df[["Attendance_Level", "Sleep_Level", "Access_to_Resources", "Internet_Access", "Family_Income", "School_Type", "Parental_Education_Level", "Gender", "Marks_Level"]]

print(X.head())

X = X.astype('category')


model = DiscreteBayesianNetwork([
    ('Attendance_Level', 'Marks_Level'),
    ('Sleep_Level', 'Marks_Level'),
    ('Access_to_Resources', 'Marks_Level'),
    ('Internet_Access', 'Marks_Level'),
    ('Family_Income', 'Marks_Level'),
    ('School_Type', 'Marks_Level'),
    ('Parental_Education_Level', 'Marks_Level'),    
    ('Family_Income', 'School_Type'),
    ('Gender', 'Marks_Level')
])

model.fit(X)

inference = VariableElimination(model)
query_result = inference.query(variables=['Attendance_Level'], evidence={'Marks_Level': 'High'})
print(query_result)



