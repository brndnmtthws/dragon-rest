"""DragonAPI is a Python wrapper for the DragonMint T1."""
import requests
import json
from urllib import parse


class DragonAPI(object):
    """
    DragonMint/Innosilicon API wrapper.

    This wrapper should work with both DragonMint and Innosilicon branded
    miners. If you have problems with the API, please open GitHub issue
    accordingly.

    The official documentation for the API is avaiable at:
    https://halongmining.com/api/

    Example::

        from dragon_rest.dragons import DragonAPI

        dragon_host = '10.0.0.1'
        api = DragonAPI(dragon_host,
                        username='admin',
                        password='dragonadmin')

        r = api.summary()
        print(r)
        # now you're in the big leagues, boye 😉

    """

    def __init__(self,
                 host,
                 username='admin',
                 password='dragonadmin',
                 timeout=60,
                 jwt=None):
        """Create and authenticate an API client."""
        self.base_url = "http://{}".format(host)
        self.username = username
        self.password = password
        self.timeout = timeout
        self.jwt = jwt
        if not self.jwt:
            self.auth()

    @staticmethod
    def is_dragon(host, timeout=1):
        """
        Check if host is a dragon.

        Check if the specified host is a dragon based on simple heuristic.
        The code simply checks if particular strings are in the index page.
        It should work for DragonMint or Innosilicon branded miners.
        """
        try:
            r = requests.get('http://{}/'.format(host), timeout=timeout)
            if r.status_code == 200:
                if '<title>DragonMint</title>' in r.text or \
                        '<title>AsicMiner</title>' in r.text:
                    return True
        except requests.exceptions.RequestException:
            pass
        return False

    def __post(self, path, data=None):
        response = requests.post(
            parse.urljoin(self.base_url, path),
            headers={'Authorization': 'Bearer ' + self.jwt},
            timeout=self.timeout,
            data=data)
        response.raise_for_status()
        try:
            if not response.json()['success'] and \
                'token' in response.json() and \
                    response.json()['token'] == 'expired':
                # refresh the token, retry
                self.auth()
                return self.__post(path, data)
            return response.json()
        except ValueError:
            return response

    def __post_files(self, path, files):
        response = requests.post(
            parse.urljoin(self.base_url, path),
            headers={'Authorization': 'Bearer ' + self.jwt},
            timeout=self.timeout,
            files=files)
        response.raise_for_status()
        try:
            if not response.json()['success'] and \
                'token' in response.json() and \
                    response.json()['token'] == 'expired':
                # refresh the token, retry
                self.auth()
                return self.__post_files(path, files)
            return response.json()
        except ValueError:
            return response

    def __get_stream(self, path):
        response = requests.get(
            parse.urljoin(self.base_url, path),
            headers={'Authorization': 'Bearer ' + self.jwt},
            stream=True,
            timeout=self.timeout)
        response.raise_for_status()
        if not response.json()['success'] and \
            'token' in response.json() and \
                response.json()['token'] == 'expired':
            # refresh the token, retry
            self.auth()
            return self.__get_stream(path)
        return response

    def auth(self):
        """Authenticate with the miner and obtain a JSON web token (JWT)."""
        response = requests.post(
            parse.urljoin(self.base_url, '/api/auth'),
            timeout=self.timeout,
            data={'username': self.username, 'password': self.password})
        response.raise_for_status()
        json = response.json()
        self.jwt = json['jwt']
        return json

    def summary(self):
        """Fetch DEVS, POOLS and Fan Speed from the cgminer API."""
        return self.__post('/api/summary')

    def overview(self):
        """
        Fetch miner overview.

        Fetch miner type, hardware information, network information
        and versions of the miner
        """
        return self.__post('/api/overview')

    def pools(self):
        """Receive the configured pools of the miner."""
        return self.__post('/api/pools')

    def updatePools(self,
                    pool1,
                    username1,
                    password1,
                    pool2=None,
                    username2=None,
                    password2=None,
                    pool3=None,
                    username3=None,
                    password3=None):
        """Change the pools of the miner. This call will restart cgminer."""
        return self.__post('/api/updatePools',
                           data={
                               'Pool1': pool1,
                               'UserName1': username1,
                               'Password1': password1,
                               'Pool2': pool2,
                               'UserName2': username2,
                               'Password2': password2,
                               'Pool3': pool3,
                               'UserName3': username3,
                               'Password3': password3,
                           })

    def updatePassword(self,
                       user,
                       currentPassword,
                       newPassword):
        """Change the password of a user."""
        return self.__post('/api/updatePassword',
                           data={
                               'user': user,
                               'currentPassword': currentPassword,
                               'newPassword': newPassword
                           })

    def network(self):
        """Get the current network settings."""
        return self.__post('/api/network')

    def updateNetwork(self,
                      dhcp='dhcp',
                      ipaddress=None,
                      netmask=None,
                      gateway=None,
                      dns=None):
        """Change the current network settings."""
        return self.__post('/api/updateNetwork',
                           data={
                               'dhcp': dhcp,
                               'ipaddress': ipaddress,
                               'netmask': netmask,
                               'gateway': gateway,
                               'dns': json.dumps(dns)
                           })

    def type(self):
        """Return the type of the miner."""
        return self.__post('/api/type')

    def reboot(self):
        """Reboot the miner."""
        return self.__post('/api/reboot')

    def poweroff(self):
        """Power Off the Miner."""
        return self.__post('/api/poweroff')

    def restartCgMiner(self):
        """Restart cgminer."""
        return self.__post('/api/restartCgMiner')

    def factoryReset(self):
        """Remove all user settings and reboot the miner."""
        return self.__post('/api/factoryReset')

    def getAutoTune(self):
        """Return cgminer auto-tune mode."""
        return self.__post('/api/getAutoTune')

    def getAutoTuneStatus(self):
        """Return cgminer Auto-Tune status."""
        return self.__post('/api/getAutoTuneStatus')

    def setAutoTune(self, autotune):
        """Set cgminer to use or not embedded auto-tune functionality."""
        return self.__post('/api/setAutoTune',
                           data={'autotune': autotune})

    def upgradeUpload(self, file):
        """Upgrade the firmware of the miner."""
        files = {'upfile': open(file, 'rb')}
        return self.__post_files('/upgrade/upload',
                                 files=files)

    def upgradeDownload(self, url):
        """Upgrade the firmware of the miner with a URL of the update file."""
        return self.__post('/upgrade/download',
                           data={'url': url})

    def getLatestFirmwareVersion(self):
        """Return the latest version available of the miner."""
        return self.__post('/api/getLatestFirmwareVersion')

    def getDebugStats(self):
        """
        Get debug status of miner.

        Return the cgminer stats of each board and each chip of the miner.
        """
        return self.__post('/api/getDebugStats')

    def streamLogs(self):
        """Return systemd-journald logs in chunked packages."""
        return self.__get_stream('/stream/logs')
