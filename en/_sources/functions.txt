User-defined funtions
*********************

Introduction
============

There is still a lot of duplicated code --- the actual drawing of the rectangle
--- around. If you need to copy and paste code, that is usually a sign of
lacking abstractions. (Programmers call it a *code smell.*)

Functions are one way to express abstractions in Python. Let's take
``turtle.reset()`` for example. It is actually an abstraction for a number of
steps, namely:

* Erase the drawing board
* Set the width and color back to default
* Move the turtle back to its initial position

A function can be defined with the ``def`` keyword in Python::

    def line_without_moving():
        turtle.forward(50)
        turtle.backward(50)

You can access names in functions as well::

    size = 50
    def line_without_moving():
        turtle.forward(size)
        turtle.backward(size)

.. note:: Python uses *whitespaces to identify blocks of code* belonging together. While other languages use special characters (like curly brackets) in python a block is introduced with a colon at the end of the line and commands within a deeper identation level - ususally 4 spaces. The block ends with the first line with a lesser identation level.

A function for a square
=======================

Exercise
--------

Write a function that draws a square. Can you see how you could improve the
tilted squares program with that and greatly relieve experimentation?


A function for a hexagon
========================

Exercise
--------

Write a function that draws a hexagon.

.. image:: /images/hexagon.png

Now combine that function into a honeycomb.

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

