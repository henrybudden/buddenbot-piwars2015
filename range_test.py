#########################################################

# PiWars 2015 code for 'BuddenBot' 

# All code is written by Henry Budden (aged 15), 
# 	using the RRB2 library authored by Simon Monk.

# This program makes the robot take distance measurements from 
#	the ultrasonic range-finder attached on the front every 0.5
#	seconds, and print the values (cm).

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


#Import relevant libraries
import rrb2 as rrb
import time

rr = rrb.RRB2(revision=2)

# Ensure that the other outputs are set to off to conserve battery energy
rr.set_led1(0)
rr.set_led2(0)
rr.set_oc1(0)
rr.set_oc2(0)

# Inform the user of the next procedure
print("The program will now continually show the distance infront of the rangefinder")

# Wait for 2 seconds to allow time for the user to move the rover away from any objects
time.sleep(2)

# Forever
while True:
	# Print the distance in front of the range-finder followed by its units (cm)
	print rr.get_distance(), "cm"
	time.sleep(0.5)
