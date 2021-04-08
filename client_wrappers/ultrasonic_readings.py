import RPi.GPIO as GPIO
import time
import ssl
import paho.mqtt.client as mqtt
import uuid

unique_id = uuid.uuid4().hex

while True:
    try:
        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 7
        PIN_ECHO = 11

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        print("Waiting for sensor to settle")

        time.sleep(2)

        print("Calculating distance")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        distance_calculated = "Distance:"+str(distance)+ " cm"
        print(distance_calculated)

        
        client = mqtt.Client(client_id=unique_id)
        client.username_pw_set(
            username="commandandcontrol", password="Qpc423hwdM")
        client.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
        client.connect("cwlicc.zapto.org", 8883, 60)
        client.publish("user1_pi1_sensor1",
                       distance_calculated, retain=True)
        client.loop()
        client.disconnect()

        client = mqtt.Client(client_id='RPi-000000000078')
        client = mqtt.Client(client_id='RPi-000000000078')

    finally:
        GPIO.cleanup()
    time.sleep(0.005)
