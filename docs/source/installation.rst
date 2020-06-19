============
Installation
============

Labelx (``labelx``) requires Python 3.6, 3.7 or 3.8. If you do not already have a
Python environment configured on your computer, please see the
`Python <https://www.python.org>`_ page for instructions on installing Python
environment.

.. note::
   if you are on Windows and want to install optional packages (e.g., scipy) then you
   will need to install a python distribution such as
   `Anaconda <https://www.anaconda.com>`_,
   `Enthought Canopy <https://www.enthought.com/product/canopy>`_
   or `Pyzo <https://www.pyzo.org>`_. If you use one of these Python distributions,
   please refer to their online documentation.

Assuming that the default python environment is already configured on your computer and
you intend to install ``labelx`` inside of it. To create and work with Python virtual
environments, please follow instructions on
`venv <https://docs.python.org/3/library/venv.html>`_ and
`virtual environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

To start the installation process, please make sure the latest version of ``pip``
(python3 package manager) is installed. If ``pip`` is not installed, please refer to
the `Pip documentation <https://pip.pypa.io/en/stable/installing/>`_ and install
``pip`` first.

Linux/macOS
-----------
Install the latest release of ``labelx`` with ``pip``:

.. code-block:: shell

   pip install labelx

To upgrade to a newer version use the ``--upgrade`` flag:

.. code-block:: shell

   pip install --upgrade labelx

If system wide installation is not possible for permission reasons, use ``--user``
flag to install ``labelx`` for current user

.. code-block:: shell

   pip install --user labelx


Windows
-------
``labelx`` should support ``windows cmd`` out of the box. But if you face any issues,
please refer to the ``hint`` below -

.. hint::
   Windows terminal (cmd/power shell) doesn't support all the unicode codecs and To get
   the best results - please use a terminal emulator like,
   cmder [`Download Cmder <http://cmder.net/>`_] or ConEmu
   [`Download ConEmu <https://conemu.github.io/>`_]. Please use *<xterm>* color scheme
   from `settings` menu, for the best visual representation of the program.

Considering ``python3`` is installed and ``pip`` is configured.

Open Cmder/ConEmu and Type:

.. code-block:: shell

   pip install labelx

Or

.. code-block:: shell

   python3 setup.py install

This command should install ``labelx`` with all the required dependencies.

Install from Github
-------------------
Alternatively, ``labelx`` can be installed manually by downloading the current version
from `GitHub <https://github.com/dalwar23/labelx>`_ or
`PyPI <https://pypi.org/project/labelx/>`_. To install a downloaded versions, please
unpack it in a preferred directory and run the following commands at the top level of
the directory:

.. code-block:: shell

   pip install .

or run the following:

.. code-block:: shell

   python3 setup install

Dependencies
------------

This package requires a configuration file in either ``.yaml`` or ``yml`` format. The
look up priority for the configuration file is as following-

1. <user_home_directory>/.config/<package_name>/config.yaml (``Window/Linux/MacOS``)
2. <current_working_directory>/<package_name>/config.yaml (``Windows/Linux/MacOS``)
3. /etc/<package_name>/config.yaml (``Linux/MacOS``)

If ``config.yaml`` doesn't exists in one of these locations, the program will NOT run.
So, to create the configuration file, please use -

**Windows**

Windows system by default doesn't allow creation of ``.`` prefixed directory from GUI,
so use the following -

- Open `cmd` and change the directory to the ``home`` folder of the user
- Run ``mkdir .config`` (if the folder doesn't exist)
- Run ``cd .config``
- Run ``mkdir labelx``

Now that the ``.`` prefixed directory is created, use the GUI to add a file in
``labelx`` directory named ``config.yaml``. Once the file is created, open the file
and add the following lines according to your settings -

.. code-block:: yaml

   ---
   login:
     host: <gitlab_server>
     protocol: <https>/<http>
     token: <secret_access_token_from_gitlab_profile>

**Linux/MacOS**

- Open a terminal and ``cd`` into the home directory or any other directory form the
  above dependency list.
- Run ``mkdir -p .config/labelx``
- Run ``cd .config/labelx/``
- Run ``nano config.yaml``
- Add the above lines into the file and save it
