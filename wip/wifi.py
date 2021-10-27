from wifi import Cell, Scheme

def found_interface():
    return "wlp3s0"

def get():
    i = found_interface()
    networks = Cell.all(i)
    list_ssid=[]
    quality_rate_list = [('best', 70), ('ok',65), ('medium',40), ('bad',30), ('awfull',0)]
    
    for network in networks:
        ssid = network.ssid
        quality = int(network.quality.split('/')[0])
        rate = list(filter(lambda x: x[1] >= quality, quality_rate_list))[-1][0]

        list_ssid.append( {'ssid':ssid,
                           'quality':quality,
                           'rate':rate
                           })
    
    list_ssid.sort(key=lambda x: -x['quality'])
    
    return list_ssid

def infos():
    connected = is_connected() 
    return {
            'connected'         : connected,
            'connected_ssid'    : connected_ssid()      if connected else None,
            'connected_ap_ip'   : connected_ap_ip()     if connected else None,
            'connected_quality' : connected_quality()   if connected else -1,
            'connected_time'    : connected_time()      if connected else -1,
            'connected_bitrate' : connected_bitrate()   if connected else -1
        }

def is_connected():
    return False

def connected_ssid():
    return ""

def connected_ap_ip():
    return ""

def connected_quality():
    return 0

def connected_time():
    return 0

def connected_bitrate():
    return 0
