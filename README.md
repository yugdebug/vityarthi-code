# Welcome to my first vityarthi project in python
# QR Generator by Yug pratap
## Overview of the project
This is a desktop application built using python that gives a user-friendly interface(GUI) for generating QR codes. Users can input any text or URL and even chosse custom colours for the background and can also embed a logo into the center of the QR code. The application ensures high error correction so that QR remain scannable even when a logo is added to it.

## Features
- Text/URL Input: Generates a QR for any provided text or website link.

- Customizable Colours: Use any colour for the QR and fill the background.

- Logo Embedding: select a local image file (PNG, JPG, JPEG) to place in the center of the QR code.

- Save to File: Easily save the generated QR code image locally as a PNG file via a file dialog.

- Trick : Includes a button that does a trick.

## Technologies/tools used
1.Python 3: The programming language used for the project.

2.Tkinter: The standard Python interface to the Tk GUI toolkit that used to create buttons and labels.

3.qrcode: An external library used to generate the actual QR code.

3.Pillow (PIL): The Python Imaging Library that is used for creating and pasting the optional logo.

## Steps to install & run the project
- Prerequisites: Ensure you have Python installed on your system.

- Download: Download the script file to your local machine.

- Install Dependencies: Open your terminal or command prompt and install the required external libraries using pip:

```python
pip install qrcode 
pip install pillow
```
-run the code : in terminal
```python
python your_filename.py
```
## Instructions for testing
1.Launch the application.

2.In the "Enter text or URL" field, type a known website or txt.

3.Click the "Pick Fill Colour" button and select a colour other than black.

4.Click the "Pick Background Colour" button and select a colour other than white. Ensure there is a contrast with the fill colour.

5.(Optional) Click "Choose Logo" and select a small image file from your computer.

6.Click the green "Generate QR Code" button.

7.provide a filename (ex: test_qr.png) and save it.

8.sometime try the easter egg too :) 

9.Open the saved file and use a QR scanner app on your mobile device to scan it.
