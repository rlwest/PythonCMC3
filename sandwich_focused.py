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

# Initialize working memory
working_memory = {
    'focus_buffer': {'task': 'start'},
    'motor_buffer': {'action': 'none'},
    'task_completed': False
}

memories = {
    'working_memory': working_memory,
    'environment_memory': environment_memory
}

# Initialize the productions
ProceduralProductions = []
MotorProductions = []

# Production to start the task and move the first slice of bread
def start_task(memories):
    memories['working_memory']['focus_buffer']['task'] = 'move_bread1'
    memories['working_memory']['motor_buffer']['action'] = 'move_bread1'
    memories['working_memory']['task_completed'] = False
ProceduralProductions.append({
    'matches': {'working_memory': {'focus_buffer': {'task': 'start'}}},
    'negations': {},
    'utility': 10,
    'action': start_task,
    'report': "Start task and move first slice of bread"
})

# Production to update task after first slice of bread is moved
def update_task_after_bread1(memories):
    if 'bread1' in memories['environment_memory']['plate'] and memories['working_memory']['motor_buffer']['action'] == 'none':
        memories['working_memory']['focus_buffer']['task'] = 'move_cheese'
        memories['working_memory']['motor_buffer']['action'] = 'move_cheese'
        memories['working_memory']['task_completed'] = False
ProceduralProductions.append({
    'matches': {'environment_memory': {'plate': {'bread1': 'on_plate'}}, 'working_memory': {'task_completed': True}},
    'negations': {'working_memory': {'focus_buffer': {'task': 'move_cheese'}}},
    'utility': 10,
    'action': update_task_after_bread1,
    'report': "Update task to move cheese after first slice of bread is moved"
})

# Production to update task after cheese is moved
def update_task_after_cheese(memories):
    if 'cheese' in memories['environment_memory']['plate'] and memories['working_memory']['motor_buffer']['action'] == 'none':
        memories['working_memory']['focus_buffer']['task'] = 'move_ham'
        memories['working_memory']['motor_buffer']['action'] = 'move_ham'
        memories['working_memory']['task_completed'] = False
ProceduralProductions.append({
    'matches': {'environment_memory': {'plate': {'cheese': 'on_plate'}}, 'working_memory': {'task_completed': True}},
    'negations': {'working_memory': {'focus_buffer': {'task': 'move_ham'}}},
    'utility': 10,
    'action': update_task_after_cheese,
    'report': "Update task to move ham after cheese is moved"
})

# Production to update task after ham is moved
def update_task_after_ham(memories):
    if 'ham' in memories['environment_memory']['plate'] and memories['working_memory']['motor_buffer']['action'] == 'none':
        memories['working_memory']['focus_buffer']['task'] = 'move_bread2'
        memories['working_memory']['motor_buffer']['action'] = 'move_bread2'
        memories['working_memory']['task_completed'] = False
ProceduralProductions.append({
    'matches': {'environment_memory': {'plate': {'ham': 'on_plate'}}, 'working_memory': {'task_completed': True}},
    'negations': {'working_memory': {'focus_buffer': {'task': 'move_bread2'}}},
    'utility': 10,
    'action': update_task_after_ham,
    'report': "Update task to move second slice of bread after ham is moved"
})

# Production to announce the completion of the sandwich
def announce_sandwich_ready(memories):
    if 'bread2' in memories['environment_memory']['plate'] and memories['working_memory']['motor_buffer']['action'] == 'none':
        print("Ham and cheese sandwich is ready!")
        memories['working_memory']['focus_buffer']['task'] = 'done'
        memories['working_memory']['task_completed'] = True
ProceduralProductions.append({
    'matches': {'environment_memory': {'plate': {'bread2': 'on_plate'}}, 'working_memory': {'task_completed': True}},
    'negations': {'working_memory': {'focus_buffer': {'task': 'done'}}},
    'utility': 10,
    'action': announce_sandwich_ready,
    'report': "Announce the ham and cheese sandwich is ready"
})

# Motor productions to move the ingredients with delays

# Move first slice of bread to the plate
def move_bread1(memories):
    memories['environment_memory']['plate']['bread1'] = 'on_plate'
    del memories['environment_memory']['counter']['bread1']
    memories['working_memory']['motor_buffer']['action'] = 'none'
    memories['working_memory']['task_completed'] = True
    return 2

def delayed_bread1(memories):
    print("First slice of bread is on the plate.")

