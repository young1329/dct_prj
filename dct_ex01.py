'''
8x8 matrix dct
'''

from __future__ import division
from math import *

def index(x,y):
    return y*8+x
    
def show(heading,values):
    print heading
    for y in range(8):
        print 'y=%d '%y,
        for x in range(8):
            value = values[index(x,y)]
            print '%9.3f'%value,
        print
        
def showf(heading,func):
    print heading
    for y in range(8):
        print 'y=%d   '%y,
        for x in range(8):
            value = func(x,y)
            print '%9.3f'%value,
        print
        
def alpha(u):
    return sqrt(1./8) if u==0 else sqrt(2./8)
    
g = [x-128 for x in 
    52, 55, 61,66, 70, 61, 64, 73,
    63, 59, 55, 90, 109, 85, 69, 72,
    62, 59, 68, 113, 144, 104, 66, 73,
    63, 58, 71, 122, 154, 106, 70, 69,
    67, 61, 68, 104, 126, 88, 68, 70,
    79, 65, 60, 70, 77, 68, 58, 75,
    85, 71, 64, 59, 55, 61, 65, 83,
    87, 79, 69, 68, 65, 76, 78, 94,
]

show('g',g)

def get_g(x,y):
    return g[index(x,y)]


def get_G(u,v):
    return sum(
        alpha(u) * alpha(v) * get_g(x,y) * cos(pi/8 * (x+0.5)*u) *
        cos(pi/8*(y+0.5)*v)
        for y in range(8)
        for x in range(8)
    )
    
G=[
    get_G(u,v) for v in range (8) for u in range(8)
]

showf('G',get_G)

def get_B(u,v):
    v=get_G(u,v)
    return floor(v)


def get_f(x,y):
    return sum(
        alpha(u)*alpha(v)*get_B(u,v)*cos(pi/8*(x+0.5)*u)*cos(pi/8*(y+0.5)*v)
        for u in range(8) for v in range(8)
    )

showf('f',get_f)