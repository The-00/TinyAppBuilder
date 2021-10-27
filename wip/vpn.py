import requests

def public_ip():
    return requests.get("http://ifconfig.me").text

def infos():
    connected = is_connected() 
    return {
            'connected'            : connected,
            'connected_name'       : connected_name()        if connected else None,
            'connected_gateway_ip' : connected_gateway_ip()  if connected else None,
            'connected_quality'    : connected_quality()     if connected else -1,
            'connected_time'       : connected_time()        if connected else -1,
            'connected_bitrate'    : connected_bitrate()     if connected else -1
        }

def is_connected():
    return True

def connected_name():
    return ""

def connected_gateway_ip():
    return ""

def connected_quality():
    return 0

def connected_time():
    return 0

def connected_bitrate():
    return 0
