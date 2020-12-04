"""
File: legoPi.py

Talla ohjelmalla voidaan ajaa neliveto robotti autoa, joka on rakennettu Joy-it 4wd-robokitin pohjalta.


website: www.github.com/samikling
Date: 02/12/2020
"""

__author__ = "Jenni Breite & Sami Kling"
__version__ = "0.1.1"
__licence__ = ""

import RPi.GPIO as GPIO
import curses
from time import sleep

# Define pinout 
#Motor 1
Motor1A = 2
Motor1B = 3
Motor1E = 4
#Motor 2
Motor2A = 9
Motor2B = 10
Motor2E = 11
#Motor 3
Motor3A = 13
Motor3B = 15
Motor3E = 12
#Motor 4
Motor4A = 23
Motor4B = 24
Motor4E = 25
#Set up curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def setup():
	GPIO.setmode(GPIO.BCM)				# GPIO Numbering
	GPIO.setup(Motor1A,GPIO.OUT)  # Set all pins as outputs
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

def forward():
	#All motors forward
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

def backwards():
	#All motors backwards
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

def left():
	
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

def right():
	
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
	GPIO.cleanup()

if __name__ == '__main__':     #Run main
	setup()
	try:
		while True:
			char = screen.getch()
			if char == ord('q'):
				break
			elif char == curses.KEY_UP:
				forward()
			elif char == curses.KEY_DOWN:
				backwards()
			elif char == curses.KEY_RIGHT:
				right()
			elif char == curses.KEY_LEFT:
				left()
			else:
				stop()
	finally:
	#clear curses and shutdown the program.
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()
		destroy()
