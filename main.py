import wificonnect_api as wapi
import cloud as cloud
import sample as waterP
import soil_moisture as sm
import time

wapi.connect_to_wifi()

print("d")
temparture,humidity,condition,icon=wapi.fetch_weather_data()
soilD=sm.read_soilmoistureDigital()
soilA=sm.read_soilmoistureAnalog()
cloud.publish(temparture,humidity,condition,soilD,soilA)
cloud.subscribe()
    


