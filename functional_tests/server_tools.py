"""
NOTE: This is straight from Percival's book and it does not work!

Percival assumes that you have fabric installed in a global 2.x environment.
But I have my fabric in a virtualenv, because (duh), that's the only place
you should ever install anything. Hence, the subprocess call to 'fab' just
returns a 'not found' error.

To make this work would require figuring out how to make the subprocess
module run commands within a virtualenv. Not worth my time, especially
since too much of this back door server magic  makes your functional tests
suspicious anyway. Much better to write a functional test that doesn't
require back door server shenanigans!

"""
from os import path
import subprocess

THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )