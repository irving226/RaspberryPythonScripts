from picamera import picamera #color
from time import sleep

camera= PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/documents/source/Python/PiCam')
camera.stop_preview()     

##if the camera preview is upside down use this code
#camera=PiCamera()
#camera.rotation=180

#it's advised to make the cam preview see thru to debug while its running
#camera.start_preview(alpha=200)  #alpha can be anything between 0-255

camera.start_perview()
for i in range(5):
    sleep(5)
    camera.capture('/documents/source/Python/PiCam' % i)
camera.stop_preview()

#loops from 0 to 5, taking a photo and annotating the corresponding saved photo



#video recording with the camera

#camera.start_preview
#camera.start_recording('/documents/source/Python/PiCam')
#sleep(5)
#camera.stop_recording()
#camera.stop_preview()

#changing the image settings and add image effects
camera.resolution=(2562,1944)
camera.framework=15
camera.start_prewview()
sleep(5)
camera.capture('/documents/source/Python/PiCam/max.jpg')
camera.stop_preview()

# #if you wanted to add text to the image 
# #camera.start_preview()
# #camera.annotate_text="hello world"
# sleep(5)
# camera.capture('/documents/source/Python/PiCam/text.jpg')
# camera.stop_preview()

##camera.annotate_text_size=50
# camera.start_preview()
# camera.annotate_background=Color('blue')
# camera.annotate_foreground=Color('yellow')
# camera.annotate_text="hello world"
# sleep(5)
# camera.stop_preview

#changing the preview brightness
# camera.start_preview()
# camera.brightness=70
# sleep(5)
# camera.capture('/documents/source/Python/PiCam/bright.jpg')
# camera.stop_preview()


#loop adujusting the brightnewss and also adds text to display the current brightness level
# camera.start_preview()
# for i in range(100):
#     camera.annotate_text="Brightness: %s" % i
#     camera.brightness=1
#     sleep(0.1)
# camera.stop_preview()


# #changing the contrast
# camera.start_preview()
# for i in range(100):
#     camera.annotate_text= "Contrast: %s" % i
#     camera.contrast=1
#     sleep(0.1)
# camera.stop_preview()


# #image effects: none negative solarize sketch denoise emboss etc
# camera.start_preview()
# camera.image_effect='colorswap'
# sleep(5)
# camera.capture('/documents/source/Python/PiCam/colorswap.jpg')
# camera.stop_preview()
