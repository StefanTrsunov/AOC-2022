ans = 0
with open("input_file_name") as f:
    for line in f:
        first,second = line.split(',')
        f1,s1 = first.split('-')
        f2,s2 = second.split('-')
        numbers = [int(s) for s in [f1,s1,f2,s2]]
        if numbers[0] <= numbers[2] and numbers[3] <= numbers[1] or numbers[2] <= numbers[0] and numbers[1] <= numbers[3]:
            ans += 1
print(ans)