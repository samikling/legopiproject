"""
File: legoPi.py

Talla ohjelmalla voidaan ajaa neliveto robotti autoa, joka on rakennettu Joy-it 4wd-robokitin pohjalta.


website: www.github.com/samikling
Date: 02/12/2020
"""

__author__ = "Jenni Breite & Sami Kling"
__version__ = "0.1.0"
__licence__ = "MIT"

import RPi.GPIO as GPIO
import curses
from time import sleep

# Maaritetaan pinnit 
#Moottori 1
Motor1A = 12
Motor1B = 14
Motor1E = 15
#Moottori 2
Motor2A = 23
Motor2B = 24
Motor2E = 25
#Moottori 3
Motor3A = 13
Motor3B = 4
Motor3E = 17
#Moottori 4
Motor4A = 27
Motor4B = 22
Motor4E = 9
#Curses asetukset, ikkuna, echo pois, valiton tila, ja arvot
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def setup():
	GPIO.setmode(GPIO.BCM)				# GPIO Numerointi
	GPIO.setup(Motor1A,GPIO.OUT)  # Maaritetaa kaikki pinnit ulostuloiksi
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)
 	#Motor 2
	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)
	#Motor 3
	GPIO.setup(Motor3A,GPIO.OUT)
	GPIO.setup(Motor3B,GPIO.OUT)
	GPIO.setup(Motor3E,GPIO.OUT)
	#Motor 4
	GPIO.setup(Motor4A,GPIO.OUT)
	GPIO.setup(Motor4B,GPIO.OUT)
	GPIO.setup(Motor4E,GPIO.OUT)

def stop():
	#Kaikki moottorit seis
	print('Stop')
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor4A,GPIO.LOW)

def eteen():
	#Kaikki moottorit eteenpain
	print('Forward')
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.LOW)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.LOW)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.HIGH)
	GPIO.output(Motor3E,GPIO.LOW)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.HIGH)
	GPIO.output(Motor4E,GPIO.LOW)

def taakse():
	#Kaikki moottorit taaksepain
	print('Backwards')
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)

def vasemmalle():
	#Moottorit 1 ja 3 Eteenpain, 2 ja 4 Taaksepain.
	print('Turning Left')
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.LOW)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.HIGH)
	GPIO.output(Motor3E,GPIO.LOW)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)

def oikealle():
	#Moottorit 1 ja 3 taakseppain, 2 ja 4 eteenpain.
	print('Turning Right')
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.LOW)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)

	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.HIGH)
	GPIO.output(Motor4E,GPIO.LOW)



def destroy():
	#Pinnien 'puhdistus'
	GPIO.cleanup()

if __name__ == '__main__':     # Paaohjelma ajetaan tassa.
	setup()
	try:
		while True:
			char = screen.getch()
			if char == ord('q'):
				break
			elif char == curses.KEY_UP:
				eteen()
			elif char == curses.KEY_DOWN:
				taakse()
			elif char == curses.KEY_RIGHT:
				oikealle()
			elif char == curses.KEY_LEFT:
				vasemmalle()
			else:
				stop()
	finally:
	#Sammutetaan curses rutiinit ja havitetaan pinnien tiedot!
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()
		destroy()
