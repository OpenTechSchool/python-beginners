Loops
*****

Introduction
============

One more thing: Our programs often featured repetition. There is a powerful
concept in Python called looping, which we will elaborate later on. For now,
take this easy example::

    for i in range(10):
        print("Hello!")

Drawing a dashed line
=====================

Exercise
--------

Draw a dashed line.  You can move the turtle without tracing a line behind you
with the ``turtle.penup()`` function;  put it back on the ground with
``turtle.pendown()``.

.. image:: /images/dashed.png

Solution
--------

::

    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

Bonus
-----

Can you make the dashes become larger as the line progresses?

.. image:: /images/dashedprogressing.png

Honeycomb loops
===============

Exercise
--------

Take your honeycomb program and make it easier with loops. How small can you
get it?

Solution
--------

::

    def hexagon():
        for i in range(6):
            turtle.forward(100)
            turtle.left(60)

    for i in range(6):
        hexagon()
        turtle.forward(100)
        turtle.right(60)
