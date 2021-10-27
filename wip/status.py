from uptime import uptime
from datetime import timedelta
import tools.wifi
import tools.vpn


def get():
    wifi_infos   = tools.wifi.infos() 
    vpn_infos    = tools.vpn.infos() 
    client_infos = None
    
    state = {
        'uptime'    : sec_to_txt( uptime()              ),
        'public_ip' : str(        tools.vpn.public_ip() ),
        'intern_ip' : str(        "10.0.0.1"            ),
        'wifi' : {
            'connected'      : bool(       wifi_infos[ 'connected'         ] ),
            'ssid'           : str(        wifi_infos[ 'connected_ssid'    ] ),
            'ap_ip'          : str(        wifi_infos[ 'connected_ap_ip'   ] ),
            'quality'        : int(        wifi_infos[ 'connected_quality' ] ),
            'connected_time' : sec_to_txt( wifi_infos[ 'connected_time'    ] ),
            'bitrate'        : int(        wifi_infos[ 'connected_bitrate' ] )
        },
        'vpn' : {
            'connected'      : bool(       vpn_infos[ 'connected'            ] ),
            'name'           : str(        vpn_infos[ 'connected_name'       ] ),
            'gateway_ip'     : str(        vpn_infos[ 'connected_gateway_ip' ] ),
            'quality'        : int(        vpn_infos[ 'connected_quality'    ] ),
            'connected_time' : sec_to_txt( vpn_infos[ 'connected_time'       ] ),
            'bitrate'        : int(        vpn_infos[ 'connected_bitrate'    ] )
        },
        'clients' : [
            {
                'name' : str,
                'ip' : str,
                'quality': int,
                'connected_time' : int,
                'bitrate' : int
            }
            for client in []
        ]
    }
    
    return state




def sec_to_txt(n):
    if n > 0:
        td = timedelta(seconds=n)
        txt = [] 
        days = td.days
        years = days // 365
        days %= 365
        months = days // 30
        days %= 30
        weeks = days // 7
        days %= 7
        
        sec = td.seconds
        hours = sec // 3600
        sec %= 3600
        minutes = sec // 60
        sec %= 60
        
        
        if years>0: txt.append( f"{years} années" if years>1 else "1 année" )
        if months>0: txt.append( f"{months} mois" )
        if weeks>0: txt.append( f"{weeks} semaines" if weeks>1 else "1 semaine" )
        if days>0: txt.append( f"{days} jours" if days>1 else "1 jour" )
        if hours>0: txt.append( f"{hours} heures" if hours>1 else "1 heure" )
        if minutes>0: txt.append( f"{minutes} minutes" if minutes>1 else "1 minute" )
        if sec>0: txt.append( f"{sec} secondes" if sec>1 else "1 seconde" )
        
        txt = ", ".join( txt[:-1] ) + " et " + txt[-1]
    else:
        txt = "no time"
    return txt