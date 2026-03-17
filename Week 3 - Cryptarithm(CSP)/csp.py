def decode(string, mapping):
    num = ""
    for ch in string:
        num += str(mapping[ch])
    return int(num)


def findMapping(mapping, input1, input2, output, i, keys, used, leading) :

    if i == len(keys) :
        
        result = decode(input1, mapping) + decode(input2, mapping)
        
        output_decoded = decode(output, mapping)
        
        if(result == output_decoded) :
            return True
        
        return False
    
    letter = keys[i]
    
    for j in range(10):
        if j in used :
            continue
        
        if j == 0 and letter in leading :
            continue
        
        mapping[letter] = j
        used.add(j)
        
        found = findMapping(mapping, input1, input2, output, i + 1, keys, used, leading)
        
        if(found) :
            return True
        
        used.remove(j)
        mapping[letter] = None
            
    return False


def solveCryptarithm(input1, input2, output):
    keys = list(set(input1 + input2 + output))
    
    mapping = {}
    
    leading = {input1[0], input2[0], output[0]}
    
    for key in keys:
        mapping[key] = None
    
    used = set()
    found = findMapping(mapping, input1, input2, output, 0, keys, used, leading)
    
    if found :
        return mapping
    
    return None

mapping = solveCryptarithm("BASE", "BALL", "GAMES")

if mapping is not None :
    print("Solution :")
    print("BASE " + str(decode("BASE", mapping)))
    print("BALL " + str(decode("BALL", mapping)))
    print("GAMES " + str(decode("GAMES", mapping)))
    
else:
    print("No Solution Found")