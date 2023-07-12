# Import thu vien
import paho.mqtt.client as mqtt
# Ket noi den MQTT
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
# Nhan lenh -> gui len broker 
while True:
    tmp = input('Nhap lenh: ')
    if(tmp.lower() == "exit"):
        print("Thoát")
        break
    else:
        topic, msg = tmp.split("-")
        client.publish(topic, msg)

