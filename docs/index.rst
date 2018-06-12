.. dragon_rest documentation master file, created by
   sphinx-quickstart on Tue Jun 12 16:12:30 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

`Build Status`_ `Maintainability`_ `Test Coverage`_ `PyPI version`_
`Documentation Status`_ # `dragon-rest`_ Python wrapper for DragonMint
T1 REST API

If you use Halong Mining’s DragonMint T1, and would like to interact
with it programmatically using Python, then look no further! I have
implemented the full HTTP REST API for your enjoyment and pleasure.

Quickstart
----------

Install pip package
~~~~~~~~~~~~~~~~~~~

::

  $ pip install dragon-rest

Write the Python codes
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

  from dragon_rest.dragons import DragonAPI

  dragon_host = '10.0.0.1'
  api = DragonAPI(dragon_host,
                  username='admin',
                  password='dragonadmin')

  r = api.summary()
  print(r)
  # now you're in the big leagues, boye

Reference
---------

API documentation: https://dragon-rest.readthedocs.io/

For details on the DragonMint API, see: https://halongmining.com/api/

.. _Build Status: https://travis-ci.org/brndnmtthws/dragon-rest
.. _Maintainability: https://codeclimate.com/github/brndnmtthws/dragon-rest/maintainability
.. _Test Coverage: https://codeclimate.com/github/brndnmtthws/dragon-rest/test_coverage
.. _PyPI version: https://badge.fury.io/py/dragon-rest
.. _Documentation Status: https://dragon-rest.readthedocs.io/en/latest/?badge=latest
.. _dragon-rest: https://dragon-rest.readthedocs.io/en/latest/

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
