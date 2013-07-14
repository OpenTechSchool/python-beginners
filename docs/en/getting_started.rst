Getting started
***************

If you haven't yet got python, the latest official installation packages can be found here:

http://python.org/download/

Python 3 is preferable, being the newest version out!

What is Python, exactly?
========================

Ok, so python is this thing called a **programming language**. It takes text that 
you've written (usually referred to as **code**), turns it into instructions for 
your computer, and runs those instructions. We'll be learning how to write code 
to do cool and useful stuff. No longer will you be bound to use others' 
programs to do things with your computer!

Practically, Python is just another program on your computer. The first thing to 
learn is how to use and interact with it. There are in fact many ways to do this; 
the first one to learn is to interact with python's interpreter, 
using your **operating system's** (OS) console.

A **console** (or 'terminal', or 'command prompt') is a *textual* way to interact with 
your OS, just as the 'desktop', in conjuction with your mouse, is the *graphical* 
way to interact your system.

Opening a console on Mac OS X
-----------------------------

OS X's standard console is a program called Terminal. Open Terminal by 
navigating to Applications, then Utilities, then double-click the 
"Terminal" program. You can also easily search for it in the system 
search tool in the top right.

The command line Terminal is a tool for interacting with your
computer. A window will open with a command line prompt message,
something like this::

    mycomputer:~ myusername$ 

Opening a console on Linux
--------------------------

Different linux distributions (e.g Ubuntu, Fedora, Mint) may have different 
console programs, usually called referred to as a terminal. The exact terminal 
you start up, and how, can depend on your distribution. On Ubuntu, you will 
likely want to open Gnome Terminal. It should present a prompt like this::

    myusername@mycomputer:~$ 

Opening a console on Windows
----------------------------

Window's console is called the Command Prompt, named "cmd.exe". An easy way 
to get to it is by using the key combination "Windows+R" 
('Windows' meaning the windows logo button), which should open a 'Run' dialog. 
Then simply type :kbd:`cmd` and hit :kbd:`<Enter>` / click Ok. It should look like::

    C:\Users\myusername> 

Window's Command Prompt is not quite as powerful as its counterparts on Linux 
and OS X, so you might like to start the Python Interpreter (see just below) 
directly, or using the IDLE program that Python comes with. You can find these 
in the start menu.

Using Python
============

The python program that you have installed by default will act as something 
called an **interpreter**. An interpreter will take commands and run them as you 
enter them, very handy for trying things out.

Just type :program:`python` at your console, hit :kbd:`<Enter>`, and you should 
enter Python's Interpreter.

To find out which version of python you're running, use :program:`python -V` to tell you.

Interacting With Python
-----------------------

After Python opens, it will show you some contextual information similar to this::

    Python 3.3.2 (default, May 21 2013, 15:40:45) 
    [GCC 4.8.0 20130502 (prerelease)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

.. note::

   The prompt **>>>** on the last line indicates that you are now in an
   interactive Python interpeter session, also called the "Python shell". 
   **This is different from the normal terminal command prompt!**

You can now enter some python code. Try::

  print("Hello world")

Press :kbd:`<Enter>` and see what happens. After showing the results, Python 
will bring you back to the interactive prompt, where you could enter 
another command::

  >>> print("Hello world")
  Hello world
  >>>

An extremely useful command is ``help()``, which enters a help functionality 
to explore all the stuff python lets you do, right from the interpreter.

To leave the interactive shell, press :kbd:`Ctrl-Z` and then
:kbd:`Enter` on Windows, or :kbd:`Ctrl-D` on OS X or Linux. Alternatively, 
you could also run the python command ``exit()``!

Running Python files
--------------------

When you have a lot of python code to run, you will want to save it into a file, 
so you for instance can modify small parts of it (fix a bug) and re-run it, 
without having to repeatedly re-type the rest.
Instead you can save your code to a file and pass a file name to the 
:program:`python` executable. It will execute that file instead of launching 
the interactive interpreter.

.. note::

   Make sure you are at your system command prompt, which will have ``$`` or 
   ``>`` at the end, not at python's (which has ``>>>`` instead)!

Let's try that.  Create a file :file:`hello.py` in your current directory with 
your favorite text editor and paste the print command from above.  Now save 
that file. On Linux or OS X, you can also run :kbd:`touch hello.py` to create 
an empty file to edit. To run this file with python, it's pretty easy:

.. code-block:: bash

   $ python hello.py

.. note::

   Not getting "Hello world" but some crazy error about "can't open 
   file" or "No such file or directory?" Your command line might not be 
   running in the directory you saved the file in. You can use 
   the system command line to change your active directory with the 
   :command:`cd` command, which stands for "change directory". On Windows, 
   you might want something like::

     $ cd Desktop\Python_Exercises

   On Linux or OS X, you might want something like::

     $ cd Desktop/Python_Exercises

   This changes to the directory Python_Exercises under the Desktop folder 
   (yours might be somewhere a bit different). If you don't know the location 
   of the directory where you saved the file, you can simply drag the 
   directory to the command line window.  If you don't know which 
   directory your shell is currently running in use :command:`pwd`, 
   which stands for "print working directory".

On Windows you should also be able to  double-click the Python file to run it.

When pressing :kbd:`<Enter>` now, the file is executed and you see the output 
as before.  But this time, after Python finished executing all commands from 
that file it exits back to the system command prompt, instead of going back 
to the interactive shell.

.. tip::

   Wordpad, TextEdit, Notepad, and Word are **not** suitable text
   editors.  If you are unsure whether you already have a usable
   editor, you might want to download and install `Sublime Text
   <http://www.sublimetext.com/>`_.  Code editors like this
   can also help you with formatting, running and debugging your code.

And now we are all set and can get started with turtle!

.. important::

   When playing around with turtle, avoid naming your file :file:`turtle.py`
   --- rather use more appropriate names such as :file:`square.py` or
   :file:`rectangle.py`.  Otherwise, whenever you refer to ``turtle``, Python
   will pick up *your* file instead of the standard turtle.

