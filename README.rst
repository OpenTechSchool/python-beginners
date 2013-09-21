Introduction to programming with Python
***************************************

This workshop is an introduction to basic programming concepts and
abstractions.  It is laid out for hands-on workshops taking up roughly 4 hours.
While we have tried to be compatible with Python 2 _and_ 3 wherever possible,
we'd strongly encourage you to use Python 3.

The initial version of this material was loosely based on the "Python für Kids"
book by Gregor Lingl.  It is conceptual-- rather than incidental --that it
trades in idioms for learnability.  We believe that beginners sometimes have to
jump through one or another hoop to fully comprehend the scope and
applicability of a concept.  Every introduced abstraction solves another pain
point in the life of a beginning programmer.

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
- sphinx-intl

You can install these with pip using ``pip install -r requirements.txt``

Build
=====

The fabric script ``fabfile.py`` contains tasks making the build process very
easy. The following commands have to be executed in the ``docs`` directory.

If you just want to render the HTML version, it's sufficient to run

.. code:: bash

    fab build

This will create a directory ``_build``,
containing the HTML version.

Other `builders <http://sphinx.pocoo.org/builders.html#builders>`_ can be
passed as argument. For instance use ``singlehtml`` to render the whole
tutorial into a single HTML file.

.. code:: bash

   fab build:singlehtml

Translation
=============

1. Translation (pot) templates must be built or updated - ``fab gen_pots``
2. Templates must merged/built into po translation files - ``fab update_pos:de``

.. note:: Both 1 and 2 can be done with ``fab update_pos``

3. po files must be checked and translated correctly
4. ``fab build`` will compile po files, and build the docs for each language

.. note:: only po files should be committed to version control. pot and mo
   files are built automatically.


Deploy
======

The workshop is deployed as a `GitHub Page`_. A good way to do
that is described `here <https://gist.github.com/791759>`_. To simplify this
process, you can use the fabric target ``setup``.

.. code:: bash

   fab setup

This recreates the ``_build/html`` folder by building the project, while the 
folder is cloned to the ``gh-pages`` branch. You can simple cd into the folder 
thereafter and push new updates, or use ``fab build`` to rebuild it.

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

