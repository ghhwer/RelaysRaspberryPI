import RPi.GPIO as GPIO
from time import sleep

class relayShiftRegisterModule:
        def __init__(self,DATA_PIN, CLK_PIN, CLK_INTERVAL=0.00109, number_of_relays=4):
                """
                Sets up class variables and any I/O needed
                """
                self.DATA_PIN = DATA_PIN
                self.CLK_PIN = CLK_PIN
                self.CLK_INTERVAL = CLK_INTERVAL
                self.number_of_relays = number_of_relays
                GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
                GPIO.setup(self.DATA_PIN, GPIO.OUT)
                GPIO.setup(self.CLK_PIN, GPIO.OUT)
                GPIO.output(self.DATA_PIN, 0)
                GPIO.output(self.CLK_PIN, 0)

        def data_burst(self,data):
                """
                Sends a raw 8 bit given by data
                """

                data_bin = '{:08b}'.format(data)
                for x in range(8):
                        #Clock High
                        GPIO.output(self.CLK_PIN,1)
                        #Send Data and Wait
                        GPIO.output(self.DATA_PIN, bool(int(data_bin[x])))
                        sleep(self.CLK_INTERVAL)
                        #Clock Low and Wait
                        GPIO.output(self.CLK_PIN,0)
                        sleep(self.CLK_INTERVAL)

        def reset_module(self):
                """
                Reset module by sending 0 to the shifter register
                """
                self.data_burst(0)

        def set_relays(self,relays):
                """
                Sets relays encoded within a vector
                """
                data = 0
                for x in range(1,self.number_of_relays+1):
                        if x in relays:
                                data += 2**x
                self.data_burst(data)

        def set_single_relay(self, relay_index):
                """
                Sets relay given by its 'index'
                """
                self.data_burst(2**relay_index)

        def clean_up(self):
                """
                cleans up I/O
                """
                GPIO.cleanup()