import machine
import network
import urequests
import time



# Weather API credentials and URL
weather_api_key = '8577f110b6da435a86a74743232506'
weather_api_url = 'https://api.weatherapi.com/v1/current.json?q=12.5613,77.3315&key=' + weather_api_key


wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Connect to Wi-Fi
def connect_to_wifi():
    # Wi-Fi credentials
    wifi_ssid = input("enter the wifi ssid : ")
    wifi_password = input("enter the password : ")
    if not wifi.isconnected():
        print('Connecting to Wi-Fi...')
        wifi.connect(wifi_ssid, wifi_password)
        while not wifi.isconnected():
            pass
    print('Connected to Wi-Fi:', wifi_ssid)
    print('IP address:', wifi.ifconfig()[0])


def fetch_weather_data():
    
    response = urequests.get(weather_api_url)
    weather_data = response.json()
    response.close()
    
    
    current_data = weather_data['current']
    temperature_c = current_data.get('temp_c')
    humidity = current_data.get('humidity')
    condition = current_data.get('condition', {}).get('text')
    icon = current_data.get('condition', {}).get('icon')
    
    
    return temperature_c,humidity,condition,icon
    

