Getting started
***************

Starting Python
===============

After installing Python on your system successfully, you can start the interactive Python prompt by typing ``python`` in the command and press <enter>. It will show you some context information about Python similar to this::

  Python 2.7.2 (default, Feb  1 2012, 00:28:57) 
  [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 


.. note:: On windows the installer is not always setting up the "path" correctly. If that is the case on your system, you probably didn't see this message before but have to follow the steps described on the `Python docs <http://docs.python.org/using/windows.html#excursus-setting-environment-variables>`_ and **restart your command line**.

Those three ">>>" in the last line indicate that you are now in the interactive shell of Python. Type for example::

  print("Hello world")

press <enter> and see what happens. You will now see the phrase "Hello world" appear and then Python will bring you back to the interactive input, where you could enter another command now::

  >>> print("Hello world")
  Hello world
  >>>


Running Python files
====================

But you don't want to type everything into the Python shell everytime. Instead
having a file with commands and handing that to Python to execute it would be
much better. In order to do that you can just pass a file name to the Python
command in your shell and it will execute that file. Let's try that. Just open
the file "hello.py" in this directory in your favourite text editor and paste
the print command from above. Now save that file, go back the command line and
type::

  Python hello.py

When pressing <enter> now, the file is executed and you see the print as before. But this time, after Python executed all commands from that file, it exited instead of going back to the interactive shell. In some opearting systems (and depending on your setup) you might also be able to just double click on the hello.py file to execute it 

.. note:: Wordpad, TextEdit, Notepad and Word are **not** suited text editors. If you are unsure whether you already have a usable editor, you might want to download and install `Sublime Text2 <http://www.sublimetext.com/>`_. Sophisticated editors like this also take care of identation and help you run and debug your code.

And now we are all set and can get started with turtle.

		



