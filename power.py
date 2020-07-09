import servers
import json
import time

def off(zone, serverid):
    return servers.get_sacloud_response(
                    get_url().format(zone, serverid), 'DELETE')

def on(zone, serverid):
    return servers.get_sacloud_response(
                    get_url().format(zone, serverid), 'PUT')

def get(zone, serverid):
    return servers.get_sacloud_response(get_url().format(zone, serverid))

def get_url():
    url  = 'https://secure.sakura.ad.jp/cloud/zone/'
    url += '{0}/api/cloud/1.1/server/{1}/power'
    return url

def restart(serverid, zone):
    off(zone, serverid)
    start = time.time()
    is_break=False
    while True:
        load_data = json.loads(get(zone, serverid))
        if load_data["Instance"]["Status"] == 'down':
            break
        time.sleep(3)
        print('processing...')
        if time.time() - start > 30:
            print('!!BREAK!!')
            is_break = True
            break

    if not is_break:
        print('up comming')
        on(zone, serverid)
