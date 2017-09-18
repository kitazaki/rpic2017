#!/usr/bin/python
import RPi.GPIO as GPIO
from flup.server.fcgi import WSGIServer
import time, sys, urlparse

# set up GPIO pin number
gp_out = 18

def app(environ, start_response):
     start_response("200 OK", [("Content-Type", "text/html")])
     i = urlparse.parse_qs(environ["QUERY_STRING"])
     yield (' ')
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(gp_out, GPIO.OUT)
     servo = GPIO.PWM(gp_out, 50) 
     if "q" in i:
          if i["q"][0] == "o":
               servo.start(0.0)
               # 0 degree
               servo.ChangeDutyCycle(7.25)
               time.sleep(0.5)
          elif i["q"][0] == "c":
               servo.start(0.0)
               # +90 degree
               servo.ChangeDutyCycle(11.5)
               time.sleep(0.5)
     GPIO.cleanup()

WSGIServer(app).run()

