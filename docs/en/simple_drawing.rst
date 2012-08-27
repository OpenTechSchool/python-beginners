Simple drawing with turtle
**************************

Introduction
============

Turtle is like a drawing board.

It has functions like ``forward(...)`` and ``left(...)`` which can move the
turtle around::

    from turtle import *

.. image:: /images/default.png

::

    forward(25)

.. image:: /images/forward.png

::

    left(30)

.. image:: /images/left.png


The ``forward(...)`` function takes the number of pixels which you want to move
forward, ``left(...)`` takes a number of degrees which you want to rotate to
the left. (There are ``backward(...)`` and ``right(...)``, too.)

Drawing a square
================

Exercise
--------

Draw a square as in the following picture:

.. image:: /images/square.png

For a square you will probably need a right angle, which is 90 degrees.

Solution
--------

::

    from turtle import *

    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

.. note::

    As per convention, we want to terminate all figures in our starting
    position.  This will make it easier to draw multiple shapes later on.

Bonus
-----

If you want to get creative, you can modify your shape with the ``width(...)``
and ``color(...)`` functions.  If you cannot figure out the *signature* of a
function (that is the syntax and semantics of it, say, number of parameters and
their meaning) you can use ``help(color)``.

.. caution::

    If you misdrew anything, you can tell turtle to erase its drawing board with
    the ``reset()`` directive.

Drawing a rect
==============

Exercise
--------

Can you draw a (non-square) rectangle too?

.. image:: /images/rectangle.png

Solution
--------

::

    from turtle import *

    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)

Bonus
-----

How about a triangle?  (A triangle with 120 degrees angles will have all legs
equally sized.)


More squares
============

Exercise
--------

Now, draw a tilted square.  And another one, and another one.  You can
experiment with the angles between the individual squares.

.. image:: /images/tiltedsquares.png

Try 20, 90 and 180 for example.

Solution
--------

::

    from turtle import *

    left(20)     # <--

    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

    left(20)     # <--

    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

    left(20)     # <--

    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)


