Logical operators
*****************

Introduction
============

Conditionals are a nice way to make decisions by asking if something equals
*True* or not. But often one condition is not enough. 
We may want to take the opposite of our result. Or for instance if we want to
make a decision upon ``turtle.xcor()`` and ``turtle.ycor()`` we have to combine
them. This can be done with logical operators. 

Negation of a statement
=======================

If we want something to be *False* we can use ``not``. It is a logical
operator::

    x = False
    if not x :
        print("condition met")
    else:
        print("condition not met")

Exercise
--------

The turtle gives us a useful function to know if it is drawing or not:
``turtle.isdown()``.  This function returns *True* if the turtle is drawing. As
we have seen earlier, the function ``turtle.penup()`` and ``turtle.pendown()``
toggle between drawing while moving, or just moving without a trace.

Can we write a function that only goes forward if the pen is up?

.. rst-class:: solution

Solution
--------

::

    def stealthed_forward(distance):
        if not turtle.isdown():
            turtle.forward(distance)


This and that or something else
===============================

Two easy to understand operators are ``and`` and ``or``. They do exactly what
they sound like:::

    if 1 < 2 and 4 > 2:
        print("condition met")

    if 1 > 2 and 4 < 10:
        print("condition not met")

    if 4 < 10 or 1 < 2:
        print("condition met")

You are not restricted to one logical operator. You can combine as may as you
want.

Exercise
--------

Earlier we put the turtle in a circular prison. This time let's make
it a box. If the turtle goes more than 100 in the X *or* Y axis then
we turn the turtle back around to the center.

.. rst-class:: solution

Solution
--------

::

  def forward(distance):
      while distance > 0:
          if (turtle.xcor() > 100
              or turtle.xcor() < -100
              or turtle.ycor() > 100
              or turtle.ycor() < -100):
              turtle.setheading(turtle.towards(0,0))
          turtle.forward(1)
          distance = distance - 1
