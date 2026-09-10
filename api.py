import requests

class TrackIP:
    def trackLocation(self, ip):
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            return response.json()
        else:
            print("Server or connection error :(")

class selfIP:
    def myIP(self):
        response = requests.get("https://api.ipify.org/?format=json")
        if response.status_code == 200:
            return response.json()
        else:
            print("Server or connection error :(")