import servers

def allpoweron(zone='tk1a'):
    for serverid in servers.server_ids(zone):
        print(poweron(zone, serverid))

allpoweron()