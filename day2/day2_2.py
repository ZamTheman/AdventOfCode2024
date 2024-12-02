filename = "./day2/inp.txt"

def validateArray(inputs):
    safe = True
    current = inputs[0]
    decreasing = inputs[1] < inputs[0]
    for i in range(len(inputs)):
        if i == 0:
            continue

        if decreasing:
            if inputs[i] >= current or current - inputs[i] > maxStep:
                safe = False
                break
        
        if not decreasing:
            if inputs[i] <= current or inputs[i] - current > maxStep:
                safe = False
                break

        current = inputs[i]

    return safe

nrSafes = 0
maxStep = 3
with open(filename) as f:
    for line in f:
        safe = True
        inputs = [int(x) for x in line.strip().split()]
        if validateArray(inputs):
            nrSafes += 1
            continue

        for i in range(len(inputs)):
            new_array = inputs[:i] + inputs[i+1:]
            if validateArray(new_array):
                nrSafes += 1
                break

print(nrSafes)