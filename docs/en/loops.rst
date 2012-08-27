Loops
*****

Introduction
============

One more thing: Our programs often featured repetition. There is a powerful
concept in Python called looping, which we will elaborate later on. For now,
take that easy example::

    for i in range(10):
        print "Hello!"

Drawing a dashed line
=====================

Exercise
--------

Draw a dashed line.  You can move the turtle without tracing a line behind you
with the ``up()`` function;  put it back on the ground with ``down()``.

.. image:: /images/dashed.png

Solution

::

    for i in range(10):
        forward(15)
        up()
        forward(5)
        down()

Bonus
-----

Can you make the dashes become larger as the line progresses?

.. image:: /images/dashedprogressing.png

Honeycomb loops
===============

Exercise
--------

Take your honeycomb program and make it easier with loops.  How small can you
get it?

Solution
--------

::

    def hexagon():
        for i in range(6):
            forward(100)
            left(60)

    for i in range(6):
      hexagon()
      forward(100)
      right(60)
