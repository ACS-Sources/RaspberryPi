import time
import RPi.GPIO as GPIO

def LED_off(pin_number):
    print("LED Pin" +  str(pin_number) + " off")
    GPIO.output(pin_number, False)
    
def LED_on(pin_number):
    print("LED Pin" + str(pin_number) + " on")
    GPIO.output(pin_number, True)

    
if __name__ == "__main__":
    my_pin = 8
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(my_pin, GPIO.OUT)
    
    
    print("Start: LED steuern")
    LED_on(my_pin);
    time.sleep(1)
    LED_off(my_pin)
    
    #--
    time.sleep(1)
    #--
    
    LED_on(my_pin);
    time.sleep(1)
    LED_off(my_pin)
    
    print("Ende: LED steuern")
