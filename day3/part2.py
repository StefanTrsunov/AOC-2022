dict = {chr(i+96):i for i in range(1,27)}
uppercase = {chr(j+38):j for j in range(27,53)}
dict.update(uppercase)
elf = []
found = []
with open("input_file_name") as f:
    lines = [line.strip() for line in f]

for i in range(0, len(lines), 3):
    elf.append(lines[i:i + 3])

for a in range(len(elf)):
    first = elf[a][0]
    second = elf[a][1]
    third = elf[a][2]
    for i in range(len(first)):
        for j in range(len(second)):
            for k in range(len(third)):
                if first[i] == second[j] == third[k]:
                    found.append(first[i])
                    break
            else:
                continue
            break
        else:
            continue
        break
value = 0
print(found)
for i in range(len(found)):
    value += int(dict.get(f"{found[i]}"))
print(value)