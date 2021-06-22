import network
import time

ssid='801'
passwd='123456789.'
def wifiConnect(ssid, password):
    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected() :
        print("will connect to wifi Route")
        wifi.active(True)
        wifi.connect(ssid, password)
        while not wifi.isconnected():
            time.sleep(1)
    if wifi.isconnected():
        print('network config:', wifi.ifconfig())            
wifiConnect(ssid,passwd)


