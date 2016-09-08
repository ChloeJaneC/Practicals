read_file = open("numbers.txt", mode="r")
num_total = 0
for line in read_file:
    num_lines = int(line)
    num_total += num_lines
print(num_total)
read_file.close()
