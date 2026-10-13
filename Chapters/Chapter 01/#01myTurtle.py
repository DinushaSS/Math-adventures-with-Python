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
speed(0)


def square():
    for i in range(4):
        forward(100)
        right(90)


# Shape using loop
for i in range(80):
    square()
    right(5)

done()
#######################
