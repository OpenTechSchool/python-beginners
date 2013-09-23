Functions with parameters
*************************

Introduction
============

As we shrink down our code and add functions to remove duplication, we
are *factorizing* it. This is a good thing to do. But the functions we
have defined so far are not very flexible. The variables are defined
inside the function, so if we want to use a different angle or a
distance then we need to write a new function.

That is why we need to be able to give parameters, also called
*arguments*, to the function.  This way the *variables* in the
function can have different values each time we call the function:

Remember how we defined the function ``line_without_moving()`` in the previous
section::

    def line_without_moving():
        turtle.forward(50)
        turtle.backward(50)

We can improve it by giving it a parameter::

    def line_without_moving(length):
        turtle.forward(length)
        turtle.backward(length)

The parameter acts as a *variable* only known inside the function's definition.
We use the newly defined function by calling it with the value we want the
parameter to have like this::

    line_without_moving(50)
    line_without_moving(40)

We have been using functions with parameters since the beginning of the
tutorial with ``turtle.forward()``, ``turtle.left()``, etc... 

And we can put as many arguments (or parameters) as we want, separating them
with commas and giving them different names::

    def tilted_line_without_moving(length, angle):
        turtle.left(angle)
        turtle.forward(length)
        turtle.backward(length)


A parameterized function for a variable size hexagon
====================================================

Exercise
--------

Write a function that allows you to draw hexagons of any size you want, each
time you call the function.

A function of several parameters
================================

Exercise
--------

Write a function that draws a honeycomb with a variable number of hexagons, of
variable sizes.

Solution
--------

::
    
    def hexagon(size):
        for i in range(6):
            turtle.forward(size)
            turtle.left(60)
            
    def honeycomb(size, count):
        for i in range(count):
            hexagon(size)
            turtle.forward(size)
            turtle.right(60)

