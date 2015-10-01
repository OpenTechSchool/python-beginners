Simple drawing with turtle
**************************

Introduction
============

Turtle is like a drawing board.

It has functions like ``turtle.forward(...)`` and ``turtle.left(...)`` which
can move the turtle around.

Before you can use turtle, you have to import it. We recommend playing around
with it in the interactive interpreter first, as there is an extra bit of work
required to make it work from files. Just go to your terminal and type::

    import turtle

.. image:: /images/default.png

.. note::

   Not seeing anything on Mac OS?  Try issuing a command like
   ``turtle.forward(0)`` and looking if a new window opened behind your
   command line.

.. note::

   Do you work with Ubuntu and get the error message "No module named
   _tkinter"? Install the missing package with ``sudo apt-get install
   python3-tk``

.. note::
   
   While it might be tempting to just copy and paste what's written on
   this page into your terminal, we encourage you to type out each command.
   Typing gets the syntax under your fingers (building that muscle memory!)
   and can even help avoid strange syntax errors.

::

    turtle.forward(25)

.. image:: /images/forward.png

::

    turtle.left(30)

.. image:: /images/left.png


The ``turtle.forward(...)`` function tells the turtle to move forward
by the given distance. ``turtle.left(...)`` takes a number of degrees which you
want to rotate to the left. There is also ``turtle.backward(...)`` and
``turtle.right(...)``, too.

.. note::
   Want to start fresh? You can type ``turtle.reset()`` to clear the drawing
   that your ``turtle`` has made so far. We'll go into more detail on
   ``turtle.reset()`` in just a bit.

The standard turtle is just a triangle. That's no fun! Let's make it a turtle
instead with the ``turtle.shape()`` command::

  turtle.shape("turtle")

So much cuter!

If you put the commands into a file, you might have recognized that the turtle
window vanishes after the turtle finished its movement.  (That is because
Python exits when your turtle has finished moving.  Since the turtle window
belongs to Python, it terminates as well.)  To prevent that, just put
``turtle.exitonclick()`` at the bottom of your file.  Now the window stays open
until you click on it::

    import turtle

    turtle.shape("turtle")

    turtle.forward(25)

    turtle.exitonclick()

.. note::

   Python is a programming language where horizontal indenting of text is
   important. We'll learn all about this in the Functions chapter later on,
   but for now just keep in mind that stray spaces or tabs before any line
   of Python code can cause an unexpected error.

Drawing a square
================

.. note::

   You're not always expected to know the anwer immediately. Learn by
   trial and error! Experiment, see what python does when you tell it
   different things, what gives beautiful (although sometimes
   unexpected) results and what gives errors. If you want to keep
   playing with something you learned that creates interesting
   results, that's OK too. Don't hesitate to try and fail and learn
   from it!

Exercise
--------

Draw a square as in the following picture:

.. image:: /images/square.png

For a square you will probably need a right angle, which is 90 degrees.

.. rst-class:: solution

Solution
--------

::

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

.. note::

    Notice how the turtle starts and finishes in the same place and
    facing the same direction, before and after drawing the
    square. This is a useful convention to follow, it makes it easier
    to draw multiple shapes later on.

Bonus
-----

If you want to get creative, you can modify your shape with the
``turtle.width(...)`` and ``turtle.color(...)`` functions.  How do you
use these functions?  Before you can use a function you need to know
its *signature* (for example the number of parameters and what they
mean.) To find this out you can type ``help(turtle.color)`` into the
Python shell. If there is a lot of text, Python will put the help text
into a *pager*, which lets you page up and down. Press the :kbd:`q`
key to exit the pager.

.. tip::

   Are you seeing an error like this::

    NameError: name 'turtle' is not defined

   when trying to view help? In Python you have to import names before you
   can refer to them, so in a new Python interactive shell you'll need to
   ``import turtle`` before ``help(turtle.color)`` will work.

Another way to find out about functions is to browse the `online documentation`_.

.. _online documentation: http://docs.python.org/library/turtle


.. caution::

    If you misdrew anything, you can tell turtle to erase its drawing board
    with the ``turtle.reset()`` directive or undo the most recent step with
    ``turtle.undo()``.

.. tip::

   As you might have read in the help, you can modify the color with
   :samp:`turtle.color({colorstring})`.  These include but are not limited to
   "red," "green," and "violet."  See the `colours manual`_ for an extensive
   list.

   .. _colours manual: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm

Drawing a rectangle
===================

Exercise
--------

Can you draw a rectangle too?

.. image:: /images/rectangle.png

.. rst-class:: solution

Solution
--------

::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

Bonus
-----

How about a triangle? In an equilateral triangle (a triangle with all
sides of equal length) each corner has an angle of 60 degrees.


More squares
============

Exercise
--------

Now, draw a tilted square. And another one, and another one. You can
experiment with the angles between the individual squares.

.. image:: /images/tiltedsquares.png

The picture shows three 20 degree turns. You could try 20, 30 and 40, for example.

.. rst-class:: solution

Solution
--------

::

    turtle.left(20)

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.left(30)

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

    turtle.left(40)

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

