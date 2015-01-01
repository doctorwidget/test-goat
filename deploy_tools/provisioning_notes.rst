**************************
Provisioning A New Site
**************************


Required Packages
=====================

#. nginx
#. git
#. Python 3.4+


Non-Python Tools
--------------------------

Git and nginx are installed via ``apt-get``.

.. code-block:: bash

   user@host$: sudo apt-get install nginx git


Python Tools
----------------

Ubuntu 14.04 comes with a Python 3.4 available. That means you have access to
the now-standard ``pyvenv`` tool, which *should* always install pip along with
every new virtualenv. However,  Ubuntu 14.04 shipped with a **broken**
distribution that cannot install pip. Here's a workaround that uses ``pyvenv``
to create a pip-free virtualenv and then manually adds pip after the fact.

.. code-block:: bash

   user@host$: cd ~/.sites/goat-staging.ceratops.net

   user@host$: pyvenv-3.4 --without-pip  virtualenv

   user@host$: source virtualenv/bin/activate

   (virtualenv)user@host$: python --version
   Python 3.4.0

   (virtualenv)user@host$: curl https://bootstrap.pypa.io/get-pip.py | python
   #... output elided
   #... successfully installed pip-6.03 setuptools-10.1

   # toggle the virtualenv off and back on
   (virtualenv)user@host$: deactivate
   user@host$: source virtualenv/bin/activate

   (virtualenv)user@host$: pip --version
   # pip 6.03 from /home/nathaniel/sites/goat-staging.ceratops.net/virtualenv...

And at that point, you have a fully-functional virtualenv with a working pip.
Now you can run ``pip install foo`` to your hearts content.


Nginx Virtual Host Config
==================================

See ``nginx.template.conf``.

replace SITENAME with e.g. goat-staging.ceratops.net


Upstart Job
=================

See ``gunicorn-upstart.template.conf``

Replace SITENAME with e.g. goat-staging.ceratops.net


Remote Directory  Structure
=====================================

Assuming we have a user account at ``/home/username/``

/home/username/
   +-- sites
       +-- SITENAME
           +-- database/
           +-- source/
           +-- static/
           +-- virtualenv/

+


