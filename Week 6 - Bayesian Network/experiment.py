from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

data = data.astype('category')

print(data)

model = DiscreteBayesianNetwork([('Rain', 'TrafficJam'), ('TrafficJam', 'ArriveLate')])

model.fit(data)

inference = VariableElimination(model)
query_result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})
print(query_result)
