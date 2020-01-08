from __future__ import print_function

from future import standard_library
standard_library.install_aliases()
from cloudmesh_base.util import banner
from cloudmesh_base.Shell import Shell
import os
import pip
import sys
import yaml
from setuptools.command.install import install
import textwrap

make = """
    test:
    - echo "hallo world"
    github:
    - git commit -a
    - git push
    clean:
    - rm -rf *.egg-info *.eggs
    - rm -rf docs/build
    - rm -rf build
    - rm -rf dist
    doc:
    - sphinx-apidoc -o docs/source cloudmesh_base
    - cd docs; make -f Makefile html
    view:
    - open docs/build/html/index.html
    pypi:
    - python setup.py install
    - python setup.py sdist bdist_wheel
    - python setup.py bdist_wheel upload -r {repo}
    - python setup.py sdist upload -r {repo}
    register:
    - python setup.py register -r {repo}
    tag:
    - bin/new_version.sh
    rmtag:
    - git tag
    - echo "rm Tag?"; read TAG; git tag -d $$TAG; git push origin :refs/tags/$$TAG
    install:
    - python setup.py install
"""

clean_python = '''
        find . -name "*~" -exec rm \{\} \;
	    find . -name "*.pyc" -exec rm \{\} \;
'''

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


def os_execute(commands):
    for command in commands.split("\n"):
        command = command.strip()
        print(command)
        os.system(command)

def get_version_from_git():
    r = Shell.git('tag').split("\n")[-1]
    return r

def check_pip():
    major = int(pip.__version__.split(".")[0])
    if major < 7:
        print("")
        print("    ERROR: Pip version", pip.__version__, "is to old.")
        print("    Tip:   Please update pip with ")
        print("")
        print("             pip install pip -U")
        print("")
        sys.exit()

def makefile(tag, **kwargs):
    script = "\n".join(yaml.load(make)[tag])
    commands = "\n".join(yaml.load(make)[tag]).format(**kwargs)

    banner("RUNNING")
    os_execute(commands)


def Make(action, **kwargs):

    class InstallAction(install):
        def run(self):
            makefile(action, **kwargs)
            if action == "clean":
                os.system(clean_python)

    return InstallAction


