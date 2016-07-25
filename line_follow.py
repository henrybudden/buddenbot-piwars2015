#########################################################

# PiWars 2015 code for 'BuddenBot' 

# All code is written by Henry Budden (aged 15), 
# 	using the RRB2 library authored by Simon Monk.

# This program uses the robot's IR line sensor 
#	modules to follow a black line on a white 
#	surface. As well as moving, the code also
#	prints the real-world values of the two sensors
#	at 0.25 second intervals. The program asks the 
#	user to input the speed that they require, then 
#	waits until the on-board button (SW1) is pressed
#	before starting to move. If the button is pressed 
#	again, the program pauses, waiting for the button
#	to be pressed in order to resume.

# The IR line sensor modules work by shining an IR LED
#	(not visible to the human eye, as the wavelength of
#	the light is just longer than visible light. If the 
#	surface underneath the sensor is white, then the IR
# 	light is reflected, which can be picked up by the IR 
#	detector, creating a logic low, however, when the surface
#	underneath the sensor is black, the light does not get
#	reflected and a logic high is produced.

#########################################################

# Import relevant python libraries 
import rrb2 as rrb 
import RPi.GPIO as GPIO
import time
from squid import *

# Set up library values
rgb = Squid(26,19,13)
rr = rrb.RRB2(revision=2)

# Set GPIO numbering mode to BCM in order to receive values from
#	the IR line sensor modules, whose signal pins are attached to
# 	raspberry pi GPIO pins.
GPIO.setmode(GPIO.BCM)

# Create an array for the two input pins to save repetition later
#	in the code.
ir_pins = [20,21]

# Set up the two GPIO pins listed above as inputs, as they are the
#	signal pins from the two IR line sensor modules.
GPIO.setup(ir_pins, GPIO.IN)

# Set up variables for the input pins and the potential results
#	in order to make them less potentially confusing, by giving them
#	real-world values, for use later in the code.
left = 21
right = 20
black = True
white = False

# Turn on the two 'open collector' outputs of the RRB2 controller board,
#	as they are used to supply 5V each to the two IR line sensor modules.
rr.set_oc1(1)
rr.set_oc2(1)

# Turn off built in LEDs to conserve battery
rr.set_led1(0)
rr.set_led2(0)

# Allow the user to input the speed at which they would like the robot to 
# 	run at, before printing it, to allow the user to double check it is 
#	correct.
speed = float(raw_input("Enter desired speed, from 0 to 1 (0.8 is best): "))
print "The speed entered was ", speed, "."

print "Press SW2 to begin following lines" 

while True:
	# If SW2 is pressed, wait 0.5 seconds to ensure that it isn't registered twice
	if rr.sw2_closed() == True:
		time.sleep(0.5)
		while True:
			rgb.set_color(GREEN)
			# If the button is pressed, stop all motors, display a message to
			#	the user informing them that the program has paused, wait 1 second, 
			#   then break to the previous loop in order to wait for the button to 
			#   be pressed to resume the line following.
			if rr.sw1_closed()== True:
				# Turn all motors off
				rr.set_motors(0,0,0,0)
				print "Line following paused"
				# Set RGB LED to yellow
				rgb.set_color(YELLOW)
				time.sleep(1)
			# If the left IR line sensor module is reading the ground as being black
			#	(on the line), then check the right sensor.
			if GPIO.input(left) == black:
				# If both left and right are black, continue in a straight line, and
				#	display real-world values to the user.
				if GPIO.input(right) == black:
					rr.set_motors(speed,0,speed,0)
					print "Left and Right Black" 
				# If left is black and right is white, turn left to stay on the line and
				#	display real-world values to the user.
				elif GPIO.input(right) == white:
					rr.set_motors(speed,1,speed,0)
					print "Left Black and Right White"
			# If the left IR line sensor module is reading the ground as being white
			#	(not on the line), then check the left sensor.
			elif GPIO.input(left) == white: 
				# If left is white and right is black, turn right to stay on the line and
				#	display real-world values to the user.
				if GPIO.input(right) == black:
					rr.set_motors(speed,0,speed,1)
					print "Left White and Right Black"
				# If both left and right are white, continue in a straight line, and
				#	display real-world values to the user.
				elif GPIO.input(right) == white:
					rr.set_motors(speed,0,speed,0)
					print "Left and Right White"
			# If abort button (SW2 is pressed)
			if rr.sw2_closed()==True:
				# Turn off all motors
				rr.set_motors(0,0,0,0)
				# Set RGB LED to RED
				rgb.set_color(RED)
				time.sleep(1)
				# Exit program
				exit()
		# Wait for 0.25 seconds before looping
		time.sleep(0.25)
