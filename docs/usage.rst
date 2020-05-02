.. highlight:: shell

============
Usage
============

Simple Command
--------------

You can use the ``os_command`` module to create a ``Command`` object, which 
takes a list as input, here an example with a simple ``ls`` command:

.. code-block:: python

    >>> cmd_list = ['ls', '-a', '.']
    >>> cmd_test = Command(list_cmd=cmd_list)

You can use the ``display()`` function to print the command:


.. code-block:: python

    >>> cmd_test.display()
    ls -a .

An the the ``run()`` function to excectute it, the return code will be return in a dictionnary:

.. code-block:: python

    >>> return_code = cmd_test.run(out_data=True)
    >>> print(return_code['stdout'])
    .
    ..
    1y0m.pdb
    volume.xvg

Here is another example with the command ``wc``:

.. code-block:: python

    >>> cmd_list = ['wc', './1y0m.pdb']
    >>> cmd_test_2 = Command(list_cmd=cmd_list)
    >>> cmd_test_2.display()
    wc ./1y0m.pdb
    >>> return_code = cmd_test_2.run(out_data=True)
    >>> print('Number of line = {}  word = {} char = {}'.format(
    ... *return_code['stdout'].split()[:3]))
    Number of line = 1627  word = 18466 char = 13...

Defining environment
--------------------

The ``define_env`` can also be used on the ``Command`` object to change an environmnent variable:

.. code-block:: python

        >>> print(os.getenv('USELESS'))
        None
        >>> cmd_list = ['ls', '-lsh']
        >>> cmd_test = Command(list_cmd=cmd_list)
        >>> cmd_test.display() #doctest: +ELLIPSIS
        ls -lsh
        >>> # Here we define the $USELESS env. variable:
        >>> cmd_test.define_env(os.environ.update({'USELESS': 'Changed'}))
        >>> return_code = cmd_test.run(out_data=True)
        >>> print(os.getenv('USELESS'))
        Changed


Run a job in background
-----------------------

A command can also be ran in background using ``run_background()``. It is permitting to run a parallel function, to *eg.* survey the command output. The function working in parallel has to be define in the ``monitor`` dictionnary with ``'function'`` as key, everyother keys of ``monitor`` can be used for the ``monitor`` function.

Here we run a bash command ``sleep`` for 1 second, and use a python function ``function_iter()`` that print out ``"X"`` every tenth of a seconds: 

.. code-block:: python

        >>> import time
        >>>
        >>> # Create the function that will run while the command is running
        >>>
        >>> def function_iter(proc, dict):
        ...     while proc.poll() is None:
        ...         time.sleep(dict['refresh_time'])
        ...         print('X', end='')
        >>>
        >>> monitor = {'function': function_iter,
        ...            'refresh_time': 0.1}
        >>>
        >>> # Create the command
        >>>
        >>> cmd_list = ['sleep', '1']
        >>> background_test = Command(list_cmd=cmd_list)
        >>> background_test.display()
        sleep 1
        >>> return_code = background_test.run_background(monitor,
        ... display=True)
        XXXXXXXXX
        None

