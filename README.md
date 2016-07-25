The Code in this directory was written by Henry Budden (Aged 15) for entry into the 2015 PiWars Competition
with his robot "BuddenBot".

All code was written by Henry, but has used the RaspberryPiRobot2 Board designed by Simon Monk, and using the
library of commands also authored by Simon Monk.

Below is a overview of the functions of the programs in this directory:

	line_follow.py - Rover follows line using two IR sensors mounted on front of robot. This program will be used in 
					the line following challenge
	line_test.py - Rover prints out real-world values of the IR sensors to the terminal. This program will be used to 
					test hardware in anticipation for the line following challenge.
	proximity_alert.py - Rover commences forwards towards an object, then stops, using an ultrasonic range finder. This
					program will be used in the proximity alert challenge.
	range_test.py - Rover prints distance in front of ultrasonic range-finder to the terminal. This program will be used to
					test hardware in anticipation for the proximity alert challenge.
	rc_rover.py - Rover is controlled manually via a Wiimote connected via Bluetooth. This program will be used in the
					obstacle course, straight line speed test, robot vs robot duel and skittles challenges.

  					
Furthermore, there are two additional directories in the home directory:
	
	rrb2-1.1 - This is the home for the library of commands for the rrb2 authored by Simon Monk
	
	squid - This is the home for the library of commands for the raspberry squid (RGB LED) authored by Simon Monk
