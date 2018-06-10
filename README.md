[![Build Status](https://travis-ci.org/brndnmtthws/dragon-rest.svg?branch=master)](https://travis-ci.org/brndnmtthws/dragon-rest) [![Maintainability](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/maintainability)](https://codeclimate.com/github/brndnmtthws/dragon-rest/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/186a969e83fe6608c02d/test_coverage)](https://codeclimate.com/github/brndnmtthws/dragon-rest/test_coverage)
# dragon-rest
Python wrapper for DragonMint T1 REST API

## Quickstart

### Install pip package
```
$ pip install dragon_rest
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

For details on the API, see: https://halongmining.com/api/
