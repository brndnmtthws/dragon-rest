import vcr
from pytest import fixture
from dragon_rest.dragons import DragonAPI

vcr = vcr.VCR(
    cassette_library_dir='tests/fixtures/cassettes'
)


@fixture
def jwt():
    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEcmFnb25NaW50IiwiaWF0IjoxNTI4NjQzOTYwLCJleHAiOjE1Mjg2NjU1NjAsInVzZXIiOiJhZG1pbiJ9.rm9Ll81v5pVmlHQCEyFqoeb6TnJSqH66lM1-izK_NoQ'


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

    assert api.jwt is not None
    assert r['success']


@vcr.use_cassette()
def test_overview(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.overview()

    assert api.jwt is not None
    assert r['success']


@vcr.use_cassette()
def test_pools(host, jwt):
    api = DragonAPI(host, jwt=jwt)
    r = api.pools()

    assert api.jwt is not None
    assert r['success']


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

    assert api.jwt is not None
    assert r['success']
