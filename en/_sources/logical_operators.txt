Logical operators
*****************

Introduction
============

Conditionals are a nice way to make decisions by asking if something equals
True or not. But often one condition is not enough. 
We may want to take the opposite of our result. Or for instance if we want to
make a decision upon ``turtle.xcor()`` and ``turtle.ycor()`` we have to combine
them. This can be done with logical operators. 

Negation of a statement
=======================

We can take the opposite value of a statement to use ``not`` its value.
It is a logical operator::

    x = False
    if not x :
        print("conditon met")
    else:
        print("condition not met")

Exercise
--------

The turtle gives us a useful function to know if it is drawing or not: ``turtle.isdown()``.
This function returns *True* if the turtle is drawing. As we have seen earlier, the function
``turtle.penup()`` and ``turtle.pendown()`` toggle between writing while moving,
or just moving without a trace.

Can we write a function that only goes forward if the pen is up?

Solution
--------

::

    def stealthed_forward(distance):
        if not turtle.isdown():
            turtle.forward(distance)


This and that or something else
===============================

Two easy to understand operators are ``and`` and ``or``. They do exactly what
they sound like: combine two statements in a way both have be true (``and``) or
at least one of them has to be true (``or``)::

    if 1 < 2 and 4 > 2:
        print("condition met")

    if 1 > 2 and 4 < 10:
        print("condition not met")

    if 4 < 10 or 1 < 2:
        print("condition met")

You are not restricted to one logical operator. You can combine as may as you
want.

Exercise
--------

Create a function that accepts the argument ``angle`` and moves the turtle
forward into that direction until either the vertical or horizontal distance to
the center exceeds 100.

Solution
--------

::

    def move_to_square_border(angle):
        turtle.left(angle)
        x = turtle.xcor()
        y = turtle.ycor()
        while x > -100 and x < 100 and y > -100 and y < 100:
            turtle.forward(10)
            x = turtle.xcor()
            y = turtle.ycor()

Bonus
-----

Can you use this to draw a star?
