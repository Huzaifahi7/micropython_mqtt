import time
import machine
from umqttsimple import MQTTClient
mqtt_server = 'mqttdns.eastus.cloudapp.azure.com'
topic_sub = 'testin'
led=machine.Pin(2,machine.Pin.OUT)
def sub_cb(topic, msg):
    try:
        led.value(int(msg))
    except:
        pass
keepalive=60
client = MQTTClient('usergoets1', mqtt_server,port=1883,user='',password='',keepalive=keepalive)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic_sub)
reset_timer=0
while True:
    msg=client.check_msg()
    time.sleep(1)
    reset_timer+=1
    if reset_timer>=keepalive-5:
        reset_timer=0
        client.disconnect()
        client.connect()
        client.subscribe(topic_sub)  