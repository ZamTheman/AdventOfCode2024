import re

filename = "./day4/inp.txt"
strings = []
with open(filename) as f:
    for line in f:
        strings.append(line)

word = "XMAS"
word_len = len(word)
start_x = start_y = word_len - 1
end_x = len(strings[0]) - word_len - 1
end_y = len(strings) - word_len
count = 0

for i in range(len(strings)):
    for j in range(len(strings[0])):
        if not strings[i][j] == 'X':
            continue

        left_ok = j >= start_x
        right_ok = j <= end_x
        top_ok = i >= start_y
        bottom_ok = i <= end_y
        if left_ok and top_ok and strings[i - 1][j - 1] == word[1] and strings[i - 2][j - 2] == word[2] and strings[i - 3][j - 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 0")
            count += 1
        if top_ok and strings[i - 1][j] == word[1] and strings[i - 2][j] == word[2] and strings[i - 3][j] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 1")
            count += 1
        if right_ok and top_ok and strings[i - 1][j + 1] == word[1] and strings[i - 2][j + 2] == word[2] and strings[i - 3][j + 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 2")
            count += 1
        if right_ok and strings[i][j + 1] == word[1] and strings[i][j + 2] == word[2] and strings[i][j + 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 3")
            count += 1
        if right_ok and bottom_ok and strings[i + 1][j + 1] == word[1] and strings[i + 2][j + 2] == word[2] and strings[i + 3][j + 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 4")
            count += 1
        if bottom_ok and strings[i + 1][j] == word[1] and strings[i + 2][j] == word[2] and strings[i + 3][j] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 5")
            count += 1
        if left_ok and bottom_ok and strings[i + 1][j - 1] == word[1] and strings[i + 2][j - 2] == word[2] and strings[i + 3][j - 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 6")
            count += 1
        if left_ok and strings[i][j - 1] == word[1] and strings[i][j - 2] == word[2] and strings[i][j - 3] == word[3]:
            print("i: " + str(i) + " j: " + str(j) + " 7")
            count += 1

print(count)
