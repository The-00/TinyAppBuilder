from bottle import get

import tools.style
import tools.wifi

@get('/connect/')
@get('/connect')
def connect_what():
    buttons = "<input type='button' value='WIFI' class='button wifi' onclick='window.location.href = \"/connect/wifi\"'>"
    buttons+= "<input type='button' value='VPN'  class='button vpn'  onclick='window.location.href = \"/connect/vpn\"' >"
    return f"<head>{tools.style.get('config.css')}</head><body>{buttons}</body>"

@get('/connect/wifi')
def wifi_list():
    liste=""
    for net in tools.wifi.get():
        liste += f"<input type='button' value='{net['ssid']}' class='button {net['rate']}' onclick='window.location.href = \"/connect/wifi/{net['ssid']}\"'><br>"

    return f"<head>{tools.style.get('config_wifi_list.css')}</head><body>{liste}</body>"

@get('/connect/wifi/:wifi')
def connect_wifi(wifi=None):
    print(wifi)
    return f'connecting to {wifi}'

@get('/connect/vpn')
def vpn_list():
    return f'vpn list'

@get('/connect/vpn/:vpn')
def connect_vpn(vpn=None):
    print(vpn)
    return f'connecting to {vpn}'
