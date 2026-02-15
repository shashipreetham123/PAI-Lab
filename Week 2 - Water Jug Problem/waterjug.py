from collections import deque

class State:
    def __init__(self, jug1, jug2, comment):
        self.jug1 = jug1
        self.jug2 = jug2
        self.previous = None
        self.comment = comment
        

def solve_water_jug(jug1, jug2, target):
    q = deque()
    
    q.append(State(0, 0, "Initial State"))
    
    visited = set()
    
    while len(q) != 0 :
        current_state = q.popleft()

        if((current_state.jug1, current_state.jug2) in visited):
            continue
        
        visited.add((current_state.jug1, current_state.jug2))
        
        if ((current_state.jug1 == target and current_state.jug2 == 0) or 
            (current_state.jug2 == target and current_state.jug1 == 0)):
            
            steps = []
            
            temp = current_state
            
            while temp != None :
                steps.append(temp)
                temp = temp.previous
            
            steps.reverse()
            return steps

        # Fill Jug 1
        if(current_state.jug1 < jug1):
            next_state = State(jug1, current_state.jug2, "Fill Jug 1")
            next_state.previous = current_state
            q.append(next_state)
        
        # Fill Jug 2
        if(current_state.jug2 < jug2):
            next_state = State(current_state.jug1, jug2, "Fill Jug 2")
            next_state.previous = current_state
            q.append(next_state)
            
        # Empty Jug 1
        if(current_state.jug1 > 0) :
            next_state = State(0, current_state.jug2, "Empty Jug 1")
            next_state.previous = current_state
            q.append(next_state)
        
        # Empty Jug 2
        if(current_state.jug2 > 0) :
            next_state = State(current_state.jug1, 0, "Empty Jug 2")
            next_state.previous = current_state
            q.append(next_state)
        
        # Pour water from Jug 1  to Jug 2 Until Jug 2 is Full
        if(current_state.jug1 + current_state.jug2 >= jug2 and  current_state.jug1 > 0):
            next_state = State(current_state.jug1 - (jug2 - current_state.jug2), jug2, "Pour water from Jug 1  to Jug 2 Until Jug 2 is Full")
            next_state.previous = current_state
            q.append(next_state)
            
        # Pour water from Jug 2 to Jug 1 Until Jug 1 is Full
        if(current_state.jug1 + current_state.jug2 >= jug1 and current_state.jug2 > 0):
            next_state = State(jug1, current_state.jug2 - (jug1 - current_state.jug1), "Pour water from Jug 2 to Jug 1 Until Jug 1 is Full")
            next_state.previous = current_state
            q.append(next_state)
        
        # Pour all the Water from Jug 1 to Jug 2
        if(current_state.jug1 + current_state.jug2 <= jug2 and current_state.jug1 > 0):
            next_state = State(0, current_state.jug1 + current_state.jug2, "Pour all the Water from Jug 1 to Jug 2")
            next_state.previous = current_state
            q.append(next_state)
        
        # Pour all the Water from Jug 2 to Jug 1
        if(current_state.jug1 + current_state.jug2 <= jug1 and current_state.jug2 > 0):
            next_state = State(current_state.jug1 + current_state.jug2, 0, "Pour all the Water from Jug 2 to Jug 1")
            next_state.previous = current_state
            q.append(next_state)
    
    return None
            
            
            

jug1_capacity = int(input("Enter the Capacity of Jug 1 : "))
jug2_capacity = int(input("Enter the Capacity of Jug 2 : "))
target = int(input("Enter the Target : "))

steps = solve_water_jug(jug1_capacity, jug2_capacity, target)

if(steps != None) :
    for step in steps:
        print(f"({step.jug1}, {step.jug2})  {step.comment}")
else:
    print("No Solution")