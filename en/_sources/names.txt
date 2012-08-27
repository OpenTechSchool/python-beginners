Names
*****

Introduction
============

Whew. Experimenting with the angles requires you to change three different
places each time. Imagine you'd want to experiment with the square sizes, let
alone with rectangles! We can do better than that.

This is where names come into play: You can tell Python that from now on,
whenever you refer to a name, you actually mean something else. That concept
might be familiar from symbolic maths, where you would write: *Let x be 5.*
Then x*2 will obviously be 10. That's why those names are known as variables,
too.

In Python syntax, that very statement translates to::

    x = 5

After that statement, if you do ``print x``, it will actually output its value
--- 5.  You can well use that for turtle too::

    forward(x)

A variable called angle
=======================

Exercise
--------

If we have a variable called ``angle``, how could we use that to experiment
much faster with our tilted squares program?

Solution
--------

::

    from turtle import *
    angle = 20

    left(angle)

    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

    left(angle)
    # ...

Bonus
-----

Can you apply that principle to the size of the squares, too?

The house of santa claus
========================

Exercise
--------

Draw a house.

.. image:: /images/house.png

You can calculate the length of the diagonal line with Pythagoras. That value
is a good candidate for a name binding.


