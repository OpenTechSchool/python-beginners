Conditional statements
**********************

Introduction
============

So far we have accomplished predefined tasks, but in all honesty we were accomplishing no better achievements than the 18th century automata, or the music boxes following one set of instruction to the end. What makes programming so much more powerful are conditional statements. This is the ability to *test* a variable against a value and act in one way if the condition is met by the variable or an other way if not. They are also commonly called by programmers *if statements*.

To know if a condition is *True* of *False*, we need a new type of data: 
the booleans. They allow logical operations. 
A logic statement or operation can be evaluated to be *True* or *False*.
Our conditional statement can then be understood like this: 

**if** *(evaluation of a condition returns true)* **then** *do some operation*
**else** *do an other operation*. And any operation that can be evaluated as
*True* or *False* can be put to the test. All comparisons return *True* or
*False*: ``==``, ``>``, ``<``.

Examples
========

Here are some simple examples::

    condition = True
    if condition:
        print("condition met")

    if not condition:
        print("condition not met")

    direction = -30
    if direction > 0 :
        turtle.forward(direction)
    else:
        turtle.left(180)
        turtle.forward(-direction)

Go forward, but not too much
============================

Exercise
--------

Let's try to make our turtle stop when it reaches the end of the window.  For
now, we will only take horizontal movements into account.  We want the turtle
to go forward for a specified distance (taken as a function parameter) until it
reaches this distance and stops.

.. note::

  * We start from the center of the screen, which has coordinate (0;0)
  * We can get the x coordinate of our turtle with the function ``turtle.xcor()``
  * We can get the width of the screen with the function ``turtle.window_width()``

Solution
--------

::

    def stop_at_end_of_screen(distance):
        future_x_coord = turtle.xcor() + distance
        diff = turtle.window_width()/2 - future_x_coord
        if  diff > 0 :
            turtle.forward(distance)
        else:
            turtle.forward(turtle.window_width()/2 - turtle.xcor())

Bonus exercise
--------------

Now when the turtle reaches the end of the screen, it turns around and 
continue its movement in the other direction, the remaining of the distance

.. note:: ``turtle.heading()`` gives you the current angle the turtle's
   direction makes with the original east facing turtle. A turtle going
   straight up has a heading of 90 degrees.

Solution
--------

::

    def uturn_at_border(distance):
        if turtle.heading() == 0 :
            future_x_coord = turtle.xcor() + distance
        else:
            future_x_coord = turtle.xcor() - distance
        diff = turtle.window_width()/2 - future_x_coord
        if  diff > 0 :
            turtle.forward(distance)
        else:
            turtle.forward(turtle.window_width()/2 - turtle.xcor())
            turtle.left(180)
            turtle.forward(-diff)
        
