
import cv2  
import os
import time


#import identify_cat
#import servo

import datetime




def fetch_frame(initial_time):
    
    
    reboot_time = initial_time + datetime.timedelta(hours=2)
    
    #interpreter = identify_cat.setup_tensors()
    
    initialState = None  
    
    rebooting = False

    motionTrackList= [ None, None ]  


    video = cv2.VideoCapture(0)  


    input_folder = "/home/pi/automatic_cat_feeder/camera_input"
    
    if not os.path.exists(input_folder):
            os.makedirs(input_folder)

    
    check, cur_frame = video.read()  
    
    
    if check:
        print("waiting for movement")
        if os.path.exists(input_folder + "/test.jpg"):
            os.remove(input_folder + "/test.jpg")
        cv2.imwrite(input_folder + "/test.jpg", cur_frame)

        
    else:
        raise Exception("No frame detected")
    
    #cv2.imwrite(input_folder + "/test.jpg", cur_frame)  



    while True:

        time.sleep(0.5)
        now = datetime.datetime.now()
        
        if now > reboot_time and not rebooting:
            os.system("shutdown -r")
            rebooting = True
        
        check, cur_frame = video.read()  
        #cv2.imwrite(input_folder + "/test.jpg", cur_frame)  

        
        var_motion = 0        

        gray_image = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)  
        gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)  

        if initialState is None:  
            initialState = gray_frame  
            continue  

        differ_frame = cv2.absdiff(initialState, gray_frame)  
        thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]  
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)  


        cont,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

    

        for cur in cont:  
            if cv2.contourArea(cur) < 10000:  
                continue  

            var_motion = 1  
        # cv2.rectangle(cur_frame, (cur_x, cur_y), (cur_x + cur_w, cur_y + cur_h), (0, 255, 0), 3)  

        

        motionTrackList.append(var_motion)  
        motionTrackList = motionTrackList[-2:]  

        year = now.year
        month = now.month if len(str(now.month))==2 else '0' + str(now.month)
        day = now.day if len(str(now.day))==2 else '0' + str(now.day)

        hour = now.hour if len(str(now.hour))==2 else '0' + str(now.hour)
        minute = now.minute if len(str(now.minute))==2 else '0' + str(now.minute)
        second = now.second if len(str(now.second))==2 else '0' + str(now.second)
        

    
        if (motionTrackList[-1] == 1 and motionTrackList[-2] == 0) or (motionTrackList[-1] == 0 and motionTrackList[-2] == 1):                
            #motionTime.append(datetime.datetime.now())  
            frames = []
        
            #frame = resize_frame(cur_frame)
            
            #frames.append(frame)
                        
            
            #for _ in range (10):
                #time.sleep(0.2)
                #check, frame = video.read()
                #if check:
                    #frame = resize_frame(frame)
                    #frames.append(frame)
                
             
            #cat = identify_cat.identify(frame, interpreter)
    
            #print(cat)
            
            cv2.imwrite(input_folder + f"/{str(year) + str(month) + str(day)}-{str(hour) + str(minute) + str(second)}.jpg", cur_frame)
            
            for i in range (10):
                time.sleep(0.1)
                check, frame = video.read()
                if check:
                    cv2.imwrite(input_folder + f"/{str(year) + str(month) + str(day)}-{str(hour) + str(minute) + str(second)}/{str(i)}.jpg", frame)

                    


            
            #servo.open_bowl(cat)

    

            #cat = 'cat'
            
            
            #return flip_frame


        #if motionTrackList[-1] == 0 and motionTrackList[-2] == 1:  
            #motionTime.append(datetime.datetime.now())
            
            
def resize_frame(frame):
    frame = cv2.flip(frame, 0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (400, 400), interpolation = cv2.INTER_AREA)
    frame = (frame / 255.).astype("float32").reshape(1, 400, 400, 3)
    
    return frame

            


    

    
    

