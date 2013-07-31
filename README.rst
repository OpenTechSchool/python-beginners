Introduction to programming with Python
***************************************

HTML Version
============

You can view this workshop being hosted here:
http://opentechschool.github.io/python-beginners/

The following sections are for people who want to contribute.

Setup
=====

This workshop is written in the reStructuredText_ format. The
``.rst`` files can be edited with a normal text editor.

It can be rendered to several output formats using Sphinx_. To do that, you
need to have the following Python packages installed:

- docutils
- Pygments
- Sphinx
- Fabric

Build
=====

The fabric script ``fabfile.py`` contains tasks making the build process very
easy. The following commands have to be executed in the ``docs`` directory.

If you just want to render the HTML version, it's sufficient to run

.. code:: bash
   
    fab build

This will create a directory ``_build`` inside the ``docs`` directory,
containing the HTML version.

Other `builders <http://sphinx.pocoo.org/builders.html#builders>`_ can be
passed as argument. For instance use ``singlehtml`` to render the whole
tutorial into a single HTML file.

.. code:: bash

   fab build:singlehtml
  
Deploy
======

The workshop is deployed as a `GitHub Page`_. A good way to do
that is described `here <https://gist.github.com/791759>`_. To simplify this
process, you can use the fabric target ``setup``.

.. code:: bash

   fab setup

This creates a clone of the repository inside the ``_build`` folder. You can 
now run ``fab build``, change into ``docs/_build/html``, commit and push.

License
=======

This work is licensed under the Creative Commons Attribution-ShareAlike
3.0 Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
Creative Commons, 444 Castro Street, Suite 900, Mountain View,
California, 94041, USA.

.. _OpenTechSchool: http://opentechschool.org
.. _PyCoaches: http://python.opentechschool.org
.. _reStructuredText: http://docutils.sourceforge.net/docs/
.. _Sphinx: http://sphinx.pocoo.org/index.html
.. _Graphviz: http://www.graphviz.org/
.. _GitHub Page: https://help.github.com/categories/20/articles

