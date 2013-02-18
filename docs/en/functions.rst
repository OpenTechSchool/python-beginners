User-defined functions
**********************

Introduction
============

There is still a lot of duplicated code --- the actual drawing of the rectangle
--- around. If you need to copy and paste code, that is usually a sign of
lacking abstractions. (Programmers call it a *code smell.*)

Functions are one way to express abstractions in Python. Let's take
``turtle.reset()`` for example. It is actually an abstraction for a number of
steps, namely:

* Erase the drawing board.
* Set the width and color back to default.
* Move the turtle back to its initial position.

A function can be defined with the ``def`` keyword in Python::

    def line_without_moving():
        turtle.forward(50)
        turtle.backward(50)

This function we defined is called ``line_without_moving`` and it is
an abstraction for two turtle steps - a move forward and a move
backward.

You can access variables in functions as well::

    size = 50
    def line_without_moving():
        turtle.forward(size)
        turtle.backward(size)

.. important::

   Python uses *identing with whitespace to identify blocks of code*
   that belong together. In Python a block (like the function
   definitions shown above) is introduced with a colon at the end of the
   line and subsequent commands are indented --- usually 4 spaces
   further in. The block ends with the first line that isn't indented.

   This is different to many other programming languages, which use
   special characters (like curly brackets ``{}``) to group blocks of
   code together.

   You can indent your blocks with either tabs or spaces, but if you
   use both tabs *and* spaces in the same file the Python interpreter
   will complain. Make sure to always use one or the other.

A function for a square
=======================

Exercise
--------

Write a function that draws a square. Could you use this function to improve the
tilted squares program? If you change the program to use a function, is it easier
to experiment with?

Solution
--------

::

    def tilted_square():
      turtle.left(angle)

      turtle.forward(50)
      turtle.left(90)
      turtle.forward(50)
      turtle.left(90)
      turtle.forward(50)
      turtle.left(90)
      turtle.forward(50)
      turtle.left(90)

    angle = 20            # <--
    tilted_square()
    tilted_square()
    tilted_square()


A function for a hexagon
========================

Exercise
--------

Write a function that draws a hexagon.

.. image:: /images/hexagon.png

Now combine that function into a honeycomb. Just make it with a single layer like this:

.. image:: /images/honeycomb.png

Solution
--------

::

    def hexagon():
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(60)
        turtle.forward(100)
        turtle.left(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

    hexagon()
    turtle.forward(100)
    turtle.right(60)

You could also put the ``turtle.forward(100); turtle.right(60)`` portion in the
function, but you better not call it ``hexagon`` in that case.  That's
misleading because it actually draws a hexagon and then advances to a position
where another hexagon would make sense in order to draw a honeycomb.  If you
ever wanted to reuse your hexagon function outside of honeycombs, that would be
confusing at least.
