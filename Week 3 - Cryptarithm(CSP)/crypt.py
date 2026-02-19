def getCandidates(char, mapping, leading, used) :
    if char is None : return [0]
    if char in mapping : return [mapping[char]]
    
    candidates = []
    
    for i in range(10) :
        if i in used : continue
        if i == 0 and char in leading : continue
        
        candidates.append(i)
        
    return candidates


def find_mapping(word1, word2, result, mapping, used, leading, carry, column, max_col) :
    
    if column == max_col :
        return carry == 0
    
    char1 = None if len(word1) <= column else word1[column]
    char2 = None if len(word2) <= column else word2[column]
    charR = None if len(result) <= column else result[column]
    
    for val1 in getCandidates(char1, mapping, leading, used) :
        assigned1 = False
        
        if char1 is not None and char1 not in mapping :
            assigned1 = True
            mapping[char1] = val1
            used.add(val1)
            
        for val2 in getCandidates(char2, mapping, leading, used) :
            assigned2 = False
            
            if char2 is not None and char2 not in mapping :
                assigned2 = True
                mapping[char2] = val2
                used.add(val2)
                
            addition = val1 + val2 + carry
            
            base = addition % 10
            next_carry = addition // 10
            
            assignedR = False
            can_move_forward = False
            
            if base == 0 and charR in leading :
                if assigned2 :
                    mapping.pop(char2)
                    used.remove(val2)
                continue
            
            if charR in mapping :
                if mapping[charR] == base :
                    can_move_forward = True
            elif charR not in mapping and base not in used :
                assignedR = True
                can_move_forward = True
                mapping[charR] = base
                used.add(base)
            
            if can_move_forward : 
                found = find_mapping(word1, word2, result, mapping, used, leading, next_carry, column + 1, max_col)
                if found :
                    return True
            
            if assignedR :
                mapping.pop(charR)
                used.remove(base)
            
            if assigned2 :
                mapping.pop(char2)
                used.remove(val2)
                
        
        if assigned1 :
            mapping.pop(char1)
            used.remove(val1)
    
    return False
    
    
def solve_cryptarithm(word1, word2, result) :
    word1_reversed = word1[::-1]
    word2_reversed = word2[::-1]
    result_reversed = result[::-1]
    
    leading = set([word1[0], word2[0], result[0]])
    
    max_col = max(len(word1), len(word2), len(result))
    
    used = set()
    
    mapping = {}
    
    found = find_mapping(word1_reversed, word2_reversed, result_reversed, mapping, used, leading, 0, 0, max_col)
    
    if found :
        return mapping
    else :
        return None


def encode(word, mapping) :
    result = 0
    
    for i in range(len(word)) :
        result = result * 10 + mapping[word[i]]
    
    return result



def main () :
    
    word1 = input("Enter the first word : ")
    word2 = input("Enter the second word : ")
    
    result = input("Enter the result : ")
    
    mapping = solve_cryptarithm (word1.upper(), word2.upper(), result.upper())
    
    if mapping is not None :
        print(f"{word1.upper()} : {encode(word1.upper(), mapping)}")
        print(f"{word2.upper()} : {encode(word2.upper(), mapping)}")
        print(f"{result.upper()} : {encode(result.upper(), mapping)}")
    else : 
        print ("Cannot Decode")
    
main()