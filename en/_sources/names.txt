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

    turtle.forward(x)


.. note:: You can not save numbers in variables, like we did here for "x", but
   you can actually save various kinds of things in them. A typical other thing
   you want to have store often is a "string" - a line of text. Strings are
   indicated with a starting and a leading \". You'll learn about this and
   other types, as those are called in Python, and what you can do with them
   later on.

A variable called angle
=======================

Exercise
--------

If we have a variable called ``angle``, how could we use that to experiment
much faster with our tilted squares program?

Solution
--------

::

    angle = 20

    turtle.left(angle)

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.left(angle)
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


