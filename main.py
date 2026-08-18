from api import TrackIP
from api import selfIP

myIP = selfIP()
my_pub_ip = myIP.myIP()
print(f"Your Public IP: {my_pub_ip["ip"]}")
ip = input(f"\nInput IP: ")

obj = TrackIP()
data = obj.trackLocation(ip)

if data:
    print(f"\nCountry: {data["country"]} ({data["countryCode"]})")
    print(f"Region: {data["regionName"]} ({data["region"]})")
    print(f"City: {data["city"]}")
    print(f"Zip: {data["zip"]}")
    print(f"ISP: {data["isp"]}")
    print(f"Latitude: {data["lat"]}")
    print(f"Longitude: {data["lon"]}")
    print(f"Organization: {data["org"]}")
    print("\nNOTICE: The program may show a nearby or different City or region depending on your ISP and network routing.")
    print()

else:
    print("Invalid IP! Check and try again.")