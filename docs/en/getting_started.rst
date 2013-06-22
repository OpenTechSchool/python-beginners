Getting started
***************

After you've installed Python, steps for launching it depend on which
OS you are using:

Starting Python on Mac OS X
===========================

To start Python on OS X you first need to launch a command line terminal. Do this by
navigating to Applications, then Utilities, then double-click the
"Terminal" program.

The command line Terminal is a tool for interacting with your
computer. A window will open with a command line prompt message,
something like this::

    myname ~$

.. note:: Take note of the dollar sign $ at the end of the
   prompt. This tells you that you are using the system command
   line. We'll be using two different interactive environments today,
   the system command line (with this prompt) and the Python
   interactive shell (which we'll see shortly.)

To launch Python from the system command line type :program:`python` and
then press :kbd:`<Enter>`

Starting Python on Linux
========================

To start Python on Linux you first need to launch a command line terminal
program. Exactly how to do this depend on what Linux desktop
environment you are using, but try searching for Terminal in your
computer's program launcher interface.

The command line terminal is a tool for interacting with your
computer. A window will open with a command line prompt message, something
like this::

    myname@mycomputer:~$


.. note:: Take note of the dollar sign $ at the end of the
   prompt. This tells you that you are using the system command
   line. We'll be using two different interactive environments today,
   the system command line (with this prompt) and the Python
   interactive shell (which we'll see shortly.)

To launch Python from the system command line type :program:`python` and
then press :kbd:`<Enter>`

Starting Python on Windows
==========================

On Windows you can launch Python through the Start menu.


Interacting With Python
=======================

After Python opens, it will show you some contextual information similar to this::

  Python 2.7.2 (default, Feb  1 2012, 00:28:57)
  [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

The prompt ``>>>`` on the last line indicates that you are now in an
interactive Python session, also called the "Python shell". It is
waiting for your commands::

  print("Hello world")

Press :kbd:`<Enter>` and see what happens. You will now see the phrase "Hello
world" appear and then Python will bring you back to the interactive prompt,
where you could enter another command::

  >>> print("Hello world")
  Hello world
  >>>

To leave the interactive shell, press :kbd:`Ctrl-D`.

Running Python files
====================

But you don't want to type everything into the Python shell every time.
Instead you can save the commands to a file and pass a file name to the
:program:`python` executable. It will execute that file instead of launching
the interactive interpreter.

Let's try that.  Create a file :file:`hello.py` in your current directory with
your favorite text editor and paste the print command from above.  Now save
that file.

On Mac OS X and Linux go back to the system command line (where the
prompt ends with ``$`` not ``>>>``, use :kbd:`Ctrl-D` to exit Python if it is
running) and type:

.. code-block:: bash

   python hello.py

.. note::

   Not getting "Hello world" but some crazy error about "can't open
   file" or "No such file or directory?"  Probably your command line
   is not running in the directory you saved the file in; you can use
   the system command line to change your active directory with the
   :command:`cd` command, which stands for "change directory"::

     cd Python_Exercises

   This changes to the subdirectory Python_Exercises of the currently active
   directory.  If you don't know which directory you are currently in then
   running in then use :command:`pwd`,which stands for "print working directory".

On Windows you can double-click the Python file to run it.

When pressing :kbd:`<Enter>` now, the file is executed and you see the output
as before.  But this time, after Python finished executing all commands from
that file it exits instead of going back to the interactive shell.

.. tip::

   Wordpad, TextEdit, Notepad, and Word are **not** suitable text
   editors.  If you are unsure whether you already have a usable
   editor, you might want to download and install `Sublime Text
   <http://www.sublimetext.com/>`_.  Sophisticated editors like this
   can also help you with formatting, running and debugging your code.

And now we are all set and can get started with turtle!

.. important::

   When playing around with turtle, avoid naming your file :file:`turtle.py`
   --- rather use more appropriate names such as :file:`square.py` or
   :file:`rectangle.py`.  Otherwise, whenever you refer to ``turtle``, Python
   will pick up *your* file instead of the standard turtle.

