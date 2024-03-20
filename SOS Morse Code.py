# Morse Code For S.O.S 
# which is ... --- ...


import winsound
import time

DELAY_TIME = 0.25  # in Seconds
FREQUENCY = 1300  # in Hertz


def dot():
    # Short beep for Dot
    winsound.Beep(FREQUENCY, 200)
    # Makes a beep in certain frequency for 200 milliseconds

def dash():
    # Beep for dash (longer than dot beep)
    winsound.Beep(FREQUENCY, 450)

def delay(delay_time):
    # Delay between every character and every sentence
    time.sleep(delay_time)
    # Makes a certain delay in seconds

def S():
    dot()
    dot()
    dot()
    delay(DELAY_TIME)


def O():
    dash()
    dash()
    dash()
    
    delay(DELAY_TIME)

for i in range(3):
    S()
    O()
    S()
    delay(1)






