# This Python file uses the following encoding: utf-8
import os,sys
from upm import pyupm_jhd1313m1 as lcd
import mraa
import time
import sys
import math

buttonCounter=0
buttonState=0
lastButtonState=0


temptPin=0
tempt=mraa.Aio(temptPin)
temptValue=0

soundPin=1
sound=mraa.Aio(soundPin)
soundSensorValue=0

lightPin=2
light=mraa.Aio(lightPin)
lightValue=0

buttonPin=mraa.Gpio(2)
buttonPin.dir(mraa.DIR_IN)

lcdDisplay=lcd.Jhd1313m1(0, 0x3E , 0x62)    #LCD initialization

while True:
    buttonState=buttonPin.read()
    if buttonPin.read()!=lastButtonState:
        if (buttonPin.read()==1):
            buttonCounter=buttonCounter+1
    lastButtonState=buttonPin.read()
    time.sleep(5)
    
    if buttonCounter==1: 
        lightValue=float(light.read())
        print "Isik Degeri= "+str(lightValue)
        lcdDisplay.clear()
        lcdDisplay.setCursor(0,0)
        lcdDisplay.write("Isik Degeri="+str(lightValue))
        time.sleep(5)
    elif buttonCounter==2:   
        B=3975
        temptValue = float(tempt.read())
        resistance = (float)(1023 - temptValue) * 10000 / temptValue
        temperature = 1 / (math.log(resistance / 10000) / B + 1 / 298.15) - 273.15
        print "Sicaklik Degeri="+str(temperature)
        lcdDisplay.setCursor(0,0)
        lcdDisplay.clear()
        lcdDisplay.write("Sicaklik Degeri=")
        lcdDisplay.setCursor(0,1)
        lcdDisplay.write(str(temperature))
        time.sleep(5)
    elif buttonCounter==3:   
        soundSensorValue = float(sound.read())
        print "Ses Degeri="+str(soundSensorValue)
        lcdDisplay.clear()
        lcdDisplay.setCursor(0,0)
        lcdDisplay.write("Ses Degeri="+str(soundSensorValue))
        time.sleep(5)



