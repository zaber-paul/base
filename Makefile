all: clean requirements
	python setup.py install
	sphinx-apidoc -o docs/source cloudmesh_base
	cd docs; make -f Makefile html

view:
	open docs/build/html/index.html

clean:
	rm -rf docs/build
	rm -rf build
	rm -rf cloudmesh_base.egg-info
	rm -rf dist

requirements:
	pip install -r requirements-other.txt


tag:
	cm-authors > AUTHORS
	git tag
	@echo "New Tag?"; read TAG; git tag $$TAG; git push origin --tags

rmtag:
	git tag
	@echo "rm Tag?"; read TAG; git tag -d $$TAG; git push origin :refs/tags/$$TAG
