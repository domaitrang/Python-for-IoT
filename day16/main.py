# Import thu vien
import paho.mqtt.client as mqtt
import speech_recognition as sr

# create a speech recognition object
r = sr.Recognizer()
# Ket noi den MQTT
user = "Nwk9FyEvPB4UCCghNSESIwA"
password = "UPKMs21CdKrGS8cb6aZnFqVU"

client = mqtt.Client(client_id="Nwk9FyEvPB4UCCghNSESIwA")
client.username_pw_set(username=user, password=password)
client.connect(host="mqtt3.thingspeak.com", port=1883)

topic = "channels/2218493/publish/fields/field3"

# Nhan lenh -> gui len broker
with sr.Microphone() as source:
    while True:
        # read the audio data from the default microphone
        print("Say something:")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data, language="vi-VN")
        print(text)
        if ("bật đèn xanh" in text):
            client.publish(topic, '1')
        elif ("tắt đèn xanh" in text):
            client.publish(topic, '0')
        elif ("bật đèn vàng" in text):
            client.publish(topic, '3')
        elif ("tắt đèn vàng" in text):
            client.publish(topic, '2')
        elif ("bật đèn đỏ" in text):
            client.publish(topic, '5')
        elif ("tắt đèn đỏ" in text):
            client.publish(topic, '4')
        elif ("tắt toàn bộ" in text):
            client.publish(topic, '-1')
        elif ("bật toàn bộ" in text):
            client.publish(topic, '100')
        elif ("tạm biệt" in text):
            print("Kết thúc chương trình")
            break
