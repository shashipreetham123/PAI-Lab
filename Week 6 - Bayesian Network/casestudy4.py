from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define model structure
model = DiscreteBayesianNetwork([
    ('Rain', 'Sprinkler'),
    ('Rain', 'Ground'),
    ('Sprinkler', 'Ground')
])

# Step 2: Define CPDs for independent variables

cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[
        [0.2],   # Rain = Yes
        [0.8]    # Rain = No
    ],
    state_names={'Rain': ['Yes', 'No']}
)

cpd_sprinkler = TabularCPD(
    variable='Sprinkler',
    variable_card=2,
    values=[
        [0.01, 0.4],   # Sprinkler = Yes
        [0.99, 0.6]    # Sprinkler = No
    ],
    evidence=['Rain'],
    evidence_card=[2],
    state_names={
        'Sprinkler': ['Yes', 'No'],
        'Rain': ['Yes', 'No']
    }
)

cpd_ground = TabularCPD(
    variable='Ground',
    variable_card=2,
    values=[
        [0.99, 0.9, 0.8, 0],   # Ground = Wet
        [0.01, 0.1, 0.2, 1]    # Ground = Dry
    ],
    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2, 2],
    state_names={
        'Ground': ['Wet', 'Dry'],
        'Rain': ['Yes', 'No'],
        'Sprinkler': ['Yes', 'No']
    }
)


# Step 4: Add CPDs to model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_ground)

# Step 5: Check model
print("Model valid:", model.check_model())

# Step 6: Inference
inference = VariableElimination(model)

# Query 1: P(Rain | Ground = Wet)
result_rain_ground_wet = inference.query(variables=['Rain'], evidence={'Ground': 'Wet'})
print("\nP(Rain | Ground = Wet):")
print(result_rain_ground_wet)

# Query 2: P(Sprinkler | Ground = Wet)
result_sprinkler_ground_wet = inference.query(variables=['Sprinkler'], evidence={'Ground': 'Wet'})
print("\nP(Sprinkler | Ground = Wet):")
print(result_sprinkler_ground_wet)

# Query 3: P(Ground | Rain = Yes)
result_ground_wet_rain = inference.query(variables=['Ground'], evidence={'Rain': 'Yes'})
print("\nP(Ground | Rain = Yes):")
print(result_ground_wet_rain)
