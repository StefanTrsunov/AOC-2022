dict = {chr(i+96):i for i in range(1,27)}
uppercase = {chr(j+38):j for j in range(27,53)}
dict.update(uppercase)
found = []
with open("input_file_name") as f:
    for line in f:
        first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]
        for i in range(len(first_compartment)):
            for j in range(len(second_compartment)):
                if first_compartment[i] == second_compartment[j]:
                    found.append(first_compartment[i])
                    break
            else:
                continue
            break
value = 0
for i in range(len(found)):
    value += int(dict.get(f"{found[i]}"))
print(value)