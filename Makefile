all: clean requirements
	python setup.py install
	sphinx-apidoc -o docs/source cloudmesh_base
	cd docs; make -f Makefile html

view:
	open docs/build/html/index.html

requirements:
	pip install -r requirements-other.txt

######################################################################
# CLEANING
######################################################################

clean:
	find . -name "*~" -exec rm {} \;
	find . -name "*.pyc" -exec rm {} \;
	rm -rf build dist docs/build .eggs
	rm -rf *.egg-info
	# cd docs; make clean
	echo "clean done"

######################################################################
# TAGGING
######################################################################

tag:
	cm-authors > AUTHORS
	git tag
	@echo "New Tag?"; read TAG; git tag $$TAG; python setup.py install;   git commit -m "version $$TAG" cloudmesh_base/version.py; pit push; git commit -m $$TAG --allow-empty; git push origin --tags; git push

rmtag:
	git tag
	@echo "rm Tag?"; read TAG; git tag -d $$TAG; git push origin :refs/tags/$$TAG

