import heapq

board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "E"]
]

def manhatten(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def heuristic(initial_value, goal_value):
    est_moves = 0
    for i in range(len(initial_value)):
        if(initial_value[i] == "E"):
            continue
        cur = initial_value[i]
        goal_index = goal_value.index(cur)

        x1, y1 = i // 3, i % 3
        x2, y2 = goal_index // 3, goal_index % 3
        
        est_moves = est_moves + manhatten(x1, y1, x2, y2)
        
    return est_moves
        

def solve(initial_state, final_state):
    pq = []
    visited = set()
    
    init_g = 0
    init_f = heuristic(initial_state, final_state)
    
    heapq.heappush(pq, (init_f, init_g, initial_state, None))
    
    while len(pq) != 0 :
        current = heapq.heappop(pq)
        current_f = current[0]
        current_g = current[1]
        current_state = current[2]
        
        if(current_state in visited):
            continue
        
        if(current_state == final_state):
            temp = current
            path = []
            
            while temp != None :
                path.append(temp[2])
                temp = temp[3]

            path.reverse()
            
            return path

        visited.add(current_state)
        
        e_index = list(current_state).index("E")
        
        # Move the Empty Space Left
        if(e_index % 3 < 2):
            lst = list(current_state)
            lst[e_index], lst[e_index + 1] = lst[e_index + 1], lst[e_index]
            next_state = "".join(lst)
            
            if(next_state not in visited):
                next_g = current_g + 1
                next_f = next_g + heuristic(next_state, final_state)
                heapq.heappush(pq, (next_f, next_g, next_state, current)) 

        # Move the Empty Space Right
        if(e_index % 3 > 0):
            lst = list(current_state)
            lst[e_index], lst[e_index - 1] = lst[e_index - 1], lst[e_index]
            next_state = "".join(lst)
            
            if(next_state not in visited):
                next_g = current_g + 1
                next_f = next_g + heuristic(next_state, final_state)
                heapq.heappush(pq, (next_f, next_g, next_state, current))    
        
        # Move the Empty Space Up
        if(e_index - 3 >= 0):
            lst = list(current_state)
            lst[e_index], lst[e_index - 3] = lst[e_index - 3], lst[e_index]
            next_state = "".join(lst)
            
            if(next_state not in visited):
                next_g = current_g + 1
                next_f = next_g + heuristic(next_state, final_state)
                heapq.heappush(pq, (next_f, next_g, next_state, current))    
        
        # Move the Empty Space Down
        if(e_index + 3 <= 8):
            lst = list(current_state)
            lst[e_index], lst[e_index + 3] = lst[e_index + 3], lst[e_index]
            next_state = "".join(lst)
            
            if(next_state not in visited):
                next_g = current_g + 1
                next_f = next_g + heuristic(next_state, final_state)
                heapq.heappush(pq, (next_f, next_g, next_state, current))    
                
    return None
   

steps = solve("12345E678", "12345678E")

if steps is not None :
    for i in range(len(steps)):
        step = steps[i]
        print(f"Step {i} : \n")
        i = 0
        while i < len(step):
            string = ["[ "]
            for j in range(3):
                string.append(step[i + j])
                string.append(" ")
            string.append("]")
            print("".join(string))
            i = i + 3
        print('')