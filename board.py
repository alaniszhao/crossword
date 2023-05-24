import numpy as np
import random
from square import *
import copy
import time

class Board:
  def get_index(self, valid_indices, half):
  #returns an index to move in a direction from
    if(half==0):
    #upper half generation
      i=random.randint(0,self.size*2+self.size)
      while((valid_indices.get(i))%self.size in {1,2} or
           (valid_indices.get(i))//self.size in {1,2, self.size-2, self.size-3}
           or (i in self.filled)):
      #check that the index isn't too close to an edge, too close to the middle
      #check that the index isn't already filled
        i=random.randint(0,(self.size//2+1)**2)
      return valid_indices.get(i)
    #lower half generation
    i=random.randint((self.size//2+1)**2,len(valid_indices)-1)
    while((valid_indices.get(i))%self.size in {1,2} or
          (valid_indices.get(i))//self.size in {1,2, self.size-2, self.size-3}
          or (i in self.filled)):
      #checks same as above
      i=random.randint((self.size//2+1)**2,len(valid_indices)-1)
    return valid_indices.get(i)
  
  def count_squares(self):
    #return the number of filled squares
    return len(self.filled)
  
  def generate_dirs(self,half):
    #generates a direction to fill in based on the half
    #right: 0 means don't move horizontally
    #       1 means move horizontally to the right
    #up: 0 means don't move vertically
    #    1 means move down a row(current row + 1)
    #    -1 means move down a row(current row - 1)
    if(half==0):
      up = random.randint(0,1)
      right = random.randint(0,1)
      while(up==0 and right==0):
        #keep choosing so you don't fill single squares
        up = random.randint(0,1)
        right = random.randint(0,1)
      return (right, up)
    else:
      up = random.randint(-1,0)
      right = random.randint(0,1)
      while(up==0 and right==0):
        up = random.randint(-1,0)
        right = random.randint(0,1)
      return (right, up)
    
  def invalid_index(self,board):
    #checks if the current board has any word sizes of 1 or 2 which are invalid
    #all possible across/down words in valid crosswords have len >=3
    seen = 0
    last = 0
    for row in range(self.size):
      #across checks
      for col in range(self.size//2+1):
        index = row*self.size+col
        if(not board[index].get_fill()): 
          #increase the number of seen blank squares if curr square blank
          seen+=1
          last = seen
        elif(board[index].get_fill() and (seen==2 or seen==1)):
          #if you find a filled square and the current seen blanks are 1 or 2
          #the board is invalid
          return True
        elif(board[index].get_fill() and seen>=3):
          #if you see a filled but the word len >=3 then reset seen
          seen = 0
          last = seen
        else: 
          seen = 0
          last = seen
      seen=0
      if(last==1):
        #if the row ends and there is only 1 blank square(middle column) then
        #invalid
        return True
    seen=0
    for col in range(self.size//2+1):
      #down checks
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
      if(last==1 or last==2):
        #if the end of the row has 1 or 2 blanks, invalid puzzle
        return True
    return False
   
  def move_dir(self, poss_board, i, right, up):
    #move from index i in the corresponding direction
    num_moves = self.size//10+random.randint(1,3)
    #random # of moves
    indices = set()
    count = 0
    while(count<num_moves):
      index = i + count*right + count*up*self.size
      indices.add(index)
      if(index<=0 or index>=self.size**2-1):
        #out of range, can't move
        return (poss_board, False)
      poss_board[index].set_fill(True)
      #otherwise move as much as possible in the direction
      if(self.invalid_index(poss_board)):
        #if the board becomes invalid, undo all moves
        for curr in indices:
          if(curr not in self.filled):
            poss_board[curr].set_fill(False)
        return (poss_board, False)
      if(i%self.size>=self.size//2-1):
        #reach the middle, still valid
        for val in indices: #this adds all filled indices to the board set
          self.filled.add(val)
        return (poss_board, True)
      count+=1
    for val in indices:
      self.filled.add(val)
    return (poss_board, True)

  def clear(self,half):
    #clear the corresponding half when timout
    if(half==0):
      for row in range(self.size//2+1):
        for col in range(self.size//2+1):
          index = row*self.size+col
          #set all fills to false
          self.squares[index].set_fill(False)
          if(index in self.filled):
            #remove from the board set
            self.filled.remove(index)
    else:
      #same as above for the lower half
      for row in range(self.size//2+1,self.size):
        for col in range(self.size//2+1):
          index = row*self.size+col
          self.squares[index].set_fill(False)
          if(index in self.filled):
            self.filled.remove(index)

  def generate_fills(self, valid_indices):
    #generate the filled squares in the crossword
    num_squares = (self.size**2)//20
    count_squares = 0
    while(count_squares<num_squares):
      timeout = time.time() + self.size//2
      valid = False
      while(not valid): #keep generating until a valid half is created
        time.sleep(0.25)
        if time.time() > timeout:
          #sometimes an impossible board is generated, start over in this case
          self.clear(0)
          count_squares=0
          break
        index = self.get_index(valid_indices, 0)
        (right, up) = self.generate_dirs(0)
        poss_board = copy.deepcopy(self.squares)
        (new_board, valid) = self.move_dir(poss_board, index, right, up)
        #move the board in the selected direction
        #the original board will be returned in the move is invalid
        self.squares = new_board
        print("index: "+str(index))
        print("direction: ("+str(right)+","+str(up)+")")
        print(self)
        print("\n")
      count_squares = self.count_squares()
    first_half = count_squares
    count_squares = 0
    while(count_squares<num_squares):
      #same as above for the lower half
      timeout = time.time() + self.size//2
      valid = False
      while(not valid):
        time.sleep(0.25)
        if time.time() > timeout:
          self.clear(1)
          count_squares=0
          break
        index = self.get_index(valid_indices, 1)
        (right, up) = self.generate_dirs(1)
        poss_board = copy.deepcopy(self.squares)
        print("index: "+str(index))
        (new_board, valid) = self.move_dir(poss_board, index, right, up)
        self.squares = new_board
        print("direction: ("+str(right)+","+str(up)+")")
        print(self)
        print("\n")
      count_squares = self.count_squares()-first_half
    #flip the created half and duplicate on the other side for symmetricity
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
    self.filled = set()
    for i in range(size*size): #create an empty board
      self.squares.append(Square())
    limit = size//2 + 1
    valid = dict()
    index=0
    for i in range(size):
      #create a dict of all valid indices in the left half to fill
      for j in range(limit):
        valid.update({index: i*size+j})
        index+=1
    self.generate_fills(valid)

  def __str__(self): #_ means empty, # means filled
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
    x = Board(15)
    print(x)

if __name__ == "__main__":
    main()