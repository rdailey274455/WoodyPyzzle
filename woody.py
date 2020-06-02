import random
import os

def piece_pic_to_coords(piece_pic):
    row=0
    col=0
    piece_coords=list()
    for ci in range(len(piece_pic)):
        if piece_pic[ci]=='N':
            row+=1
            col=0
        else:
            if piece_pic[ci]=='L':
                piece_coords.append((col,row))
            col+=1
    return piece_coords

pieces=list()
pieces.append([(0,0)])  # single block
# print('Loading L-shaped pieces . . .')
pieces.append(piece_pic_to_coords(
    'LLLN'+
    'L..N'+
    'L..N'))
pieces.append(piece_pic_to_coords(
    'LLLN'+
    '..LN'+
    '..LN'))
pieces.append(piece_pic_to_coords(
    '..LN'+
    '..LN'+
    'LLLN'))
pieces.append(piece_pic_to_coords(
    'L..N'+
    'L..N'+
    'LLLN'))
pieces.append(piece_pic_to_coords(
    'LLN'+
    'L.N'))
pieces.append(piece_pic_to_coords(
    'LLN'+
    '.LN'))
pieces.append(piece_pic_to_coords(
    '.LN'+
    'LLN'))
pieces.append(piece_pic_to_coords(
    'L.N'+
    'LLN'))
# print('Loading square pieces . . .')
pieces.append(piece_pic_to_coords(
    'LLLN'+
    'LLLN'+
    'LLLN'))
pieces.append(piece_pic_to_coords(
    'LLN'+
    'LLN'))
# print('Loading line pieces . . .')
pieces.append(piece_pic_to_coords(
    'LLLLLN'))
pieces.append(piece_pic_to_coords(
    'LN'+
    'LN'+
    'LN'+
    'LN'+
    'LN'))
pieces.append(piece_pic_to_coords(
    'LLLLN'))
pieces.append(piece_pic_to_coords(
    'LN'+
    'LN'+
    'LN'+
    'LN'))
pieces.append(piece_pic_to_coords(
    'LLLN'))
pieces.append(piece_pic_to_coords(
    'LN'+
    'LN'+
    'LN'))
pieces.append(piece_pic_to_coords(
    'LLN'))
pieces.append(piece_pic_to_coords(
    'LN'+
    'LN'))

block_empty='. '
block_full='[]'
block_overlap='><'
block_piece_origin='()'
block_piece_origin_small='o '

board_main=[[block_empty for c in range(10)] for r in range(10)]

def board_draw(board_lol,show_axes):
    board_string=str()
    for r in range(-1 if show_axes else 0,len(board_lol)):
        for c in range(-1 if show_axes else 0,len(board_lol[r])):
            if r==-1 and c==-1:
                board_string+='  '
            elif r==-1 and not c==-1:
                board_string+=str(c+1)+' ' if c+1<10 else str(c+1)  # board_string+=' '+chr(ord('A')+c)
            elif not r==-1 and c==-1:
                board_string+=' '+str(r+1) if r+1<10 else str(r+1)
            else:
                board_string+=board_lol[r][c]
        board_string+='\n'
    return board_string

def piece_draw(piece_coords):
    board_mini=[[block_empty for c in range(5)] for r in range(5)]
    piece_height=0
    piece_width=0
    for ti in range(len(piece_coords)):
        piece_height=max(piece_height,piece_coords[ti][1]+1)
        piece_width=max(piece_width,piece_coords[ti][0]+1)
    origin=(2-(piece_width+0)//2,2-(piece_height+0)//2)
    board_mini[origin[1]][origin[0]]=block_piece_origin_small
    for coord in piece_coords:
        # print('x:'+str(origin[0]+coord[0])+', y:'+str(origin[1]+coord[1]))
        board_mini[origin[1]+coord[1]][origin[0]+coord[0]]=block_piece_origin if coord[0]==0 and coord[1]==0 else block_full
    return board_mini

def str_pad_cell(s,l,pad_char,pad_left,pad_right):
    if not pad_left and not pad_right:
        return s
    left_has_been_padded=False
    while len(s)<l:
        if pad_left and pad_right:
            s=s+pad_char if left_has_been_padded else pad_char+s
            left_has_been_padded=not left_has_been_padded
        elif pad_left and not pad_right:
            s=pad_char+s
        elif not pad_left and pad_right:
            s=s+pad_char
    return s

def str_side_by_side(s1,s2):
    s1l=s1.split('\n')
    s2l=s2.split('\n')
    s3=str()
    while len(s1l)>0 or len(s2l)>0:
        if len(s1l)>0:
            s3+=s1l.pop(0)
        if len(s2l)>0:
            s3+=s2l.pop(0)
        if len(s1l)>0 and len(s2l)>0:
            s3+='\n'
    return s3

hand=list()

def hand_deal(hand_list,pieces_lol,count):
    for i in range(count):
        hand_list.append(random.randrange(len(pieces_lol)))

# print(board_draw(board_main,True))
# for piece in pieces:
    # print(board_draw(piece_draw(piece),False))

hand_deal(hand,pieces,3)
# print(str_side_by_side(str_side_by_side(
    # board_draw(piece_draw(pieces[hand[0]]),False),
    # board_draw(piece_draw(pieces[hand[1]]),False)),
    # board_draw(piece_draw(pieces[hand[2]]),False)))

# main game loop
while True:
    _=os.system('cls')
    # draw board
    print(board_draw(board_main,True))
    # draw hand
    print(str_side_by_side(str_side_by_side(
        board_draw(piece_draw(pieces[hand[0]]),False),
        board_draw(piece_draw(pieces[hand[1]]),False)),
        board_draw(piece_draw(pieces[hand[2]]),False)))
    # draw hand options (still need to accomodate less than three pieces in hand)
    print(str_pad_cell('1',10,' ',True,True)+str_pad_cell('2',10,' ',True,True)+str_pad_cell('3',10,' ',True,True))
    # choose piece to place
    choice_piece=int(input('Which piece would you like to place? '))-1
    choice_r=int(input('Which row? '))-1
    choice_c=int(input('Which column? '))-1
    # draw board with hovering piece, warn about invalid positions (include coord choosing in while loop)
    choice_placement_confirm=input('Confirm (y/n)? ')
    