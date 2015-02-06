"""
This entire project uses Python3, but as of Jan 01 2015, Fabric is still 2.X
only. That means this file can only be run from inside an independent, second
virtualenv that uses 2.X, and not from the main one where everything else
runs. I find this to be surprisingly irritating!

Note that after running this script you will always need to

#. SSH into an admin account
#. manually restart the gunicorn server

.. code-block:: bash

    $: ssh nathaniel@goat-staging.ceratops.net
    #... request and supply password
    #... Welcome to Ubuntu 14.04.1 LTS...

    nathaniel@ceratops $: sudo restart gunicorn-goat-staging.ceratops.net
    #... [sudo] request and supply password
    #... gunicorn-goat-staging.ceratops.net start/running, process 32101

"""
import random

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run

REPO_URL = 'https://github.com/doctorwidget/test-goat.git'

def deploy():
    """
    Deploy this site to any given host.  

    Run from the same directory as this file, as:
           $ fab deploy:host=nathaniel@goat-staging.ceratops.net

    If launched that way, then within the script scope:
         *env.host* will have the value ``goat-staging.ceratops.net``
         *env.user* will have the value ``nathaniel``

    Note that we're providing a domain name, not an IP address. So this
    script depends on the virtual machine host *and* the DNS server both 
    being up and running. Deploying to multiple servers is a matter of 
    running this script multiple times, each with a different host.

    """
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(site_folder, source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    """Build our directories, gracefully doing nothing if they already exist."""
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    """Get latest code from github. Depends on the REPO_URL defined
    at the top of this file.

    """
    if exists(source_folder + '/.git'):
            run('cd %s && git fetch' % (source_folder,))
    else:
            run('git clone %s %s' % (REPO_URL, source_folder))
    
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name):
    """
    Update the settings.py file on the remote server. 
    
    I think I would rather do this via environmental variables in the long run,
    but here I am faithfully following along with Percival's book.

    """
    settings_path = source_folder + '/goat/settings.py'

    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "%s"' % (site_name,))
    secret_key_file = source_folder + '/goat/secret_key.py'

    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-=_+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')    


def _update_virtualenv(site_folder, source_folder):
    """
    Create a virtual environment if one does not yet exist. 

    Note that this is *not* following along with the book, because I use
    the (standard) pyvenv tool rather than the 3rd-party virtualenv tool. 

    Also note that the manual installation of pip is only necessary
    because Ubuntu 14.04 ships with a faulty version of Python in which
    the ``ensurepip`` option fails. Perhaps someday Ubuntu will fix this,
    but until then it's only one extra command. 

    """
    virtualenv_folder = site_folder + "/virtualenv"
    virtual_py3 = virtualenv_folder + '/bin/python'   
    virtual_pip3 = virtualenv_folder + '/bin/pip' 

    if not exists(virtual_py3):
        run('pyvenv-3.4 --without-pip %s' % (virtualenv_folder,))
        run('curl https://bootstrap.pypa.io/get-pip.py | %s' % (virtual_py3,))

    run('%s install -r %s/requirements.txt' % (virtual_pip3, source_folder))
        

def _update_static_files(source_folder):
    """Make sure all static files have been moved to STATIC_ROOT."""
    cmd = 'cd %s && ../virtualenv/bin/python manage.py collectstatic --noinput'   
    run(cmd % (source_folder,))


def _update_database(source_folder):
    """Migrate the database."""
    cmd = 'cd %s && ../virtualenv/bin/python manage.py migrate --noinput'
    run(cmd % (source_folder,))





