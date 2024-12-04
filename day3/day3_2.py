import re

def get_substrings(s, intial):
    enabled = intial
    do = "do()"
    dont = "don't()"
    start = 0
    strings = []
    for i in range(len(s)):
        if s[i:i + len(do)] == do:
            i = i + len(do)
            if not enabled:
                start = i
                enabled = True

        if s[i:i + len(dont)] == dont:
            if enabled:
                strings.append(s[start:i])
                enabled = False

            i = i + len(dont)

    if enabled:
        strings.append(s[start:])

    return (strings, enabled)

filename = "./day3/inp.txt"
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
my_sum = 0
line_nr = 0
enabled = True
with open(filename) as f:
    for line in f:
        line_sum = 0
        line_nr += 1
        (substrings, end_state) = get_substrings(line, enabled)
        enabled = end_state
        print("line: " + str(line_nr))
        for substring in substrings:
            matches = re.findall(pattern, substring)
            print("substring nr matches: " + str(len(matches)))
            for first, second in matches:
                print(str(first) + " " + str(second))
                line_sum += int(first) * int(second)

        my_sum += line_sum
        print("line: " + str(line_sum))
        print("tot : " + str(my_sum))

print(my_sum)
