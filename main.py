from api import TrackIP
from api import selfIP
import requests

try:
    myIP = selfIP()
    my_pub_ip = myIP.myIP()
    print(f"Your Public IP: {my_pub_ip['ip']}")
    ip = input("\nInput IP: ").strip()

    obj = TrackIP()
    data = obj.trackLocation(ip)

    if data:
        print(f"\nCountry: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
        print(f"Region: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Zip: {data.get('zip', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Latitude: {data.get('lat', 'N/A')}")
        print(f"Longitude: {data.get('lon', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print("\nNOTICE: The program may show a nearby or different City or region depending on your ISP and network routing.")
        print()

    else:
        print("Invalid IP! Check and try again.")
except requests.RequestException as error:
    print(f"Network error: {error}")
except (KeyError, ValueError) as error:
    print(f"Unexpected API response: {error}")
finally:
    input("\nPress Enter to close...")