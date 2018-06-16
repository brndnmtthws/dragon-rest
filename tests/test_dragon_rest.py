import vcr
from pytest import fixture
from dragon_rest.dragons import DragonAPI

vcr = vcr.VCR(
    cassette_library_dir='tests/fixtures/cassettes'
)


@fixture
def jwt():
    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEcmFnb25NaW50IiwiaWF0IjoxNTI5MTg2NjIxLCJleHAiOjE1MjkyMDgyMjEsInVzZXIiOiJhZG1pbiJ9.SWPJ3vPPziK_2OXk7a2QfmF0NvPwTZ6-r54dQzoYWoI'


@fixture
def host():
    return '10.1.0.25'


@vcr.use_cassette()
def test_auth(host):
    api = DragonAPI(host)

    assert api.jwt is not None


@vcr.use_cassette()
def test_summary(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.summary()

    assert r['success']
    assert len(r['DEVS']) == 3


@vcr.use_cassette()
def test_overview(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.overview()

    assert r['success']
    assert r['type'] == 'T1'


@vcr.use_cassette()
def test_pools(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.pools()

    assert r['success']
    assert len(r['pools']) == 2


@vcr.use_cassette()
def test_updatePools(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.updatePools(
        pool1='stratum+tcp://us-east.stratum.slushpool.com:3333',
        username1='brndnmtthws.dragon-0ade5',
        password1='x',
        pool2='stratum+tcp://pool.ckpool.org:3333',
        username2='3GWdXx9dfLPvSe7d8UnxjnDnSAJodTTbrt.dragon-0ade5',
        password2='x',
        pool3=None,
        username3=None,
        password3=None
    )

    assert r['success']


@vcr.use_cassette()
def test_updatePassword(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.updatePassword('admin', 'dragonadmin', 'loladmin')
    assert r['success']
    r = api.updatePassword('admin', 'loladmin', 'dragonadmin')

    assert r['success']


@vcr.use_cassette()
def test_network(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.network()

    assert r['success']
    assert r['dhcp'] == 'dhcp'


@vcr.use_cassette()
def test_updateNetwork(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.updateNetwork(dhcp='dhcp')

    assert r['success']


@vcr.use_cassette()
def test_type(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.type()

    assert r['success']
    assert r['type'] == 'T1'


@vcr.use_cassette()
def test_getAutoTune(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.getAutoTune()

    assert r['success']
    assert r['autoTuneMode'] == 'efficient'


@vcr.use_cassette()
def test_getAutoTuneStatus(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.getAutoTuneStatus()

    assert r['success']
    assert r['mode'] == 'efficient'


@vcr.use_cassette()
def test_getAutoTune(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.setAutoTune('efficient')

    assert r['success']


@vcr.use_cassette()
def test_getLatestFirmwareVersion(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.getLatestFirmwareVersion()

    assert r['success']


@vcr.use_cassette()
def test_getDebugStats(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.getDebugStats()

    assert r['success']


# This works, but VCR doesn't work with streams
# @vcr.use_cassette()
# def test_streamLogs(host, jwt):
#     api = DragonAPI(host, jwt=jwt)
#     r = api.streamLogs()
#     for line in r.iter_lines():
#         print(line)

@vcr.use_cassette()
def test_is_dragon(host):
    is_dragon = DragonAPI.is_dragon(host, timeout=1)

    assert is_dragon

@vcr.use_cassette()
def test_is_not_dragon():
    is_not_dragon = not DragonAPI.is_dragon('127.0.0.1', timeout=1)

    assert is_not_dragon
