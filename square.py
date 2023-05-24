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
