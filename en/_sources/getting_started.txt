Getting started
***************

Starting Python
===============

After installing Python on your system successfully, you can start the
interactive Python prompt by typing :program:`python` in the command line and
pressing :kbd:`<Enter>`.  It will show you some context information about
Python similar to this::

  Python 2.7.2 (default, Feb  1 2012, 00:28:57) 
  [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 


.. note::

   On Windows you can open Python through the Start Menu.

Those three ``>>>`` in the last line indicate that you are now in the
interactive shell of Python.  It is waiting for your commands::

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

On Mac OSX and Linux go back the command line and type:

.. code-block:: bash

   python hello.py

.. note::

   Not getting "Hello world" but some crazy error about "can't open file" or
   "No such file or directory?"  Probably your command line is not running in
   the directory you saved the file in;  you can change your active directory
   with the :command:`cd` command::

     cd Python_Exercises

   This changes to the subdirectory Python_Exercises of the currently active
   directory.  If you don't know which directory your shell is currently
   running in use :command:`pwd`.

On Windows you can double-click the Python file to run it.

When pressing :kbd:`<Enter>` now, the file is executed and you see the output
as before.  But this time, after Python finished executing all commands from
that file it exits instead of going back to the interactive shell.

.. tip::

   Wordpad, TextEdit, Notepad, and Word are **not** suitable text editors.  If
   you are unsure whether you already have a usable editor, you might want to
   download and install `Sublime Text <http://www.sublimetext.com/>`_.
   Sophisticated editors like this also take care of identation and help you
   run and debug your code.

And now we are all set and can get started with turtle!

.. important::

   When playing around with turtle, avoid naming your file :file:`turtle.py`
   --- rather use more appropriate names such as :file:`square.py` or
   :file:`rectangle.py`.  Otherwise, whenever you refer to ``turtle``, Python
   will pick up *your* file instead of the standard turtle.

