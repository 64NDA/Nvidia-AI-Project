# Rock Paper Scissors Using AI

This projects allows you to play rock paper scissors using real hand gestures. 
Images/DEMO_screenshot.png
[Image of Program Running](https://i.imgur.com/2vUfgM6.png)

## The Algorithm

This program uses an AI model trained to recognise certain hand gestures. Using this AI it plays rock paper scissors with the user.  
It first takes a picture of the user and their hand inputs with a webcam. It then uses this webcam image and plugs it into the AI model. The AI model decides what hand gesture the image is depicting. It takes the depicted image as an input value for whether the user plays rock, paper or scissors.  
The computer's decision is processed via a random number generator. The two values are then compared to decides who wins the round. Rounds are continuously played until the user stops the program.  
  
sidenote: The AI was trained to be able to recognise a few other hand gestures: "Paper", "Rock", "Scissors(like a peace sign)", "OK", "Point/One", "Thumbs Up", "Thumbs Down". Since, I trained the AI model myself, it may not be extremely accurate.

## Running this project

1. Make sure Python and PIP is up to date and install all necessary modules listed in python_modules https://github.com/64NDA/Nvidia-AI-Project/blob/main/Python_Modules.
2. Make sure all files inside of the Gesture_AI_Project file are downloaded together and remain within the same folder.
3. Run the GestureAIProject.py file.
4. Wait. The camera takes some time to connect.
5. When the camera connects, another window labelled test should appear with a video output of the webcam. Further instructions should appear in the terminal.
6. With the test window selected, Spacebar can be pressed to input an image. The program will then run.
7. Escape can be pressed to exit the program.

[View a video explanation here](video link)
