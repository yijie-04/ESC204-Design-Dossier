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
# Print a message on the serial console
# print('Hello! My LED is controlled by the button.')
last_state = button.value # initialize last_state variable
state = 0 # initialize state variable

# Loop so the code runs continuously
while True:
    if state == 0: # state = 0 case, all LEDs False
        led.value = False
        led1.value = False
        led2.value = False

        if last_state != button.value: # check if button was pressed
            last_state = button.value # update button state
            if button.value == False: # check if the signal edge corresponds to a True -> False state
                state = 1 # update LED state
            else:
                state = 0 # update LED state

    elif state == 1: # state = 1 case, red and blue LED on
        led.value = True
        led1.value = True
        led2.value = False

        if last_state != button.value: # check if button was pressed
            last_state = button.value # update button state
            if button.value == False: # check if the signal edge corresponds to a True -> False state
                state = 2 # update LED state
            else:
                state = 1 # update LED state
    
    elif state == 2: # state = 2 case, all LED on
        led.value = True
        led1.value = True
        led2.value = True
        
        if last_state != button.value: # check if button was pressed
            last_state = button.value # update button state
            if button.value == False: # check if the signal edge corresponds to a True -> False state
                state = 0 # update LED state
            else:
                state = 2 # update LED state
