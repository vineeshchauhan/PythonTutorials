for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


for x in range(5):
    if x == 0 or x ==2:
        print('x'*5)
    elif x == 1 or x == 3 or x == 4:
        print('x' * 2)