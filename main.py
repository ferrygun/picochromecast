import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("", "")
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    
    
from urlencode import urlencode
from picochromecast import play_url

url = 'https://translate.google.com/translate_tts?client=tw-ob&' + urlencode({'q': 'Hello, 世界', 'tl': 'ja'})
play_url(url, '192.168.50.23')
