.. highlight:: shell

============
Installation
============

1. Using conda
--------------

Use the conda forge channel to install `os_command_py`.

.. code-block:: console

    $ conda install os_command_py -c conda-forge

2. Using Pypi
-------------

Use pip to install `os_command_py`.

.. code-block:: console

    $ pip install os_command_py


3. Install os_command_py from source
------------------------------------

The sources for Docking Python can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/samuelmurail/os_command_py

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/samuelmurail/os_command_py/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

.. _Github repo: https://github.com/samuelmurail/os_command_py
.. _tarball: https://github.com/samuelmurail/os_command_py/tarball/master

4. Test Installation
--------------------

To test the installation, simply use ``pytest``:

.. code-block:: console

    $ pytest

    ================================ test session starts ================================
    platform darwin -- Python 3.8.2, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/smurail/Documents/Code/os_command_py, inifile: pytest.ini
    plugins: cov-2.8.1
    collected 8 items

    os_command_py/os_command.py ........                                          [100%]

    ================================= 8 passed in 1.18s =================================
