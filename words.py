from board import *
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

def main():
    starts = []
    b = Board(7)
    print(b)
    print("done")
    for row in range(b.size):
        for col in range(b.size):
            i = row*b.size+col
            dirs = set()
            if not b.squares[i].get_fill():
                if row==0:
                    #-1=down
                    dirs.add(-1)
                if col==0:
                    #1=right
                    dirs.add(1)
                if i-b.size>=0 and b.squares[i-b.size].get_fill():
                    dirs.add(-1)
                if i-1>=0 and b.squares[i-1].get_fill():
                    dirs.add(1)
            if len(dirs)!=0:
                starts.append((i,dirs))
    print(starts)


if __name__ == "__main__":
    main()