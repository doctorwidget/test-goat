*************
test-goat
*************

This repository contains walkthrough code for Harry Percival's book,
*Test-Driven Development with Python*.

Differences
===============

I've made a few small changes to the project structure compared to the book.

#. The main application source directory is *goat* rather than *superlists*.
#. All apps (well, technically just the one ``list`` app) are all found inside
   the   ``{{PROJECT}}/goat/apps/`` directory, rather than living as a
   siblings of ``manage.py``.
#. I use ``pytest`` as my test runner, which is why there is a ``pytest.ini``
   file.

