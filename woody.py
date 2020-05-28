board=[[str() for i in range(10)] for i in range(10)]
pieces=list() # list of lists of tuples
piece_new=list()
print('Generating line pieces...')
for i in range(5):
    for d in ['u','d','l','r']:
        for x in range(i):
            if d=='u':
                piece_new.append((0,x))
            elif d=='d':
                piece_new.append((0,-x))
            elif d=='l':
                piece_new.append((-x,0))
            elif d=='r':
                piece_new.append((x,0))
    pieces.append(piece_new)
    piece_new=list()
print('Generating square pieces...')
for i in range(3):
    for x in range(i):
        for y in range(i):
            piece_new.append((x,y))
    pieces.append(piece_new)
    piece_new=list()
print('Generating L pieces...')