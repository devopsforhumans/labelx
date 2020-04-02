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
     create    Create labels for issues and merge requests.
     pkg-info  Shows package information.

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

   labelx --debug create [OPTIONS] [ARGS]

Also you can turn on the ``debug`` mode at sub-command level by using ``--debug``
flag after the sub-command

.. code-block:: batch

   labelx create [OPTIONS] [ARGS] --debug

OR like this -

.. code-block:: batch

    labelx create --debug [OPTIONS] [ARGS]

Creating Labels
---------------

To created ``default`` labels, use the following command -

.. code-block:: shell

   labelx create -p [gitlab project id]

**Example**

.. code-block:: shell

   labelx create -p 12345

This command should run the program with ``preset`` labels and create these labels
in the project mentioned. Output should be something similar -

(output is from version 1.0.3)

.. code-block:: ini

   +--------------------------------------------------+
   |                     labelx                       |
   +--------------------------------------------------+
   | about: GitLab label creator for issues           |
   | author: Dalwar Hossain (dalwar23@protonmail.com) |
   | version: 1.0.3                                   |
   | license: GNU General Public License v3           |
   | documentation: https://labelx.readthedocs.io/    |
   +--------------------------------------------------+

   [*] Initializing.....
   [*] Please use 'labelx --help' to see all available options
   -------------------------------------- [labelx] -------------------------------------
   [$] Creating label - [Bug].....DONE
   [$] Creating label - [Done].....DONE
   [$] Creating label - [Feature Upgrade].....DONE
   [$] Creating label - [Fixed].....DONE
   [$] Creating label - [New Feature Request].....DONE
   [$] Creating label - [On Hold].....DONE
   [$] Creating label - [P1].....DONE
   [$] Creating label - [P2].....DONE
   [$] Creating label - [P3].....DONE
   [$] Creating label - [Planned].....DONE
   [$] Creating label - [Source Code Refactoring].....DONE
   [$] Creating label - [Testing].....DONE
   [$] Creating label - [WIP].....FAILED (Conflict)
   [$] Creating label - [Won't Fix].....DONE
   --------------------------- Before we leave, Please note  ---------------------------
   [*] Total skipped: 1
   [*] Skipped : ['WIP']
   -------------------------------------- Goodbye! -------------------------------------
