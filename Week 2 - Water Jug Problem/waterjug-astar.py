import heapq

def heuristic (jug1_value, jug2_value, target) :
    h = min(abs(jug1_value - target), abs(jug2_value - target))
    return h

def solve_waterjug_astar(jug1, jug2, target) :
    pq = []
    
    closed_set = set()
    
    init_g = 0
    init_h = heuristic(0, 0, target)
    
    init_f = init_g + init_h
    
    heapq.heappush(pq, (init_f, init_g, 0, 0, None, "Initial State"))
    
    while len(pq) != 0 :
        
        current = heapq.heappop(pq)
        
        current_g = current[1]
        
        x = current[2]
        y = current[3]
        
        if x == target or y == target :
            
            
            temp = current
            
            steps = []
            
            if (x == target and y != 0) :
                steps.append((x, 0, "Empty Jug 2"))
            
            if (y == target and x != 0) :
                steps.append((0, y, "Empty Jug 1"))    
            
            
            while temp is not None :
                steps.append((temp[2], temp[3], temp[5]))
                temp = temp[4]
    
            steps.reverse()            

            return steps
        
        closed_set.add((x, y))
        
        next_g = current_g + 1
        
        # Fill Jug 1
        
        if x < jug1 :
            next_x = jug1
            next_y = y
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Fill Jug 1"))
            
        # Fill Jug 2
        
        if y < jug2 :
            next_x = x
            next_y = jug2
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Fill Jug 2"))
        
        # Empty Jug 1
        
        if x > 0 :
            next_x = 0
            next_y = y
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Empty Jug 1"))
        
        # Empty Jug 2
        
        if y > 0 :
            next_x = x
            next_y = 0
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Empty Jug 2"))
        
        # Pour water from Jug 2 to Jug 1 Until Jug 1 is Full
        
        if x + y >= jug1 and y > 0 :
            next_x = jug1
            next_y = y - (jug1- x)
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Pour Water from Jug 2 to Jug 1 Until Jug 1 is Full"))
        
        # Pour water from Jug 1 to Jug 2 Until Jug 2 is Full
        
        if x + y >= jug2 and x > 0 :
            next_x = x - (jug2 - y)
            next_y = jug2
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Pour Water from Jug 1 to Jug 2 Until Jug 2 is Full"))
        
        # Pour all water from Jug 2 to Jug 1
        
        if x + y <= jug1 and y > 0 :
            next_x = x + y
            next_y = 0
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Pour all Water from Jug 2 to Jug 1"))
        
        # Pour all water from Jug 1 to Jug 2
        
        if x + y <= jug2 and x > 0 :
            next_x = 0
            next_y = x + y
            next_f = next_g + heuristic(next_x, next_y, target)
            
            heapq.heappush(pq, (next_f, next_g, next_x, next_y, current, "Pour all Water from Jug 1 to Jug 2"))
    
    return None


jug1_capacity = int(input("Enter the Capacity of Jug 1 : "))
jug2_capacity = int(input("Enter the Capacity of Jug 2 : "))
target = int(input("Enter the Target : "))

steps = solve_waterjug_astar(jug1_capacity, jug2_capacity, target)

if steps is not None :
    
    for i in range(len(steps)) :
        step = steps[i]
        print(f"Step {i} : {step[2]} ({step[0]}, {step[1]})")