MotorProductions.append({
    'matches': {'working_memory': {'motor_buffer': {'action': 'move_bread1'}}},
    'negations': {},
    'utility': 10,
    'action': move_bread1,
    'report': "Move first slice of bread to plate",
    'delayed_action': delayed_bread1
})

# Move cheese to the plate
def move_cheese(memories):
    memories['environment_memory']['plate']['cheese'] = 'on_plate'
    del memories['environment_memory']['counter']['cheese']
    memories['working_memory']['motor_buffer']['action'] = 'none'
    memories['working_memory']['task_completed'] = True
    return 2

def delayed_cheese(memories):
    print("Slice of cheese is on the plate.")

MotorProductions.append({
    'matches': {'working_memory': {'motor_buffer': {'action': 'move_cheese'}}},
    'negations': {},
    'utility': 10,
    'action': move_cheese,
    'report': "Put cheese on top of the first slice of bread",
    'delayed_action': delayed_cheese
})

# Move ham to the plate
def move_ham(memories):
    memories['environment_memory']['plate']['ham'] = 'on_plate'
    del memories['environment_memory']['counter']['ham']
    memories['working_memory']['motor_buffer']['action'] = 'none'
    memories['working_memory']['task_completed'] = True
    return 2

def delayed_ham(memories):
    print("Slice of ham is on the plate.")

MotorProductions.append({
    'matches': {'working_memory': {'motor_buffer': {'action': 'move_ham'}}},
    'negations': {},
    'utility': 10,
    'action': move_ham,
    'report': "Put ham on top of the cheese",
    'delayed_action': delayed_ham
})

# Move second slice of bread to the plate
def move_bread2(memories):
    memories['environment_memory']['plate']['bread2'] = 'on_plate'
    del memories['environment_memory']['counter']['bread2']
    memories['working_memory']['motor_buffer']['action'] = 'none'
    memories['working_memory']['task_completed'] = True
    return 2

def delayed_bread2(memories):
    print("Second slice of bread is on the plate.")

MotorProductions.append({
    'matches': {'working_memory': {'motor_buffer': {'action': 'move_bread2'}}},
    'negations': {},
    'utility': 10,
    'action': move_bread2,
    'report': "Put second slice of bread on top of the ham",
    'delayed_action': delayed_bread2
})

# Production system delays in ticks
ProductionSystem1_Countdown = 1
ProductionSystem2_Countdown = 1

# Stores the number of cycles for a production system to fire and reset
DelayResetValues = {
    'ProductionSystem1': ProductionSystem1_Countdown,
    'ProductionSystem2': ProductionSystem2_Countdown
}

# Dictionary of all production systems and delays
AllProductionSystems = {
    'ProductionSystem1': [ProceduralProductions, ProductionSystem1_Countdown],
    'ProductionSystem2': [MotorProductions, ProductionSystem2_Countdown]
}

# Initialize ProductionCycle
ps = ProductionCycle()

# Add debug statements in production cycle
def match_productions(self, memories, AllProductionSystems):
    """Finds and groups matched productions."""
    grouped_matched_productions = {key: [] for key in AllProductionSystems}

    for prod_system_key, prod_system_value in AllProductionSystems.items():
        if prod_system_value[1] > 0:
            prod_system_value[1] -= 1

        prod_system = prod_system_value[0]
        delay = prod_system_value[1]

        if delay > 0:
            continue

        for production in prod_system:
            is_match_for_all_buffers = True
            for memory_type in memories:
                for buffer_key in production['matches'].keys():
                    matches = production['matches'].get(buffer_key, {})
                    negations = production['negations'].get(buffer_key, {})
                    buffer_dict = memories[memory_type].get(buffer_key, {})
                    print(f"Checking production {production['report']} in {prod_system_key}")
                    print(f"Memory type: {memory_type}, Buffer key: {buffer_key}")
                    print(f"Memory content: {buffer_dict}")
                    print(f"Matches: {matches}")
                    print(f"Negations: {negations}")
                    if not Utility.buffer_match_eval(buffer_dict, matches, negations):
                        is_match_for_all_buffers = False
                        break

            if is_match_for_all_buffers:
                grouped_matched_productions[prod_system_key].append(production)
                print(f"Matched Production in {prod_system_key}: {production.get('report')}")

    return grouped_matched_productions

ProductionCycle.match_productions = match_productions

# Run the cycle with custom parameters
ps.run_cycles(memories, AllProductionSystems, DelayResetValues, cycles=10, millisecpercycle=10)
