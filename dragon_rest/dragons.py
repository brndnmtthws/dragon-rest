import requests
import json
from urllib import parse


class DragonAPI(object):
    def __init__(self,
                 host,
                 username='admin',
                 password='dragonadmin',
                 timeout=15,
                 jwt=None):
        self.base_url = "http://{}".format(host)
        self.username = username
        self.password = password
        self.timeout = timeout
        self.jwt = jwt
        if not self.jwt:
            self.auth()

    def post(self, path, data=None):
        response = requests.post(
            parse.urljoin(self.base_url, path),
            headers={'Authorization': 'Bearer ' + self.jwt},
            timeout=self.timeout,
            data=data)
        response.raise_for_status()
        return response.json()

    def get_stream(self, path):
        response = requests.get(
            parse.urljoin(self.base_url, path),
            headers={'Authorization': 'Bearer ' + self.jwt},
            stream=True,
            timeout=self.timeout)
        response.raise_for_status()
        return response

    def auth(self):
        response = requests.post(
            parse.urljoin(self.base_url, '/api/auth'),
            timeout=self.timeout,
            data={'username': 'admin', 'password': 'dragonadmin'})
        response.raise_for_status()
        json = response.json()
        self.jwt = json['jwt']
        return json

    def summary(self):
        return self.post('/api/summary')

    def overview(self):
        return self.post('/api/overview')

    def pools(self):
        return self.post('/api/pools')

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
        return self.post('/api/pools',
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
        return self.post('/api/updatePassword',
                         data={
                             'user': user,
                             'currentPassword': currentPassword,
                             'newPassword': newPassword
                         })

    def network(self):
        return self.post('/api/network')

    def updateNetwork(self,
                      dhcp='dhcp',
                      ipaddress=None,
                      netmask=None,
                      gateway=None,
                      dns=None):
        return self.post('/api/updateNetwork',
                         data={
                             'dhcp': dhcp,
                             'ipaddress': ipaddress,
                             'netmask': netmask,
                             'gateway': gateway,
                             'dns': json.dumps(dns)
                         })

    def type(self):
        return self.post('/api/type')

    def reboot(self):
        return self.post('/api/reboot')

    def poweroff(self):
        return self.post('/api/poweroff')

    def restartCgMiner(self):
        return self.post('/api/restartCgMiner')

    def factoryReset(self):
        return self.post('/api/factoryReset')

    def getAutoTune(self):
        return self.post('/api/getAutoTune')

    def getAutoTuneStatus(self):
        return self.post('/api/getAutoTuneStatus')

    def setAutoTune(self, autotune):
        return self.post('/api/setAutoTune',
                         data={'autotune': autotune})

    def upgradeDownload(self, url):
        return self.post('/upgrade/download',
                         data={'url': url})

    def getLatestFirmwareVersion(self):
        return self.post('/api/getLatestFirmwareVersion')

    def getDebugStats(self):
        return self.post('/api/getDebugStats')

    def streamLogs(self):
        return self.get_stream('/stream/logs')
