class Square:
  def __init__(self):
    self.filled = False
    self.selected = False
    self.letter = ""
    self.written = ""
  def get_val(self):
    return self.written
  def set_fill(self, set):
    self.filled = set
  def get_fill(self):
    return self.filled
  def set_letter(self,letter):
    #maybe needs some editing depending on how the user interacts with
    #the board
    self.written = letter
  def check_letter(self):
    return self.letter==self.written
