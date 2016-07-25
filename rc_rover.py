#########################################################

# PiWars 2015 code for 'BuddenBot' 

# All code is written by Henry Budden (aged 15), 
# 	using the RRB2 library authored by Simon Monk as well as 
#	some commands written by Matthew Hawkins (Raspberry Pi Spy) 
#	to read commands from the Wiimote.

# This program allows the robot to be controlled manually 
# 	via a Wiimote that is connected to the Pi via Bluetooth.
# 	It is worth noting that pressing the left/right buttons on the
#	4-way joystick makes the robot turn slowly left/right while also 
#	travelling forwards. Pressing the 1/2 buttons on the right of the 
#	Wiimote will make the robot turn quickly left/right on the spot.
#	Furthermore, the robot will be controlled using the Wiimote held
#	in a landscape fashion, meaning that all comments referring to the
#	'left button' are actually referring to the up button when held 
#	upright.

#########################################################

# Import relevant libraries
import cwiid
import time
import rrb2 as rrb
from squid import *

rgb = Squid(26,19,13)

rr = rrb.RRB2(revision=2)

# Ensure that the other outputs are set to off to conserve battery energy
rr.set_led1(0)
rr.set_led2(0)
rr.set_oc1(0)
rr.set_oc2(0)

# Set up button delay variable
button_delay = 0.1

# Inform user how to begin connection of the Wiimote to the 
#	Raspberry Pi
print 'Press 1 + 2 on your Wii Remote now ...'
rgb.set_color(YELLOW)
time.sleep(1)

# Attempts to connect to the Wiimote. 
try:
  wii=cwiid.Wiimote()
# If connection to Wiimote fails then the program will stop and 
#	print error message to the terminal.
except RuntimeError:
  rgb.set_color(RED)
  print "Error connecting to Wiimote"
  time.sleep(1)
  quit()

# Once connected, brief instructions are displayed on the terminal 
#	and Wiimote rumbles for 1 second
rgb.set_color(GREEN)
print "Wiimote connected..."
print "Press some buttons!"
print "Press PLUS and MINUS together to quit."
wii.rumble=1
time.sleep(1)
wii.rumble=0

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print "Closing connection"
    rgb.set_color(RED)
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check which button is pressed, print real-world values to terminal
  #		and control the rrb2's motors accordingly
  
  if (buttons & cwiid.BTN_LEFT):
    print 'Down pressed'
    rr.set_motors(1,1,1,1)
    time.sleep(button_delay)        
    rr.set_motors(0,0,0,0) 
	
  if(buttons & cwiid.BTN_RIGHT):
    print 'Up pressed'
    rr.set_motors(1,0,1,0)
    time.sleep(button_delay)
    rr.set_motors(0,0,0,0)          

  if (buttons & cwiid.BTN_UP):
    print 'Left pressed'        
    rr.set_motors(0.5,0,1,0)
    time.sleep(button_delay)
    rr.set_motors(0,0,0,0)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Right pressed'      
    rr.set_motors(1,0,0.5,0)
    time.sleep(button_delay)  
    rr.set_motors(0,0,0,0)
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    rr.set_motors(1,1,1,0)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    rr.set_motors(1,0,1,1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          
 
  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)

  # If abort button (SW2 is pressed)
  if rr.sw2_closed()==True:
		# Turn off all motors
		rr.set_motors(0,0,0,0)
		# Set RGB LED to RED
		rgb.set_color(RED)
		time.sleep(1)
		# Exit program
		exit()

