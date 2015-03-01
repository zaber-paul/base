import fabric
from fabric.api import task, local, execute
import clean
import os

__all__ = ['fast', 'sdist', 'install', 'sphinx']
    
@task
def sdist():
    """create the sdist"""
    fabric.state.output.stdout = True
    clean.all()
    local("python setup.py sdist --format=bztar,zip")
