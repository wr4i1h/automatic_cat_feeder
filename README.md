# Cat automatic feeder


It's my first (kinda) big project with python and my absolute first with tensor flow and image recognition so it is far from perfect, any suggestion is more than welcome.

Python tensor flow (lite because my raspberry pi 3b works better with it) image recognition to recognise which cat is approaching the tray with the 2 bowls and move the correct servo to open the bowl with the right food (Persephone needs food for urinary health/stones, Eris needs weight management food).

For training, I am mostly follow the tensor flow tutorial to use a pre-trained model. Keras has a list of all the pre-trained models along with the size and accuracy. I chose a light model but that still has a good accuracy, Xception. 

I let the camera take picture with only the motion recognition working for a while to take pictures when the cats were approaching to collect some data, then I did the training on google colab, after some research deciding to try to work with 20 epoch. Seems enough for now, I'm still collecting pictures while the bowls are operating (and saving them with the prediction in the name + timestamp) so I can check accuracy and improve the model. 

I am having some issue with frames of videos in which both of the cats show: I don't want any bowl to open in that case because the wrong cat will eat from that too but my model can only recognise one object per frame. I'm considering building some structure so only one cat can approach each bowl and maybe have one camera per bowl or try to find another model still light enough to run on raspberry. Right now it's not that big of an issue because if they start eating together one gets bothered quite fast and leaves. 

The camera is behind the bowls, I'm resizing the pictures to 400x400 to fit the model. I'm using a Raspberry Pi Camera Module with Automatic IR-Cut-Off-Filter 175° wide angle lens but any camera should work. If not IR and the cats are used to eat during the night maybe it's better to put some lights like led or something around the bowls.

I have 3d printed a tray that fits two double bowls per side (dry and wet food) and has 2 single lids, each controlled by a servo connected to the pi. In the middle there is a space for the pi with a removable lid. I also connected 2 leds to be able to see if everything is working correctly without having to connect to the raspberry and a button to open both lids to fill the bowls. 

To control the servos I used @adafruit very useful library. Work and instructions here   
https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
https://github.com/adafruit/Adafruit_CircuitPython_Bundle 

Every 2 hours the system reboots



