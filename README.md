[![Build Status](https://travis-ci.org/brndnmtthws/dragon-rest.svg?branch=master)](https://travis-ci.org/brndnmtthws/dragon-rest) [![Maintainability](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/maintainability)](https://codeclimate.com/github/brndnmtthws/dragon-rest/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/test_coverage)](https://codeclimate.com/github/brndnmtthws/dragon-rest/test_coverage) [![PyPI version](https://badge.fury.io/py/dragon-rest.svg)](https://badge.fury.io/py/dragon-rest) [![Documentation Status](https://readthedocs.org/projects/dragon-rest/badge/?version=latest)](https://dragon-rest.readthedocs.io/en/latest/?badge=latest)
# [dragon-rest](https://dragon-rest.readthedocs.io/en/latest/)
Python wrapper for DragonMint T1 REST API

If you use Halong Mining's DragonMint T1, and would like to interact with it programmatically using Python, then look no further! I have implemented the full HTTP REST API for your enjoyment and pleasure.

## Quickstart

### Install pip package
```
$ pip install dragon-rest
```

### Write the Python codes
```python
from dragon_rest.dragons import DragonAPI

dragon_host = '10.0.0.1'
api = DragonAPI(dragon_host,
                username='admin',
                password='dragonadmin')

r = api.summary()
print(r)
# now you're in the big leagues, boye
```

## Reference

API documentation: https://dragon-rest.readthedocs.io/

For details on the DragonMint API, see: https://halongmining.com/api/
