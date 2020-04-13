Installation
=======================================

Get the os_command_py library from `github`_.

.. code-block:: bash

	git clone https://github.com/samuelmurail/os_command_py.git
	./setup.py install --user

.. _github: https://github.com/samuelmurail/os_command_py

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. python 3 libraries:  
	* Sphinx and sphinx-argparse (only for building documentation)
	* Pytest (only for testing purpose)

Make the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Need `sphinx`_ installed with the argparse sphinx module:

.. code-block:: bash

	pip3 install Sphinx --user
	pip3 install sphinx-argparse --user

You can then build the documentation either in html format or pdf.

.. code-block:: bash

	cd os_command_py/doc
	# For html documentation:
	sphinx-build -b html . _build
	# For pdf documentation:
	sphinx-build -M latexpdf . _build/

.. _sphinx: http://www.sphinx-doc.org

Test installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch test with `doctest`_, will check that module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.

.. code-block:: bash

	$ pytest
	================================== test session starts ==================================
	platform darwin -- Python 3.7.3, pytest-5.3.0, py-1.8.0, pluggy-0.13.0
	rootdir: /Users/smurail/Documents/Code/os_command_py, inifile: pytest.ini
	plugins: cov-2.8.1
	collected 8 items

	os_command.py ........                                                            [100%]

	=================================== 8 passed in 0.20s ===================================
.. _doctest: https://docs.python.org/3/library/doctest.html