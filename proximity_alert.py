#########################################################

# PiWars 2015 code for 'BuddenBot' 

# All code is written by Henry Budden (aged 15), 
# 	using the RRB2 library authored by Simon Monk.

# This program uses an ultrasonic range-finder (HC-SR04) which
#	is attached to the RRB2 controller board. The program allows 
#	the robot to move forwards until the robot reaches a desired 
#	distance from the nearest object in front of it, where it will 
#	then stop. The program starts by asking the user to input the 
#	minimum distance required before the robot stops, and the 
#	required time interval between robot movements, then the code
#	waits for the user to press the button SW1, before the robot 
#	precedes forwards until the pre-defined distance is reached, 
#	then the robot will stop.

# The HC-SR04 range-finder works by emitting a short pulse of 
#	ultra-sound, which is inaudible to the human ear, as the 
#	frequency of the sound is above that of audible levels (between 
#	20Hz and 20KHz). The range-finder then starts a timer, and 
#	listens for the echo of the sound. When the reflected sound is 
#	received by the sensor, the timer is stopped. As the time reflects 
#	how long the sound took to travel both from the robot to the 
#	object, and back again, the time is then divided by 2, before 
#	using the calculation distance = speed * time to calculate the 
#	distance from the robot to the object. As the speed of sound in air 
#	is roughly 34300cm/s the distance can be calculated by using 
#	time/2 * 34300, which will give the distance in centimetres. This 
#   calculation is performed by the rrb2 function 'rr.get_distance()'.

#########################################################

# Import relevant python libraries 
import rrb2 as rrb
import RPi.GPIO as GPIO
import time
from squid import *

# Set up library values
rgb = Squid(26,19,13)
rr = rrb.RRB2(revision=2)

# Ensure that the other outputs are set to off to conserve battery energy
rr.set_led1(0)
rr.set_led2(0)
rr.set_oc1(0)
rr.set_oc2(0)

# Set up distance variable
distance = 0

# Inform user that SW2 needs to be pressed in order for the robot to commence
#	movement.

print "Press SW2 to Begin"
rgb.set_color(YELLOW)

while True:
	# If SW2 is pressed, wait 0.5 seconds to ensure that it isn't registered twice
	if rr.sw2_closed() == True:
		time.sleep(0.5)
		while True:
			# Set RGB LED to green
			rgb.set_color(GREEN)
			time.sleep(0.1)
			# Set distance variable to the value of the rangefinder
			distance = rr.get_distance()
			# If the button is pressed, stop all motors, display a message to
			#	the user informing them that the program has paused, wait 1 second, 
			#   then break to the previous loop in order to wait for the button to 
			#   be pressed to resume the line following.
			if rr.sw1_closed()== True:
				# Turn all motors off
				rr.set_motors(0,0,0,0)
				print "Proximity Alert paused, press SW2 to restart"
				# Set RGB LED to yellow
				rgb.set_color(YELLOW)
				time.sleep(1)
			# If the distance infront of the rangefinder is greater than 2cm
			if distance > 2:
				# Set both motors forwards at 0.8 speed
				rr.set_motors(0.8,0,0.8,0)
			# If the distance infront of the rangefinder is less than 2 cm
			elif distance < 2:
				# Turn both motors off
				rr.set_motors(0,0,0,0)
				# Inform user that the minimum distance had been reached
				print "Minimum distance reached"
				while True:	
					# Turn motors off and flash RGB LED red
					rgb.set_color(RED)
					time.sleep(0.5)
					rgb.set_color(OFF)
					time.sleep(0.5)
					rr.set_motors(0,0,0,0)
					if rr.sw2_closed() == True:
						rgb.set_color(CYAN)
						time.sleep(1)
						break
			# If abort button (SW2 is pressed)
			if rr.sw2_closed()==True:
				# Turn off all motors
				rr.set_motors(0,0,0,0)
				# Set RGB LED to RED
				rgb.set_color(RED)
				time.sleep(1)
				# Exit program
				exit()
