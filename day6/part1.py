with open("input_file_name") as f:
    data = f.read()
for i in range(len(data)):
    if data[i+1] != data[i+2] and data[i+1] != data[i+3] and data[i+1] != data[i+4] and data[i+2] != data[i+3] and data[i+2] != data[i+4] and data[i+3] != data[i+4]:
        print(i+5)
        break