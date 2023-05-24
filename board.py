import numpy as np
import random
from square import *
import copy
import time

class Board:
  def get_index(self, valid_indices, half):
    if(half==0):
      i=random.randint(0,self.size*2+self.size)
      while((valid_indices.get(i))%self.size in {1,2} or
          (valid_indices.get(i))//self.size in {1,2, self.size-2, self.size-3}
          or self.squares[i].get_fill()):
        i=random.randint(0,self.size//2+self.size)
      return valid_indices.get(i)
    i=random.randint(self.size*2+self.size,len(valid_indices)-1)
    while((valid_indices.get(i))%self.size in {1,2} or
          (valid_indices.get(i))//self.size in {1,2, self.size-2, self.size-3}):
      i=random.randint(self.size*2+self.size,len(valid_indices)-1)
    return valid_indices.get(i)
  
  def count_squares(self):
    count = 0
    for row in range(self.size):
      for col in range(self.size//2+1):
        index = row*self.size+col
        if(self.squares[index].get_fill()):
          count+=1
    return count
  
  def generate_dirs(self,half):
    if(half==0):
      up = random.randint(0,1)
      right = random.randint(0,1)
      while(up==0 and right==0):
        up = random.randint(0,1)
        right = random.randint(0,1)
      return (right, up)
    else:
      up = random.randint(-1,0)
      right = random.randint(0,1)
      while(not(up==0 and right==0)):
        up = random.randint(0,1)
        right = random.randint(0,1)
      return (right, up)
    
  def invalid_index(self,board):
    seen = 0
    last = 0
    for row in range(self.size):
      for col in range(self.size//2+1):
        index = row*self.size+col
        if(not board[index].get_fill()): 
          seen+=1
          last = seen
        elif(board[index].get_fill() and (seen==2 or seen==1)):
          return True
        elif(board[index].get_fill() and seen>=3):
          seen = 0
          last = seen
        else: 
          seen = 0
          last = seen
      seen=0
      if(last==1): return True
    seen=0
    for col in range(self.size//2+1):
      for row in range(self.size):
        index = row*self.size+col
        if(not board[index].get_fill()): 
          seen+=1
          last = seen
        elif(board[index].get_fill() and (seen==2 or seen==1)):
          return True
        elif(board[index].get_fill() and seen>=3):
          seen = 0
          last = seen
        else: 
          seen = 0
          last = seen
      seen=0
      if(last==1): return True
    return False
   
  def move_dir(self, poss_board, i, right, up):
    num_moves = self.size//10+random.randint(1,3)
    indices = set()
    count = 0
    while(count<num_moves):
      index = i + count*right + count*up*self.size
      indices.add(index)
      poss_board[index].set_fill(True)
      if(self.invalid_index(poss_board)):
        for curr in indices:
          poss_board[curr].set_fill(False)
        return (poss_board, False)
      if(i%self.size>=self.size//2-1):
        return (poss_board, True)
      count+=1
    return (poss_board, True)

    #fill lines in selected direction
    #return valid/invalid if the direction is wrong
    #return invalid if squares are too close

  def clear(self):
    for i in range(self.size*self.size):
      self.squares[i].set_fill(False)

  def generate_fills(self, valid_indices):
    num_squares = (self.size**2)//20
    count_squares = 0
    while(count_squares<num_squares):
      timeout = time.time() + 5
      valid = False
      while(not valid):
        time.sleep(0.25)
        if time.time() > timeout:
          self.clear()
          count_squares=0
          break
        index = self.get_index(valid_indices, 0)
        (right, up) = self.generate_dirs(0)
        poss_board = copy.deepcopy(self.squares)
        (new_board, valid) = self.move_dir(poss_board, index, right, up)
        self.squares = new_board
        print("index: "+str(index))
        print("direction: ("+str(right)+","+str(up)+")")
        print(self)
        print("\n")
      count_squares = self.count_squares()
    first_half = count_squares
    count_squares = 0
    while(count_squares<num_squares):
      timeout = time.time() + 5
      valid = False
      while(not valid):
        time.sleep(0.25)
        if time.time() > timeout:
          self.clear()
          count_squares=0
          break
        index = self.get_index(valid_indices, 1)
        (right, up) = self.generate_dirs(1)
        poss_board = copy.deepcopy(self.squares)
        (new_board, valid) = self.move_dir(poss_board, index, right, up)
        self.squares = new_board
        print("index: "+str(index))
        print("direction: ("+str(right)+","+str(up)+")")
        print(self)
        print("\n")
      count_squares = self.count_squares()-first_half
    for row in range(self.size):
      for col in range(self.size//2+1):
        new_row = self.size-1-row
        new_col = self.size-1-col
        index = row*self.size+col
        new_index = new_row*self.size+new_col
        value = self.squares[index].get_fill()
        self.squares[new_index].set_fill(value)
    return

  def __init__(self, size):
    if(size%2==0):
      raise Exception("Crosswords have odd length/widths!")
    self.squares=[]
    self.size = size
    for i in range(size*size):
      self.squares.append(Square())
    limit = size//2 + 1
    valid = dict()
    index=0
    for i in range(size):
      for j in range(limit):
        valid.update({index: i*size+j})
        index+=1
    self.generate_fills(valid)

  def __str__(self):
      vis = ""
      for i in range(self.size*self.size):
        if(i%self.size==0 and i!=0):
           vis = vis + "\n"
        square = self.squares[i]
        letter = square.get_val()
        if(square.get_fill()):
          vis = vis + "# "
        elif(letter==""):
          vis = vis + "_ "
        else:
          vis = vis + square.get_val()
      return vis
def main():
    x = Board(19)
    print(x)

if __name__ == "__main__":
    main()