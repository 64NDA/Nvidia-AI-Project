import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import tensorflow
import numpy as np
import argparse
import time
import random

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0


model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
classes = ["Paper", "Rock", "Scissors", "OK", "Point/One", "Thumbs Up", "Thumbs Down"]

##random number for rock paper scissors
## 0=paper, 1=rock, 2=scissors
def random_number():
    rand = random.randrange(0, 3)
    return rand

## rock papers scissors
def RPS(bot, user):
    output = ""
    if bot == user:
        output = "The bot picked the same as you. It's a draw."
    elif bot == 0 and user == 1:
        output = "The bot chose paper. You lose :("
    elif bot == 0 and user == 2:
        output = "The bot chose paper. You win! :)"
    elif bot == 1 and user == 0:
        output = "The bot chose rock. You win! :)"
    elif bot == 1 and user == 2:
        output ="The bot chose rock. You lose :("
    elif bot ==  2 and user == 0:
        output ="The bot chose scissors. You lose :("
    elif bot == 2 and user == 1:
        output ="The bot chose scissors. You win! :)"
    return output
        
print("This is rock paper scissors.")
print("Raise your hand to the camera with a palm to select paper. ")
print("Raise your hand to the camera with a fist to select rock. ")
print("Raise your hand to the camera with a peace sign to select scissors. ")
print("To input, press the spacebar. To exit press escape.")

while True:
    ##Instructions
    
    
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        #takes image
        #Rock paper scissors game
        ran = random_number()
        #
        


        
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        #gives ample time to upload image
        time.sleep(0.5)
        ##OpensImage
        image = Image.open('opencv_frame_0.png')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        
        # run the inference
        prediction = model.predict(data)
        print("Confidence level in all classes: " + str(prediction))
        greatest_guess = 0
        index = 0
        count = 0
        for predictions in prediction:
          for guess in predictions:
            if guess > greatest_guess:
              greatest_guess = guess
              index = count
            count+= 1
        
        
        #Output
        print("Class with greatest confidence was: " + str(classes[index]))
        print("With a confidence of: " + str(greatest_guess))
        ##returning guess value
        if index == 0 or index == 1 or index == 2 and greatest_guess>0.95 :
            guess = index
        else:
            guess = 3
            print("That hand gesture is not a valid input. Or the AI isn't confident enough in your input.")
            

        print(RPS(ran,guess))
        

cam.release()

cv2.destroyAllWindows()

