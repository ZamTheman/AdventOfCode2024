def get_next(pos_x, pos_y, head):
    if head == 'n':
        return (pos_x, pos_y - 1)
    if head == 'e':
        return (pos_x + 1, pos_y)
    if head == 's':
        return (pos_x, pos_y + 1)
    if head == 'w':
        return (pos_x - 1, pos_y)
    
def get_next_head(head):
    if head == 'n':
        return 'e'
    if head == 'e':
        return 's'
    if head == 's':
        return 'w'
    if head == 'w':
        return 'n'
    
def print_shadow_map(shadow_map, map):
    for row in range(len(shadow_map)):
        for x in range(len(shadow_map[0])):
            if map[row][x] == '#':
                print('#', end="")
            else:
                print(shadow_map[row][x], end="")
        
        print()
    # for line in shadow_map:
    #     for char in line:
    #         print(char, end="")

filename = "./day6/inp_test.txt"
map = []
shadow_map = []
full_map = []
turning_points = []
pos_x = pos_y = 0
head = 'n'

with open(filename) as f:
    row_nr = 0
    for line in f:
        map.append(line)
        shadow_map.append([char for char in "." * len(line)])
        if '^' in line:
            pos_x = line.index('^')
            pos_y = row_nr
            shadow_map[pos_y][pos_x] = 'o'
 
        row_nr += 1

while pos_x > -1 and pos_x < len(map[0]) - 1 and pos_y > -1 and pos_y < len(map) - 1:
    (next_x, next_y) = get_next(pos_x, pos_y, head)
    while map[next_y][next_x] == '#':
        turning_points.append([pos_x, pos_y])
        shadow_map[pos_y][pos_x] = 's'
        head = get_next_head(head)
        (next_x, next_y) = get_next(pos_x, pos_y, head)

    pos_x = next_x
    pos_y = next_y
    shadow_map[pos_y][pos_x] = 'o'

print(len(turning_points))
for pair in turning_points:
    print(f"{pair[0]}, {pair[1]}")

print_shadow_map(shadow_map, map)

