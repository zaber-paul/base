all:
	python setup.py install
	sphinx-apidoc -o docs/source cloudmesh_base
	cd docs; make -f Makefile html
