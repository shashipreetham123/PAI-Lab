from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Weather': ['Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy', 'Sunny', 'Rainy'],
    'Temperature': ['Hot', 'Cool', 'Mild', 'Hot', 'Cool', 'Mild', 'Hot', 'Cool'],
    'PlayOutside': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
}).astype('category')

print(data)

model = DiscreteBayesianNetwork([('Weather', 'Temperature'), ('Temperature', 'PlayOutside')])

model.fit(data)

inference = VariableElimination(model)
query_result = inference.query(variables=['Weather'], evidence={'PlayOutside': 'Yes'})
print(query_result)

