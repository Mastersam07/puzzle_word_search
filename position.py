#Author: Mastersam
#Python 3.5 was used in the development
#---------------------
#-----------------------------

class position:
    """
    Represents a position in an array of words.
    """

    def __init__(self, chars, p, q):
        self.i = 0  # row
        self.j = 0  # col
        self.chars = chars # char array being searched
        self.p = p      # largest row index
        self.q = q      # largest col index

    def read_chars(self, file):

    def next_col(self):
        self.j += 1

    def next_row(self):
        self.i += 1

    def in_bounds(self):
        return (self.i >= 0) and (self.i <= self.p) and (self.i >= 0) and (self.i <=self.q)

