def get_input():   
    with open("input_file_name") as f:
        lines = [line.strip() for line in f]
    return lines


def part1(lines):
    cycle = 0
    x = 1
    ans = 0
    for line in lines:
        words = line.split()
        if words[0] == 'noop':
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                ans += x * cycle
        elif words[0] == 'addx':
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                ans += x * cycle
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                ans += x * cycle
            x += int(words[1])
    return ans

def part2(lines):
    pass


print(part1(lines=get_input()))