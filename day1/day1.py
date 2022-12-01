data = []
with open("/home/stefan/personal/AOC-2022/day1/input.txt") as f:
    for line in f:
        line.split("\n")
        data.append(line)

elfs = []
sum = 0
for i in range(len(data)):
    if (data[i] != '\n'):
        sum+=int(data[i])
    else:
        elfs.append(sum)
        sum = 0
        continue

#Part 1 answer
print(max(elfs))

#Part 2 answer
elfs.sort(reverse=True)
print(elfs[0] + elfs[1] + elfs[2])