Loops
*****

Introduction
============

One more thing: Our programs often feature repetition. There is a powerful 
concept in Python called looping (jargon: *iteration*), which we will 
elaborate later on. For now, **try this easy example**::

    for i in range(10):
        print("Hello!")

This is incredibly helpful if we want to do something multiple times --- say, 
drawing the individual border lines of a shape --- but only want to write it 
once.  But it gets better::

    for i in range(10):
        print(i)

Notice how we write only one line of code using ``i`` but it has 10 
different values?

You can also loop over elements of your choice::

    for i in 5, 7, 11, 13:
        print(i)

The ``range(n)`` function can be considered a shorthand for ``0, 1, 2, ..., n-1``. 
If you want to know more about it, you can use the help in the Python shell by 
typing ``help(range)``. Use the :kbd:`q` key to exit the help again.

If you want to repeat some code a number of times, but don't care about the 
value of the ``i`` variable, it can be good practice to replace it with 
``_`` instead. This signifies that we don't care about its value, or don't 
wish to use it. So you could rewrite the first example as::

    for _ in range(10):
        print("Hello!")

You may or may not be wondering about the variable ``i`` - why is it used all the 
time above? Well, it simply stands for "index" and is one of the most common 
variable names ever found in code. But if you are looping over something 
other than just numbers, be sure to name it something better! For instance::

    for name in list_of_first_names:
        print("Hi there, " + name)

This is easier and clearer to read than if we had used ``i`` instead of ``name``.

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
--------

In the example above, the line that starts with a ``#`` is called a 
comment. In Python, anything that goes on a line after ``#`` is ignored 
by the computer. Use comments to explain what your program does, 
without changing the behaviour for the computer. They can also be used 
to easily and temporarily disable, or "comment out" some lines of code.

Comments can also go at the end of a line, like this::

     turtle.left(20)     # now we can change the angle only here

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
        # around after
        ...

Replace the ``...`` with your own stuff, and see if you can come up with 
something funny or interesting! Mistakes are encouraged.
