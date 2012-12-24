Simple drawing with turtle
**************************

Introduction
============

Turtle is like a drawing board. 

It has functions like ``turtle.forward(...)`` and ``turtle.left(...)`` which
can move the turtle around.

Before you can use turtle, you have to import it::

Note that these commands do not display anything yet because the turtle window vanishes, read along to see how to fix that.

    import turtle

.. image:: /images/default.png

::

    turtle.forward(25)

.. image:: /images/forward.png

::

    turtle.left(30)

.. image:: /images/left.png


The ``turtle.forward(...)`` function tells the turtle to move forward 
by the given distance. ``turtle.left(...)`` takes a number of degrees which you want
to rotate to the left. (There are ``turtle.backward(...)`` and
``turtle.right(...)``, too.)

If you put the commands into a file, you might have recognized that the turtle
window vanishes after the turtle finished its movement. To prevent that, just
put ``turtle.exitonclick()`` at the bottom of your file. Now the window stays
open until you click on it.

::

    import turtle

    turtle.forward(25)

    turtle.exitonclick()

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

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

.. note::

    As per convention, we want to terminate all figures in our starting
    position.  This will make it easier to draw multiple shapes later on.

Bonus
-----

If you want to get creative, you can modify your shape with the
``turtle.width(...)`` and ``turtle.color(...)`` functions.  If you cannot figure
out the *signature* of a function (that is the syntax and semantics of it, say,
number of parameters and their meaning) you can use ``help(turtle.color)``.

Press the :kdb:`q` key to exit the help again.

.. caution::

    If you misdrew anything, you can tell turtle to erase its drawing board
    with the ``turtle.reset()`` directive or undo the most recent step with
    ``turtle.undo()``.

.. tip::

   As you might have read in the help, you can modify the color with
   :samp:`turtle.color({colorstring})`.  These include but are not limited to
   "red," "green," and "violet."  See the `colors manual`__ for an extensive
   list.

   __ http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm

Drawing a rectangle
===================

Exercise
--------

Can you draw a (non-square) rectangle too?

.. image:: /images/rectangle.png

Solution
--------

::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

Bonus
-----

How about a triangle?  (A triangle with 120 degrees angles will have all sides
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

    turtle.left(20)     # <--

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.left(20)     # <--

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.left(20)     # <--

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


