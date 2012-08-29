Functions with parameters
*************************
Introduction
============

Now we know how to *factorize* this code a little. But functions as we have defined them so far are not flexible. The variables are defined inside the function, and we need to rewrite a whole function to change the value of an angle, or a distance in it.

That is why we need to be able to give parameters, or also called *arguments* so that *names* we use in the function can be used with different values each time we call the function:

Remember how we defined the function ``line_without_moving`` in the previous section::

    def line_without_moving():
        forward(50)
        backward(50)

We can improve it by giving it a parameter::

    def line_without_moving(length):
        forward(length)
        backward(length)

The parameter acts as a *name* only known inside the function's definition. We use the newly defined function by calling it with the value we want the parameter to have like this::

    line_without_moving(50)
    line_without_moving(40)

We have been using functions with parameters since the beginning of the tutorial with the *forward*, *left*, etc... 


And we can put as many arguments (or parameters) as we want, separating them with commas and giving them different names::

   def tilted_line_without_moving(length,angle):
        left(angle)
        forward(length)
        backward(length)


A parameterized function for a variable size hexagon
====================================================

Exercise
--------
Write a function that takes allows you to draw hexagons of any size you want, each time you call the function.



A function of several parameters
================================

Exercise
--------

Write a function that draws a honeycomb with a variable number of hexagons, of variable sizes


Solution
--------

::
    
    def hexagon(size):
        for i in range(6):
            forward(size)
            left(60)
            
    def honeycomb(size,count):
        for i in range(count):
            hexagon(size)
            forward(size)
            right(60)

