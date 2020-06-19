======
labelx
======


.. image:: https://img.shields.io/pypi/v/labelx.svg
        :target: https://pypi.python.org/pypi/labelx

.. image:: https://readthedocs.org/projects/labelx/badge/?version=latest
        :target: https://labelx.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Label Creator for GitLab Projects.


* Free software: GNU General Public License v3
* Documentation: https://labelx.readthedocs.io.


Features
--------

* Show package information
* Create labels for GitLab projects
* Create badges for GitLab projects

Requirements
------------

* python >= 3.6
* ``config.yaml`` at ``~/.confing/labelx/``

.. code-block:: yaml

   ---
   login:
     host: gitlab.company.com
     protocol: https
     token: KHGJIO**-dA76VGHs36

Credits
-------

See `AUTHORS.rst <AUTHORS.rst>`_

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
