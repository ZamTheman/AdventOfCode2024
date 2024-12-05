filename = "./day5/inp.txt"
nums = []
sum = 0
with open(filename) as f:
    for line in f:
        if '|' in line:
            parts = line.split('|')
            nums.append([int(parts[0]), int(parts[1])])
        elif ',' in line:
            parts = [int(x) for x in line.split(',')]
            all_ok = True
            for num in nums:
                try:
                    index1 = parts.index(num[0])
                    index2 = parts.index(num[1])
                    if index1 > index2:
                        all_ok = False
                        break
                except ValueError:
                    # Index not in list so can be ignored
                    continue
            
            if all_ok:
                sum += parts[int(len(parts) / 2)]

print(sum)
