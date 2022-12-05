ans = 0
with open("input_file_name") as f:
    for line in f:
        first,second = line.split(',')
        f1,s1 = first.split('-')
        f2,s2 = second.split('-')
        numbers = [int(s) for s in [f1,s1,f2,s2]]
        if not (numbers[1] < numbers[2] or numbers[3] < numbers[0]):
            ans += 1
print(ans)