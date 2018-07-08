#Author: Mastersam
#Python 3.5 was used in the development
#--------------------
from math import *
words = open('sheet1.txt', 'r')
find = open('find.txt', 'r')
repl = open('empty.txt', 'r')
w = words.readlines()
f = find.readlines()
r = repl.readlines()
words.close()
find.close()
repl.close()

#   i: row index of w
#   j: collumn index of w

#   a: row index of f
#   b: collumn index of f

#   k: direction index. see incr_index function

def ch_char(a, b, i, j):
    if f[a][b] == w[i][j]:
        return True
    else: return False

### Find initial match
def search(a, b, i, j, k):
    while in_bounds(a, 0, i, j, 0):
        search_in(a, b, i, j)
        if j == len(w[i]) - 2: # -2 because of '\n's at the end.
            j = 0
            i += 1
        elif j < len(w[i]):
            j += 1

### Check initial match
def search_in(a, b, i, j):
    while a < len(f):
        if ch_char(a, 0, i, j):
            search_sp(a, 0, i, j)
        a += 1

### Check if any words follow initial match
def search_sp(a, b, i, j):
    k = 0
    tmp = []
    s = False   # s: if word was found
    a0, b0, i0, j0 = a, b, i, j
    while k < 8:
        while in_bounds(a, b, i, j, k) and ch_char(a, b, i, j):
            tmp.append([w[i][j], i, j])
            b1, i1, j1 = b, i, j
            b, i, j = incr_index(b, i, j, k)
        if len(tmp) == (len(f[a]) - 1):
            write_found(tmp)
        tmp = []
        a, b, i, j = a0, b0, i0, j0
        k += 1

def write_found(tmp):
    for l in range(len(tmp)):
        rt = tmp[l][0]
        it = tmp[l][1]
        jt = tmp[l][2]
        r[it][jt] = str(rt)

def in_bounds(a, b, i, j, k):
    if (a < len(f)):
        return (b < len(f[a]) - 1) and (i >= 0) and (i < len(w)) and (j >= 0) and (j < len(w[0]) - 1)
    return False
            
def ch_word(a, b, i, j, k):
    while ch_char(a, b, i, j) and in_bounds(a, b, i, j, k):
        f[a][b] = w[i][j]
        b, i, j = incr_index(a, b, i, j, k)

def ch_all(a, b, i, j):
    while (ch_char(a, b, i, j) == False) and in_bounds(a, b, i, j, 0):
        a = a + 1
    return a
        
def incr_index(b, i, j, k):
    if k == 0:
        return b + 1, i, j + 1
    elif k == 1:
        return b + 1, i + 1, j + 1
    elif k == 2:
        return b + 1, i + 1, j
    elif k == 3:
        return b + 1, i + 1, j - 1
    elif k == 4:
        return b + 1, i, j - 1
    elif k == 5:
        return b + 1, i - 1, j - 1
    elif k == 6:
        return b + 1, i - 1, j
    elif k == 7:
        return b + 1, i - 1, j + 1

def str_to_char(f):
    for i in range(len(f)):
        f[i] = list(f[i])
    return f


r = str_to_char(r)
search(0, 0, 0, 0, 0)

repl = open('found.txt', 'w')
for i in range(len(r)):
    for j in range(len(r[i])):
        repl.write(str(r[i][j]))
repl.close()
