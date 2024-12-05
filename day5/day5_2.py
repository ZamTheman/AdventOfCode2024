filename = "./day5/inp.txt"
nums = []
sum = 0
with open(filename) as f:
    for line in f:
        if '|' in line:
            parts = line.split('|')
            nums.append([int(parts[0]), int(parts[1])])
        elif ',' in line:
            all_ok = True
            parts = [int(x) for x in line.split(',')]
            i = 0
            while i < len(nums):
                try:
                    index1 = parts.index(nums[i][0])
                    index2 = parts.index(nums[i][1])
                    if index1 > index2:
                        temp = parts[index1]
                        parts[index1] = parts[index2]
                        parts[index2] = temp
                        i = 0
                        all_ok = False
                    else:
                        i += 1
                    
                except ValueError:
                    i += 1

            if not all_ok:
                sum += parts[int(len(parts) / 2)]

print(sum)
