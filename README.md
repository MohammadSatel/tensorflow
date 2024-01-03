# Image Recognition GUI with Python, TensorFlow, and Tkinter

# Overview
This project demonstrates a simple image recognition graphical user interface (GUI) built using Python, TensorFlow, and Tkinter. The application allows users to open an image file, and it uses a pre-trained MobileNetV2 model to classify whether the image contains a dog, a car, or another object.

# Requirements
Make sure you have the required Python libraries installed before running the application using requerements.txt

# Usage
Clone or download this repository to your local machine.
Open a terminal and navigate to the project directory.
Run the script: python image_recognition_gui.py
The GUI window will appear. Click the "Open Image" button to choose an image file for classification.
The script will display the selected image in the GUI and provide the predicted class (e.g., dog, car) in the result label.

# Dependencies
TensorFlow: https://www.tensorflow.org/
Tkinter: Included in Python standard library
Pillow (PIL Fork): https://pillow.readthedocs.io/

# Model information
The application uses the MobileNetV2 model pre-trained on the ImageNet dataset. The model is automatically downloaded during the first run of the script.