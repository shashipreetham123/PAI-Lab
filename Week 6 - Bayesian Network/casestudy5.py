from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define model structure
model = DiscreteBayesianNetwork([
    ('Earthquake', 'Tornado'),
    ('Earthquake', 'Alarm'),
    ('Tornado', 'Alarm'),
    ('Burglary', 'Alarm')
])

# Step 2: Define CPDs for independent variables

cpd_earthquake = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values=[
        [0.4],   # Earthquake = Yes
        [0.6]    # Earthquake = No
    ],
    state_names={'Earthquake': ['Yes', 'No']}
)

cpd_tornado = TabularCPD(
    variable='Tornado',
    variable_card=2,
    values=[
        [0.8, 0.5],   # Tornado = Yes
        [0.2, 0.5]    # Tornado = No
    ],
    evidence=['Earthquake'],
    evidence_card=[2],
    state_names={
        'Earthquake': ['Yes', 'No'],
        'Tornado': ['Yes', 'No']
    }
)

cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[
        [0.7], # Burglary = Yes
        [0.3] # Burglary = No
    ],
    state_names={'Burglary': ['Yes', 'No']}
)

cpd_alarm = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        [1, 0.9, 0.95, 0.85, 0.89, 0.7, 0.87, 0.3],   # Tornado = Yes
        [0, 0.1, 0.05, 0.15, 0.11, 0.3, 0.13, 0.7]    # Tornado = No
    ],
    evidence=['Earthquake', 'Tornado', 'Burglary'],
    evidence_card=[2, 2, 2],
    state_names={
        'Earthquake': ['Yes', 'No'],
        'Tornado': ['Yes', 'No'],
        'Burglary': ['Yes', 'No'],
        'Alarm': ['Yes', 'No']
    }
)

# Step 4: Add CPDs to model
model.add_cpds(cpd_earthquake, cpd_tornado, cpd_burglary, cpd_alarm)

# Step 5: Check model
print("Model valid:", model.check_model())

# Step 6: Inference
inference = VariableElimination(model)

# Query 1: P(Earthquake | Alarm = Yes)
result_earthquake_alarm  = inference.query(variables=['Earthquake'], evidence={'Alarm': 'Yes'})
print("\nP(Earthquake | Alarm = Yes):")
print(result_earthquake_alarm)

# Query 2: P(Tornado | Alarm = Yes)
result_tornado_alarm = inference.query(variables=['Tornado'], evidence={'Alarm': 'Yes'})
print("\nP(Tornado | Alarm = Yes):")
print(result_tornado_alarm)

# Query 3: P(Burglary | Alarm = Yes)
result_burglary_alarm = inference.query(variables=['Burglary'], evidence={'Alarm': 'Yes'})
print("\nP(Burglary | Alarm = Yes):")
print(result_burglary_alarm)



