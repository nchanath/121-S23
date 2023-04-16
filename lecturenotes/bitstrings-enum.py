def generate_bitstrings(n):
    # Base case: return the empty string for n = 0
    if n == 0:
        return [""]
    
    # Recursive case: generate all bitstrings of length n-1 and add a 0 and a 1 to each of them
    bitstrings = []
    prev_bitstrings = generate_bitstrings(n-1)

    # print(prev_bitstrings)
    
    for s in prev_bitstrings:
        bitstrings.append(s + "0")
        bitstrings.append(s + "1")
    
    return bitstrings
