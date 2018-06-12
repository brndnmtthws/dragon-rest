dragon-rest
-----------

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

For more details on the API, take a look at :func:`~dragons.DragonAPI`.

Reference
---------

For details on the DragonMint API, see: https://halongmining.com/api/

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
