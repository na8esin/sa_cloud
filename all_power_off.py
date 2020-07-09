import servers
import power

def allpoweroff(zone='tk1a'):
    for serverid in servers.server_ids(zone):
        print(power.off(zone, serverid))

allpoweroff()
allpoweroff('is1a')