from board import *
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
w=[]
x=[]
y=[]
z=[]

total = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,z,y,z]

def fill_crossword(starts):
    words = []

def get_list(letter):
    if letter=="a":
        return a
    if letter=="b":
        return b
    if letter=="c":
        return c
    if letter=="d":
        return d
    if letter=="e":
        return e
    if letter=="f":
        return f
    if letter=="g":
        return g
    if letter=="h":
        return h
    if letter=="i":
        return i
    if letter=="j":
        return j
    if letter=="k":
        return k
    if letter=="l":
        return l
    if letter=="m":
        return m
    if letter=="n":
        return n
    if letter=="o":
        return o
    if letter=="p":
        return p
    if letter=="q":
        return q
    if letter=="r":
        return r
    if letter=="s":
        return s
    if letter=="t":
        return t
    if letter=="u":
        return u
    if letter=="v":
        return v
    if letter=="w":
        return w
    if letter=="x":
        return x
    if letter=="y":
        return y
    if letter=="z":
        return z

def search_word(beginning, l, used):
    invalid = set()
    if beginning == "":
        i = random.randint(0,25)
        curr = total[i]
        for word in curr:
            if len(word)==l:
                return word
        invalid.add(i)
        while(True):
            i = random.randint(0,25)
            while(i in invalid):
                i = random.randint(0,25)
            curr = total[i]
            for word in curr:
                if len(word)==l:
                    return word
            invalid.add(i)
    letter = get_list(beginning[0])
    for word in letter:
        if len(word)==l and beginning==word[:len(beginning)]:
            return word
    return None

def main():
    starts = []
    b = Board(7)
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
    fill_crossword(starts)


if __name__ == "__main__":
    main()