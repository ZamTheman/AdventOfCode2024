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
    
def print_shadow_map(shadow_map):
    for line in shadow_map:
        for char in line:
            print(char, end="")

        print()

filename = "./day6/inp.txt"
map = []
shadow_map = []
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
        head = get_next_head(head)
        (next_x, next_y) = get_next(pos_x, pos_y, head)

    pos_x = next_x
    pos_y = next_y
    shadow_map[pos_y][pos_x] = 'o'
    print(f"{pos_x}, {pos_y}")
    # print_shadow_map(shadow_map)

visited = 0
for line in shadow_map:
    for char in line:
        if char == 'o':
            visited += 1

print(visited)

