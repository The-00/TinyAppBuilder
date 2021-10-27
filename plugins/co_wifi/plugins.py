import wifi
import json
import tools.style
import tools.database

class Wifi():
    def __init__(self, app):
        # verify installation
        self._app = app
        self._route()
        self._installation()
        pass

    def _installation(self):
        # execute database insert
        pass

    def _route(self):
        # FRONT
        self._app.route('/wifi/status', method="GET", callback=self._getStatus)
        self._app.route('/wifi',        method="GET", callback=self._getStatus)
        self._app.route('/wifi/list',   method="GET", callback=self._getListWifi)
        # API SPECIAL
        self._app.route('/api/wifi/config', method="POST", callback=self.config)
        self._app.route('/api/wifi/status', method="GET",  callback=self.status)
        self._app.route('/api/wifi/rights', method="GET",  callback=self.rights)
        # API
        self._app.route('/api/wifi/list',          method="POST", callback=self._listWifi)
        self._app.route('/api/wifi/connect/:wifi', method="POST", callback=self._connectWifi)
        self._app.route('/api/wifi/disconnect',    method="POST", callback=self._disconnectWifi)
        

    def status(self):
        s1 = { "state" : "diconnected"}
        s2 = { "state" : "connected", "ssid" : "SSIDDETEST", "ip_ap" : "10.0.0.254/24", "ip" : "10.0.0.2/24"}
        return json.dumps(s2)
    def config(self):
        return ""
    def rights(self):
        return ""
    
    def found_interface(self):
        return "wlp3s0"
    
    def _listWifi(self):
        i = self.found_interface()
        networks = wifi.Cell.all(i)
        list_ssid=[]
        quality_rate_list = [('best', 70), ('ok',65), ('medium',40), ('bad',30), ('awfull',0)]
        
        for network in networks:
            ssid = network.ssid
            quality = int(network.quality.split('/')[0])
            rate = list(filter(lambda x: x[1] >= quality, quality_rate_list))[-1][0]
            list_ssid.append( {'ssid': ssid,
                            'quality': quality,
                            'rate': rate,
                            'is_encrypted': network.encrypted,
                            'encryption_type': network.encryption_type,
                            'address': network.address
                            })
    
        list_ssid.sort(key=lambda x: -x['quality'])
        return json.dumps(list_ssid)
        
    def _connectWifi(self, wifi):
        return ""
    def _disconnectWifi(self):
        return ""

    def _getListWifi(self):
        liste = ""
        wifi_liste = json.loads(self._listWifi())
        for net in wifi_liste:
            liste += f"<input type='button' value='{net['ssid']} | {net['address']}' class='button {net['rate']}'><br>"

        return f"<head>{tools.style.get(self.__name__, 'config_wifi_list.css')}</head><body>{liste}</body>"

    def _getStatus(self):
        return '<h1>get Status Wifi</h1>'



