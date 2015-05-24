import fabric
from fabric.api import task, local, execute
import clean
import os

__all__ = ['sdist']
    
@task
def sdist():
    """create the sdist"""
    fabric.state.output.stdout = True
    clean.all()
    local("python shell_plugins.py.in sdist --format=bztar,zip")
