Conditional statements
**********************

Introduction
============

So far we have accomplished predefined tasks, but in all honesty we
were accomplishing no better than old-time music boxes following one
set of instructions to the end. What makes programming so much more
powerful are conditional statements. This is the ability to *test* a
variable against a value and act in one way if the condition is met by
the variable or another way if not. They are also commonly called by
programmers *if statements*.

To know if a condition is *True* of *False*, we need a new type of data: 
the booleans. They allow logical operations. 
A logic statement or operation can be evaluated to be *True* or *False*.
Our conditional statement can then be understood like this: 

    **if** *(a condition evaluates to True)*:
        *then do these things only for 'True'*
    **else**:
        *otherwise do these things only for 'False'*.

The condition can be anything that evaluates as *True* or
*False*. Comparisons always return *True* or *False*, for example
``==`` (equal to), ``>`` (greater than), ``<`` (less than.)

The **else** part is optional. If you leave it off, nothing will
happen if the conditional evaluates to 'False'.


Examples
========

Here are some examples. You may want to read them over line-by-line
and see what you think they do, or run them to be certain::

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

Giving Directions
=================

Python turtles can be very good at following instructions. Let's use
the ``input()`` function to ask the user for a direction to move
the turtle. To keep things easy we will only accept two instructions:
"left" and "right".

.. note::

   Using Python 2? The ``input()`` function is called ``raw_input()``.

It's much easier to define this as a function, like so::

  def move():
      direction = input("Go left or right? ")
      if direction == "left":
          turtle.left(60)
          turtle.forward(50)
      if direction == "right":
          turtle.right(60)
          turtle.forward(50)

Now whenever you use ``move()`` you are prompted to choose ``left`` or
``right``.


"data munging"
==============

In this program, the turtle will only respond to exactly ``left``
or ``right`` with no variation. Though ``Left`` or ``RIGHT`` might
seem the same to a human, that isn't the case when programming. Python
has a few utility methods to help with that. A string has the methods
``.strip()``, which removes whitespace and ``.lower()`` which makes
everything lower-case.

Here are some examples to print out the effects of ``.strip()`` and ``.lower()``::

  my_variable = "       I Am Capitalised"
  print(my_variable)
  my_stripped = my_variable.strip()
  print(my_stripped)
  my_lower = my_variable.lower()
  print(my_lower)

Try adding ``direction = direction.strip().lower()`` to the ``move()``
function, to see the effect. We often call this kind of code "data
munging", and it is very common.

Can you add some extra input choices to make the turtle draw other
things? How about ``hexagon``?
