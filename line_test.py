#########################################################

# PiWars 2015 code for 'BuddenBot' 

# All code is written by Henry Budden (aged 15), 
# 	using the RRB2 library authored by Simon Monk.

# This program uses the robot's IR line sensor 
#	modules to print the real-world values of the 
#	two sensors at 0.25 second intervals.

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

while True:
	# If the left IR line sensor module is reading the ground as being black
	#	(on the line), then check the right sensor.
	if GPIO.input(left) == black:
		# If both left and right are black, display real-world values to the user.
		if GPIO.input(right) == black:
			print "Left and Right Black"
		# If left is black and right is white, display real-world values to the user.
		elif GPIO.input(right) == white:
			print "Left Black and Right White"
	# If the left IR line sensor module is reading the ground as being white
	#	(not on the line), then check the left sensor.
	elif GPIO.input(left) == white: 
		# If left is white and right is black, display real-world values to the user.
		if GPIO.input(right) == black:
			print "Left White and Right Black"
		# If both left and right are white, display real-world values to the user.
		elif GPIO.input(right) == white:
			print "Left and Right White"
	# Wait for 0.25 seconds before looping
	time.sleep(0.25)