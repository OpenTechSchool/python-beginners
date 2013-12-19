Loops
*****

Introduction
============

Something you might have noticed: our programs often feature repetition. 
Python has a powerful concept it makes use of called looping 
(jargon: *iteration*), which we can use to cut out our reptitive code! 
For now, **try this easy example**::

    for name in "John", "Sam", "Jill":
        print("Hello " + name)

This is incredibly helpful if we want to do something multiple times --- say, 
drawing the individual border lines of a shape --- but only want to write that 
action once. Here's another version of a loop::

    for i in range(10):
        print(i)

Notice how we write only one line of code using ``i``, but it takes on 10 
different values?

The :samp:`range(n)` function can be considered a shorthand 
for ``0, 1, 2, ..., n-1``. If you want to know more about it, you can use 
the help in the Python shell by typing ``help(range)``. 
Use the :kbd:`q` key to exit the help again.

You can also loop over elements of your choice::

    total = 0
    for i in 5, 7, 11, 13:
        print(i)
        total = total + i
        
    print(total)

Write this example out and run it with python, to check it works how you might 
expect.

.. note::

   Notice how above, the lines of code that are *looped*, are the ones that 
   are *indented*. This is an important concept in Python - that's how it 
   knows which lines should be used in the ``for`` loop, and which come 
   after, as part of the rest of your program. Use four spaces (hitting tab) 
   to indent your code.

Sometimes you want to repeat some code a number of times, but don't care about 
the value of the ``i`` variable; so it can be good practice to replace it 
with ``_`` instead. This signifies that we don't care about its value, or 
don't wish to use it. Here's a simple example::

    for _ in range(10):
        print("Hello!")

You may or may not be wondering about the variable ``i`` - why is it used all 
the time above? Well, it simply stands for "index" and is one of the most 
common variable names ever found in code. But if you are looping over something 
other than just numbers, be sure to name it something better! For instance::

    for drink in list_of_beverages:
        print("Would you like a " + drink + "?")

This is immediately clearer to understand than if we had used ``i`` 
instead of ``drink``.

Drawing a dashed line
=====================

Exercise
--------

Draw a dashed line.  You can move the turtle without the turtle drawing its 
movement by using the ``turtle.penup()`` function; to tell it to draw again, 
use ``turtle.pendown()``.

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

.. hint::

   Feeling lost?  Inspect ``i`` at every run of the loop::

       for i in range(10):
           print(i)
           # write more code here

   Can you utilize ``i`` --- commonly called the **index** variable or loop 
   variable --- to get increasing step sizes?

Comments
========

In the example above, the line that starts with a ``#`` is called a 
comment. In Python, anything that goes on a line after ``#`` is ignored 
by the computer. Use comments to explain what your program does, 
without changing the behaviour for the computer. They can also be used 
to easily and temporarily disable, or "comment out" some lines of code.

Comments can also go at the end of a line, like this::

     turtle.left(20)     # tilt our next square slightly

More Efficient Squares
======================

Exercise
--------

The squares we were drawing at the start of this tutorial had a lot of 
repeated lines of code. Can you write out a square drawing program in fewer 
lines by utilizing loops?

Solution
--------

::

    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

Bonus
-----

Try *nesting* loops, by putting one right under (*inside*) the other, with some 
drawing code that's inside both. Here's what it can look like::

    for ...:
        for ...:
            # drawing code inside the inner loop goes here
            ...
        # you can put some code here to move 
        # around after!
        ...

Replace the ``...``'s with your own code, and see if you can come up with 
something funny or interesting! :sup:`Mistakes are encouraged!`
