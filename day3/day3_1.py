import re

filename = "./day3/inp.txt"
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
my_sum = 0
with open(filename) as f:
    for line in f:
        matches = re.findall(pattern, line)
        for first, second in matches:
            my_sum += int(first) * int(second)

print(my_sum)
