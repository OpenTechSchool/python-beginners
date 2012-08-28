Conditional statements
**********************
Introduction
============

So far we have accomplished predefined tasks, but in all honesty we were accomplishing no better achievements than the 18th century automata, or the music boxes following one set of instruction to the end. What makes programming so much more powerful is conditional statements. This is the ability to *test* a variable (or a name) against a value and act in one way if the condition is met by the variable or an other way if not. They are also commonly called by programmers *if statements*.

To know if a condition is *true* of *false*, we need a new type of data: 
the booleans. They allow logic operations. A logic statement or operation 
can be avaluated to be true or false. Our conditional statement can then be 
understood like this: **if** *(evaluation of a condition returns true)* **then** *do some operation* **else** *do an other operation*. And any operation that can be avaluated as *true* or *false* can but put to the test. All comparisons return *true* or *false*: *=,>,<*.


Examples
========
Here are some simple examples::

    condition = True
    if condition:
        print "condition met"

    if not condition:
        print "condition not met"

    direction = -30
    if direction > 0 :
        forward(direction)
    else:
        left(180)
        forward (-direction)


Exercise
========

[some example...]

Bonus Exercise
==============
