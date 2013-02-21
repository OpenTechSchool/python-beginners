Conditional Loops
*****************

Introduction
============

Conditional loops are way to repeat something until a certain condition is met.
If the condition is never met, the loop can become infinite. In Python
conditional loops are defined with the ``while`` statement::

    counter = 0
    while counter < 10:
        print("in the loop")
        counter = counter + 1


Turtle prison
=============

Exercise
--------

The turtle has been up to its usual tricks again, robbing liqour
stores and building up huge gambling debts. It's time for turtle to be
put into a box that it can't get out of.

Let's make a new version of ``forward()``. One that turns the turtle
around if it tries to go further than 100 from the origin. We'll need
a ``while`` loop, and some new turtle functions:

* ``turtle.distance(0,0)`` - Distance of the turtle from the origin
* ``turtle.towards(0,0)`` - The angle to get back to origin
* ``turtle.setheading(angle)`` - Directly set the turtle direction

Now you will need to implement the prison logic using the API calls
above, a ``while`` loop and a bit of conditional logic. It's a bit of
a stretch but keep at it! Don't be afraid to talk it out with a coach
or another student.


Solution
--------

::

  def forward(distance):
      while distance > 0:
          if turtle.distance(0,0) > 100:
              angle = turtle.towards(0,0)
              turtle.setheading(angle)
          turtle.forward(1)
          distance = distance - 1


Draw a spiral
=============

Loops can be interrupted with the ``break`` statement. This is
especially useful if you write an *infinite loop*, which is a loop
where the conditional is always *True*.

Exercise
--------

Write a ``while`` loop with a condition that is always *True* to draw a spiral.
Interrupt the loop when the turtle reaches a certain distance from the center.
Use the function ``turtle.distance(x, y)`` to get the turtle's distance to the
point defined by the coordinates ``x`` and ``y``.

To do this you will need the ``turtle.xcor()`` and ``turtle.ycor()``
functions, which return the position of the turtle in X and Y axes
respectively.

.. note::

   To draw a spiral, the turtle has to rotate by a constant value and move
   forward by an increasing value.
            
Solution
--------

::

    def draw_spiral(radius):
        original_xcor = turtle.xcor()
        original_ycor = turtle.ycor()
        speed = 1
        while True:
            turtle.forward(speed)
            turtle.left(10)
            speed += 0.1
            if turtle.distance(original_xcor, original_ycor) > radius:
                break

Bonus
-----

Can you make a conditional for this loop, so you don't need the
infinite loop *while True* or the *break*? Which version do you find
easier to understand?
