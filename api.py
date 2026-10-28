import requests

class TrackIP:
    def trackLocation(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        if response.status_code == 200 and data.get("status") == "success":
            return data
        print(f"Lookup failed: {data.get('message', 'server or connection error')}")
        return None

class selfIP:
    def myIP(self):
        response = requests.get("https://api.ipify.org/?format=json", timeout=10)
        response.raise_for_status()
        return response.json()