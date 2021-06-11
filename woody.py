class Coord:
    def __init__(self, _x = 0, _y = 0):
        self.x = _x
        self.y = _y

class Piece:
    def __init__(self, _shape = 'square', _size = 1):
        self.__blocks = list()
        self.__shape = _shape
        self.__size = _size
        self.__build()
        
    def __build(self):
        self.__blocks.append(Coord(0, 0))
        # single-block pieces
        if self.__size = 1:
            self.__shape = 'single'  # just to make sure
        else:
            # square-shaped pieces
            if self.__shape = 'square':
                for x in range(self.__size):
                    for y in range(self.__size):
                        if x != 0 and y != 0:  # skip single block
                            self.__blocks.append(Coord(x, y))
            # L-shaped and I-shaped pieces
            # L-shaped pieces are basically I-shaped pieces with an extra arm
            # number in self.__shape[1] represents direction:
            # 0 is right, 1 is up, 2 is left, 3 is down
            elif self.__shape in ('L0', 'L1', 'L2', 'L3', 'I1', 'I2', 'I3', 'I4'):
                for i in range(1, self.__size):
                    dir = int(self.__shape[1])
                    armCount = {'L': 2, 'I': 1}[self.__shape[0]]
                    while armCount > 0:
                        if dir == 0:
                            self.__blocks.append(i, 0)
                        elif dir == 1:
                            self.__blocks.append(0, i)
                        elif dir == 2:
                            self.__blocks.append(-i, 0)
                        elif dir == 3:
                            self.__blocks.append(0, -i)
                        # prepare for next arm
                        dir = dir + 1 if dir < 3 else 0  # 3 is max valid value
                        armCount -= 1
                    