# 🌐 IP Location Finder

A simple Python-based IP lookup tool that displays your **public IP address** and allows you to enter any IP address to retrieve its **approximate geolocation and network information**.

## ✨ Features

- 🌐 Automatically detects your public IP address
- 🔎 Allows you to enter any IP address for lookup
- 🌍 Shows approximate location details for the entered IP
- 🏙️ Displays country, region, and city
- 📌 Displays latitude and longitude
- 🌐 Displays ISP and organization information
- ⚡ Lightweight and easy to use
- 🔑 No API key required

## 📋 Information Displayed

For the IP address entered by the user, the application can display:

- **IP Address**
- **Country**
- **Country Code**
- **Region**
- **City**
- **ZIP/Postal Code**
- **Latitude**
- **Longitude**
- **ISP**
- **Organization**

## 🔄 How It Works

```text
Start
  ↓
Detect user's public IP
  ↓
Display public IP
  ↓
Ask user for an IP address
  ↓
Send IP to geolocation API
  ↓
Receive location & network information
  ↓
Display the results
```

## 🛠️ Requirements

- **Python 3.14**
- Some library
- Internet connection

Install via `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

Run the main Python file:

```bash
python main.py
```

The application will first show your public IP address and then ask you to enter an IP address to look up.

Example:

```text
Your Public IP: xxx.xxx.xxx.xxx

Input IP: 8.8.8.8

Country: United States (US)
Region: Virginia (VA)
City: Ashburn
Zip: 20149
ISP: Google LLC
Latitude: 39.03
Longitude: -77.5
Organization: Google Public DNS
```

## ⚠️ Location Accuracy Notice

The location information provided by this application is **estimated using IP-based geolocation**.

IP geolocation is not always accurate. The displayed city or region may be different from the IP user's actual location because of ISP infrastructure, network routing, VPNs, proxies, mobile networks, and other factors.

**This software does not use GPS and cannot determine someone's exact physical location or home address.**

The displayed location should therefore be treated as an **approximation**.

## 🔌 API

This project uses an **IP geolocation API** to retrieve information about the IP address entered by the user.

The general process is:

```text
IP Address
    ↓
Geolocation API
    ↓
Country
Region
City
Coordinates
ISP
Organization
```

## 📁 Project Structure

```text
IP-Location-Finder/
│
├── main.py
├── api.py
├── requirement.txt
├── README.md
└── .gitignore
```

## 🎯 Purpose

This project was created as a **Python learning project** to practice:

- API requests
- JSON data
- Working with external APIs
- User input
- Data extraction
- Error handling

## 📜 License

This project is created for **learning and educational purposes**.

Feel free to study, modify, and improve the code.

---

**Made with Python 🐍**
