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

   If you're on Windows and instead see something like "command not found," the
   installer has not set up your *search path* correctly, ie. Windows does not
   know where to find :program:`python.exe`.  Follow the steps described in the
   `Python docs`__ and **restart your command line.**

   __ http://docs.python.org/using/windows.html#excursus-setting-environment-variables

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

But you don't want to type everything into the Python shell every time.  Instead
having a file with commands and handing that to Python to execute it would be
much better.  In order to do that you can just pass a file name to the
:program:`python` command in your shell and it will execute that file.  Let's
try that.  Create a file :file:`hello.py` in your current directory with your
favorite text editor and paste the print command from above.  Now save that
file, go back the command line and type:

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
   running in use :command:`pwd` on Linux or :command:`cd` without parameters
   on Windows.

   If you need to change your drive on Windows, just type the drive's letter
   followed by a colon::

     C:

When pressing :kbd:`<Enter>` now, the file is executed and you see the output
as before.  But this time, after Python executed all commands from that file,
it exited instead of going back to the interactive shell. 

.. note::

   Wordpad, TextEdit, Notepad, and Word are **not** suited text editors.  If
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
