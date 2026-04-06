from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Income': ['Stable', 'Stable', 'Stable', 'Unstable', 'Unstable', 'Stable', 'Stable', 'Unstable'],
    'Credit': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad'],
    'Employment': ['Permanent', 'Contract', 'Permanent', 'Contract', 'Permanent', 'Contract', 'Contract', 'Permanent'],
    'Default': ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
}).astype('category')

print(data)

model = DiscreteBayesianNetwork([
    ('Income', 'Default'),
    ('Credit', 'Default'),
    ('Employment', 'Default')
])

model.fit(data)

inference = VariableElimination(model)
query_result = inference.query(variables=['Income'], evidence={'Default': 'Yes'})

print(query_result)

query_result = inference.query(variables=['Credit'], evidence={'Default': 'Yes'})

print(query_result)

query_result = inference.query(variables=['Employment'], evidence={'Default': 'Yes'})

print(query_result)
