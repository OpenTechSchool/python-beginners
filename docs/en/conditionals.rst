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
the ``raw_input()`` function to ask the user for a direction to move
the turtle. To keep things easy we will only accept two instructions:
"left" and "right".

It's much easier to define this as a function, like so::

  def move():
      direction = raw_input("Go left or right? ")
      if direction == "left":
          turtle.left(60)
          turtle.forward(50)
      if direction == "right":
          turtle.right(60)
          turtle.forward(50)

Now whenever you use ``move()`` you are prompted to choose ``left`` or
``right``.

.. note::

   The turtle will only respond to exactly ``left`` or ``right`` with
   no variation. Though ``Left`` or ``RIGHT`` might seem the same to a
   human, that isn't the case when programming. Python has a few
   utility methods to help with that. A string has the methods
   ``.strip()``, which removes whitespace and ``.lower()`` which makes
   everything lower-case. Try adding ``direction =
   direction.strip().lower()`` to see the effect. We often call this
   kind of code "data munging", and it is very common.

Can you add some extra instructions to the turtle? How about ``hexagon``?
