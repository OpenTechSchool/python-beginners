Logical operators
*****************

Introduction
============

Conditionals are a nice way to make decisions by asking if something equals true
or not. But often one condition is not enough. For instance if we want to make a
decision upon ``xcor()`` and ``ycor()`` we have to combine them. This can be
done with logical operators.

This and that or something else
===============================

Two easy to understand operators are ``and`` and ``or``. They do exactly whay the
sound like: combine two statements in a way both have be true (``and``) or
one of them has to be true (``or``)::

    if 1 < 2 and 4 > 2:
        print "condition met"

    if 1 < 2 and 4 < 10:
        print "condition not met"

    if 4 < 10 or 1 < 2:
        print "condition met"

You are not restricted to one logical operator. You can combine as may as you
want.

Exercise
--------

Create a function that accepts the argument ``angel`` and moves the turtle into
that direction until either the vertical or horizontal distance to the center
exeeds 100.

Solution
--------

::

    def move_to_square_border(angel):
        left(angel)
        while xcor() > -100 and xcor() < 100 and ycor() > -100 and ycor() < 100:
            forward(10)

Bonus
-----

Execute the ``move_to_square_border()`` function multiple times with different
angels. Use the ``home()`` function to make the turtle jump to the center after
each line.
