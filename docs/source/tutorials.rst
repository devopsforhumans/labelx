=========
Tutorials
=========


.. tip::

   Always remember, when in doubt use ``--help``.

Getting help
------------
To see the options use ``--help`` flag after the command.

.. code-block:: shell

   labelx --help

This should output the help information on screen and it looks something similar as
below -

.. code-block:: shell

   Usage: labelx [OPTIONS] COMMAND [ARGS]...

   GitLab label creator control panel

   Options:
     --debug    Turns on DEBUG mode.  [default: False]
     --version  Show the version and exit.
     --help     Show this message and exit.

   Commands:
     create-badges  Create badges for project.
     create-labels  Create labels for issues and merge requests.
     pkg-info       Shows package information.

To checkout individual options for any command use ``--help`` flag.

.. code-block:: shell

   labelx pkg-info --help

This command should show all the available ``arguments`` for ``info`` sub-command.

.. code-block:: shell

   Usage: labelx pkg-info [OPTIONS]

     Prints information about the package

   Options:
     --help  Show this message and exit.

Turning on debug
----------------

Sometimes program runs into ERROR and there are not enough data shown on screen to
determine the cause of the ERROR. For getting ``verbose`` output of all the actions
done by the program simply ``turn on`` the ``debug`` mode with ``--debug`` flag.
By default it's turned off.

To turn on ``debug`` mode -

.. code-block:: shell

   labelx --debug create-labels [OPTIONS] [ARGS]

Also you can turn on the ``debug`` mode at sub-command level by using ``--debug``
flag after the sub-command

.. code-block:: batch

   labelx create-labels [OPTIONS] [ARGS] --debug

OR like this -

.. code-block:: batch

    labelx create-labels --debug [OPTIONS] [ARGS]

Creating Labels
---------------

To create ``default`` labels, use the following command -

.. code-block:: shell

   labelx create-labels -p [gitlab project id]

To create group labels use ``-g`` flag

.. code-block:: shell

   labelx create-labels -g [gitlab group id]

**Example**

.. code-block:: shell

   labelx create-labels -p 12345

This command should run the program with ``preset`` labels and create these labels
in the project mentioned. Output should be something similar -

(output is from version 2.1.1)

.. code-block:: ini

   +--------------------------------------------------+
   |                     labelx                       |
   +--------------------------------------------------+
   | about: GitLab label/badge creator                |
   | author: Dalwar Hossain (dalwar23@pm.me)          |
   | version: 2.1.1                                   |
   | license: GNU General Public License v3           |
   | documentation: https://labelx.readthedocs.io/    |
   +--------------------------------------------------+

   [*] Initializing.....
   [*] Please use 'labelx --help' to see all available options
   -------------------------------------- [labelx] ----------------------------------------
   [$] Creating label - [Bug] ..... DONE
   [$] Creating label - [Done] ..... DONE
   [$] Creating label - [Feature Upgrade] ..... DONE
   [$] Creating label - [Fixed] ..... DONE
   [$] Creating label - [New Feature Request] ..... DONE
   [$] Creating label - [On Hold] ..... DONE
   [$] Creating label - [P1] ..... DONE
   [$] Creating label - [P2] ..... DONE
   [$] Creating label - [P3] ..... DONE
   [$] Creating label - [Planned] ..... DONE
   [$] Creating label - [Source Code Refactoring] ..... DONE
   [$] Creating label - [Testing] ..... DONE
   [$] Creating label - [WIP] ..... DONE
   [$] Creating label - [Won't Fix] ..... DONE
   -------------------------------------- Goodbye! ----------------------------------------

Creating Badges
---------------

To create ``default`` badges, use the following command -

.. code-block:: shell

   labelx create-badges -p [gitlab project id]

To create ``group`` badges use ``-g`` flag with numeric group id.


.. code-block:: shell

   labelx create-badges -g [gitlab group id]


.. note::
   Group badges require ``owner`` permission for the group in context.

**Example**

.. code-block:: shell

   labelx create-badges -p 1245

This command should run the program with ``preset`` badges and create these badges
in the project mentioned. Output should be something similar -

(output is from version 2.1.1)

.. code-block:: shell

   +--------------------------------------------------+
   |                     labelx                       |
   +--------------------------------------------------+
   | about: GitLab label/badge creator                |
   | author: Dalwar Hossain (dalwar23@pm.me)          |
   | version: 2.1.1                                   |
   | license: GNU General Public License v3           |
   | documentation: https://labelx.readthedocs.io/    |
   +--------------------------------------------------+

   [*] Initializing.....
   [*] Please use 'labelx --help' to see all available options
   -------------------------------------- [labelx] ----------------------------------------
   [$] Creating badge - [license] ..... DONE
   [$] Creating badge - [platform] ..... DONE
   [$] Creating badge - [windows] ..... DONE
   [$] Creating badge - [linux] ..... DONE
   [$] Creating badge - [macos] ..... DONE
   [$] Creating badge - [python] ..... DONE
   [$] Creating badge - [style] ..... DONE
   [$] Creating badge - [layout] ..... DONE
   -------------------------------------- Goodbye! ----------------------------------------
