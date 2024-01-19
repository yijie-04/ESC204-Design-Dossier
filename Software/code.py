# Import libraries needed for blinking the LED
import board
import digitalio
# Configure the GPIO pin connected to the LEDs as a digital output
led = digitalio.DigitalInOut(board.GP16) # blue LED
led.direction = digitalio.Direction.OUTPUT
led1 = digitalio.DigitalInOut(board.GP19) # red LED
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP12) # white LED
led2.direction = digitalio.Direction.OUTPUT
# Configure the GPIO pin connected to the button for global LED on/off as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Configure the GPIO pin connected to the switch button for white LED on/off as a digital input
switch = digitalio.DigitalInOut(board.GP14)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Print a message on the serial console
# print('Hello! My LED is controlled by the button.')
last_state = button.value # initialize last button state variable
last_switch = switch.value # initialize last switch button state variable
state = 0 # initialize state of on/off button
signal_edge = 0 # initialize button signal edge variable

# Loop so the code runs continuously
while True:
    signal_edge = 0 # set button signal edge to 0 by default
    if last_state != button.value: # check if a button signal edge occurs
        last_state = button.value # update last button state
        if button.value == False: # check if the edge corresponds to a True -> False state
            signal_edge = 1 # assign a True signal edge
    state = signal_edge^state # calculate and set state as next state (based on FSM analysis)
    # assign the blue and red LEDs the boolean variable state
    led.value = state
    led1.value = state
    # allow changes in switch button if the blue and red LEDs are True
    if state != 0:
        if last_switch != switch.value: # check if a switch button signal edge occurs
            last_switch = switch.value # update last switch button state
            if switch.value == False: # check if the edge corresponds to a True -> False state
                if led2.value == False: # check if white LED is off
                    led2.value = True # turn the LED on
                else: # white LED is on
                    led2.value = False # turn the LED off
    else:
        led2.value = False # if state of blue and red LEDs are off, then white LED is off as well
