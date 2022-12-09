start = [
    [],
    ["F", "H", "B", "V", "R", "Q", "D", "P"],
    ["L", "D", "z", "Q", "W", "V"],
    ["H", "L", "Z", "Q", "G", "R", "P", "C"],
    ["R", "D", "H", "F", "J", "V", "B"],
    ["Z", "W", "L", "C"],
    ["J", "R", "P", "N", "T", "G", "V", "M"],
    ["J", "R", "L", "V", "M", "B", "S"],
    ["D", "P", "J"],
    ["D", "C", "N", "W", "V"]
]
with open('input_file_name') as f:
    for line in f:
        numbers = [int(s) for s in line.split() if s.isdigit()]
        stack = numbers[0]
        move_from = numbers[1]
        move_to = numbers[2]
        movement_from = start[move_from][-stack:]
        start[move_to] = start[move_to] + list(reversed(movement_from))
        start[move_from] = start[move_from][:-stack]
        print(start)