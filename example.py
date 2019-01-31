from time import sleep
from relays import relayShiftRegisterModule

def routine_a(r):
        active_relays = []
        r.reset_module()
        active_relays = []
        for x in range(1,r.number_of_relays+1):
                active_relays.append(x)
                r.set_relays(active_relays)
                sleep(1)
def routine_b(r):
    r.reset_module()
    for x in range(1,r.number_of_relays+1):
            r.set_single_relay(x)
            sleep(1)

if __name__ == '__main__': # Program starting from here 
        try:
                r = relayShiftRegisterModule(13,11,number_of_relays=4)
                while True:
                	routine_a(r)
                	routine_b(r)

        except KeyboardInterrupt:  
                r.clean_up()  