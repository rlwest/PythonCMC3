from utility import Utility
from production_cycle import ProductionCycle

# Initialize environmental memory
environment_memory = {
    'counter': {
        'bread1': 'on_counter',
        'cheese': 'on_counter',
        'ham': 'on_counter',
        'bread2': 'on_counter'
    },
    'plate': {}
}
memories = {
    'environment_memory': environment_memory
}

# Initialize the productions
ProceduralProductions = []

# Production to move the first slice of bread to the plate
def move_bread1_to_plate(memories):
    memories['environment_memory']['plate']['bread1'] = 'on_plate'
    del memories['environment_memory']['counter']['bread1']
    return 60

def delayed_bread1_to_plate(memories):
    print("First slice of bread is on the plate.")

ProceduralProductions.append({
    'matches': {'environment_memory': {'counter': {'bread1': 'on_counter'}}},
    'negations': {},
    'utility': 10,
    'action': move_bread1_to_plate,
    'report': "Move first slice of bread to plate",
    'delayed_action': delayed_bread1_to_plate
})

# Production to put the cheese on top of the first slice of bread
def move_cheese_to_plate(memories):
    memories['environment_memory']['plate']['cheese'] = 'on_plate'
    del memories['environment_memory']['counter']['cheese']
    return 60

def delayed_cheese_to_plate(memories):
    print("Slice of cheese is on the plate.")

ProceduralProductions.append({
    'matches': {'environment_memory': {'counter': {'cheese': 'on_counter'}}},
    'negations': {'environment_memory': {'plate': {'bread1': 'not_present'}}},
    'utility': 10,
    'action': move_cheese_to_plate,
    'report': "Put cheese on top of the first slice of bread",
    'delayed_action': delayed_cheese_to_plate
})

# Production to put the ham on top of the cheese
def move_ham_to_plate(memories):
    memories['environment_memory']['plate']['ham'] = 'on_plate'
    del memories['environment_memory']['counter']['ham']
    return 60

def delayed_ham_to_plate(memories):
    print("Slice of ham is on the plate.")

ProceduralProductions.append({
    'matches': {'environment_memory': {'counter': {'ham': 'on_counter'}}},
    'negations': {'environment_memory': {'plate': {'cheese': 'not_present'}}},
    'utility': 10,
    'action': move_ham_to_plate,
    'report': "Put ham on top of the cheese",
    'delayed_action': delayed_ham_to_plate
})

# Production to put the second slice of bread on top of the ham
def move_bread2_to_plate(memories):
    memories['environment_memory']['plate']['bread2'] = 'on_plate'
    del memories['environment_memory']['counter']['bread2']
    return 60

def delayed_bread2_to_plate(memories):
    print("Second slice of bread is on the plate.")

ProceduralProductions.append({
    'matches': {'environment_memory': {'counter': {'bread2': 'on_counter'}}},
    'negations': {'environment_memory': {'plate': {'ham': 'not_present'}}},
    'utility': 10,
    'action': move_bread2_to_plate,
    'report': "Put second slice of bread on top of the ham",
    'delayed_action': delayed_bread2_to_plate
})

# Production to announce the completion of the sandwich
def announce_sandwich_ready(memories):
    print("Ham and cheese sandwich is ready!")

ProceduralProductions.append({
    'matches': {'environment_memory': {'plate': {'bread2': 'on_plate'}}},
    'negations': {},
    'utility': 10,
    'action': announce_sandwich_ready,
    'report': "Announce the ham and cheese sandwich is ready"
})

# Production system delays in ticks
ProductionSystem1_Countdown = 1

# Stores the number of cycles for a production system to fire and reset
DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown
}

# Dictionary of all production systems and delays
AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown]
}

# Initialize ProductionCycle
ps = ProductionCycle()

# Run the cycle with custom parameters
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=500, millisecpercycle=10)
