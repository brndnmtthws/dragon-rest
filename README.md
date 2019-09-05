[![Build Status](https://travis-ci.org/brndnmtthws/dragon-rest.svg?branch=master)](https://travis-ci.org/brndnmtthws/dragon-rest) [![Maintainability](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/maintainability)](https://codeclimate.com/github/brndnmtthws/dragon-rest/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/test_coverage)](https://codeclimate.com/github/brndnmtthws/dragon-rest/test_coverage) [![PyPI version](https://badge.fury.io/py/dragon-rest.svg)](https://badge.fury.io/py/dragon-rest) [![Documentation Status](https://readthedocs.org/projects/dragon-rest/badge/?version=latest)](https://dragon-rest.readthedocs.io/en/latest/?badge=latest) [![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=brndnmtthws/dragon-rest)](https://dependabot.com)

# [dragon-rest](https://dragon-rest.readthedocs.io/en/latest/)

Python wrapper for DragonMint/Innosilicon REST API

If you use Halong Mining's DragonMint or Innosilicon miners, and would like
to interact with it programmatically using Python, then look no further! I
have implemented the full HTTP REST API for your enjoyment and pleasure.

![Dragon at rest](/resting-dragon.png?raw=true)

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

r = api.summary() # get summary
print(r)
api.upgradeUpload('t1_20180515_060842.swu') # upgrade firmware
# now you're in the big leagues, boye
```

## Reference

API documentation: https://dragon-rest.readthedocs.io/

For details on the DragonMint API, see: https://halongmining.com/api/

## Support

[![Contact Brenden 😎 on Umpyre](https://api.umpyre.com/badge/634c76f3513240a4bec1eda7fb5db7ea/badge.svg?width=211.275&height=68.04&name=Brenden%20%F0%9F%98%8E&font_size=18&style=light)](https://umpyre.com/u/634c76f3513240a4bec1eda7fb5db7ea)

_Want to offer support? Add yourself above._
