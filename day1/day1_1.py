filename = "./day1/inp_first.txt"
sum = 0
first_list = []
second_list = []
with open(filename) as f:
    for line in f:
        inputs = line.strip().split()
        first_list.append(int(inputs[0]))
        second_list.append(int(inputs[1]))

first_list.sort()
second_list.sort()

for i in range(len(first_list)):
    sum += abs(first_list[i] - second_list[i])

print(sum)