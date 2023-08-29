
import time
#import sys
import os
import datetime



#path = os.path.abspath("/home/pi/automatic_cat_feeder/src")
#sys.path.append(path)



import read_stream
import led




def run(initial_time):
  read_stream.fetch_frame(initial_time)



if __name__ == "__main__":
  
  time.sleep(2)
  led.setup_led()
  #setup_servo()
  led.ok_led()
  initial_time = datetime.datetime.now()
    
  try:
    led.ok_led()
    run(initial_time)
    
  except Exception as error:
    led.error_led()
    print(error)  
    os.system("shutdown -r")
      
     

