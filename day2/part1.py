with open("input_file_name") as f:
    score = 0
    for line in f:  
        if line[0] == 'A':
            if line[2] == 'Y':
                score += 8
            if line[2] == 'X':
                score += 4
            if line[2] == 'Z':
                score += 3
        if line[0] == 'B':
            if line[2] == 'Y':
                score += 5
            if line[2] == 'X':
                score += 1
            if line[2] == 'Z':
                score += 9
        if line[0] == 'C':
            if line[2] == "Y":
                score += 2
            if line[2] == "X":
                score += 7
            if line[2] == 'Z':
                score += 6
print(score)