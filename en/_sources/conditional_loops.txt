Conditional Loops
*****************

Introduction
============

Conditional loops are way to repeat something until a certain condition is met.
If the condition is never met, the loop can become infinite. In Python
conditional loops are defined with the ``while`` statement::

    counter = 0
    while counter < 10:
        print "in the loop"
        counter += 1

Move until condition is met
===========================

Exercise
--------

Use the ``while`` loop to move the turtle forward until it reaches the end of
the window. 

Solution
--------

::

    def move_to_window_border(distance):
        while turtle.xcor() + distance < turtle.window_width() / 2:
            turtle.forward(distance)

Bonus
-----

Can you make the turtle move exactly to the window border?

Draw a spiral
=============

Loops can be interrupted with the ``break`` statement. This is often used in
combination with infinite loops.

Exercise
--------

Write a ``while`` loop with a condition that is always true to draw a spiral.
Interrupt the loop when the turtle reaches a certain distance from the center.
Use the function ``turtle.distance(x, y)`` to get the turtle's distance to the
point defined by the coordinates ``x`` and ``y``.

.. note::

   To draw a spiral, the turtle has to rotate by a constant value and move
   forward by an increasing value in each repetition.
            
Solution
--------

::

    def draw_spiral(radius):
        speed = 1
        while True:
            turtle.forward(speed)
            turtle.left(10)
            speed += 0.1
            if turtle.distance(0, 0) > radius:
                break

