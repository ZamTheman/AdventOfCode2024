filename = "./day1/inp.txt"
sum = 0
first_list = []
second_list_occurancies = dict()
with open(filename) as f:
    for line in f:
        inputs = line.strip().split()
        first_list.append(int(inputs[0]))
        if int(inputs[1]) in second_list_occurancies:
            second_list_occurancies[int(inputs[1])] += 1
        else:
            second_list_occurancies[int(inputs[1])] = 1

for i in range(len(first_list)):
    multiplyer = 0
    if first_list[i] in second_list_occurancies:
        multiplyer = second_list_occurancies[first_list[i]]

    sum += first_list[i] * multiplyer

print(sum)