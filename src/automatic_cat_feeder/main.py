
import time
#import os
import datetime
import read_stream
#import led

frame = ""




def run(initial_time):
  #read_stream.fetch_frame(initial_time)
  read_stream.identify_cat(frame)



if __name__ == "__main__":
  
  time.sleep(2)
  #led.setup_led()
  #setup_servo()
  #led.ok_led()
  initial_time = datetime.datetime.now()
    
  try:
    #led.ok_led()
    run(initial_time)
    
  except Exception as error:
    #led.error_led()
    print(error)  
    #os.system("shutdown -r")
      
     

