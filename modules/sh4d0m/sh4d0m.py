 #!/usr/bin/env python
import sys
import shodan

def create_shodan_object():
    shodan_object =""
    # Add your shodan API key here
    api_key = ""
    shodan_object = shodan.Shodan(api_key)
    return shodan_object
    
def shodan_ip_search(shodan_search_object, shodan_search_ip):
    port_target = []
    #port_target =""
    result = ""
    try:
        print "\nSearching Shodan for info about " + shodan_search_ip + "...\n"
        # Search Shodan
        result = shodan_search_object.host(shodan_search_ip)
        try:
            for i in result['data']:
               print 'Port: %s' % i['port']
               port_target.append(i['port'])
               #print port_target
        except Exception as e:
            print e
    except Exception as e:
        print e
    return port_target

def CreateShodan(ip):
    ports =""
    port_target=[]
    search_ip = ""
    try:    
        search_ip = ip
        shodan_api_object = create_shodan_object()
        port_target = shodan_ip_search(shodan_api_object, search_ip)
        #print port_target
        ports = str(port_target).replace("[","").replace("]","")
        #print ports
        return ports
    except Exception as e:
        print 'Error: %s' % e
        sys.exit(1)
