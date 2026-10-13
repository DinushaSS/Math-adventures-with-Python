#######################
from turtle import *

shape("turtle")
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
done()
#######################

#######################
from turtle import *

shape("turtle")

for i in range(4):
    forward(100)
    right(90)
done()
#######################

#######################
# create function
from turtle import *

shape("turtle")


def square():
    for i in range(4):
        forward(100)
        right(90)


square()
done()
#######################
