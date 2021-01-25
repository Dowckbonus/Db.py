filename = 'guest.txt'

with open(filename, 'a') as gs:
    gs.write('andrew\n')
    gs.write('bruce\n')
    gs.write('cindy\n')
    
with open(filename) as gs:
    lines = gs.readlines()
    for line in lines:
        print(line.title().rstrip())
