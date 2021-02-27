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

- Sphinx (and its dependencies docutils and Pygments)
- Fabric
- sphinx-intl
- sphinx-bootstrap-theme

You can install these with pip using ``pip install -r requirements.txt``

To push / pull translations from Transifex you will need the package
``transifex-client`` as well.

Build
=====

The fabric script ``fabfile.py`` contains tasks making the 
build process very easy.

If you just want to render the HTML version, it's sufficient to run::

    $ fab build:en

Replace `en` with the language you'd like to build.

This will create a directory ``_build``, containing the HTML version.

You can view this in a browser by running ``fab serve`` and visiting the 
web address listed.

Other `builders <http://sphinx.pocoo.org/builders.html#builders>`_ can be 
passed as an argument. For instance use ``singlehtml`` to render the whole 
tutorial into a single HTML file::

    $ fab build:en,singlehtml

Translation
===========

Translations should normally be done through Transifex.

You can see the project on Transifex 
`here <https://www.transifex.com/projects/p/python-for-beginners/>`_.

After editing the tutorial, it is desirable to update sources for it.

1. New translation templates (.pot) must be created, then po translation 
   files are updated (or created for the first time) - ``fab gen_pots``
2. If you wish to upload new sources to transifex, you should use their
   cli client. ``tx push -s``.
3. To pull down translations for a particular language, use e.g. 
   ``tx pull -l de``, for de (german) or others.
4. ``fab build:de`` will compile po files, and build the docs for that 
   language.

It is also possible to edit and update po files manually, you can check out 
the other fab command (``fab list``) for help with that.

.. note:: only .po files should be committed to version control. .pot and .mo
   files are built automatically.

Deploy
======

The workshop is deployed as a `GitHub Page`_. A good way to do 
that is described `right here <https://gist.github.com/791759>`_. To simplify 
this process, you can use a nifty fabric target::

    $ fab setup

This recreates the ``_build/html`` folder, cloning the folder to the 
``gh-pages`` branch of this repo. Then you should build updates for the 
desired language. Then `cd` into this folder, and git push the updates to 
update the branch. Like so::

    $ fab build:en
    $ cd _build/html
    $ git status
    $ git commit --all
    $ git push

Credits
=======

The material presented here is a collaborative work.  It has been created
largely by OpenTechSchool_ Python coaches.  Every bit, from exercises to
translations, has been contributed by the community.  After every workshop
where this material is used we try to gather feedback on how to improve the
material.

License
=======

This work is licensed under the Creative Commons Attribution-ShareAlike 
3.0 Unported License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
Creative Commons, 444 Castro Street, Suite 900, Mountain View, 
California, 94041, USA.

.. _OpenTechSchool: http://opentechschool.org
.. _reStructuredText: http://docutils.sourceforge.net/docs/
.. _Sphinx: http://sphinx.pocoo.org/index.html
.. _GitHub Page: https://help.github.com/categories/20/articles
