# Welcome to my first vityarthi project in python
# QR Generator by Yug pratap
## Overview of the project
This is a desktop application built using python that gives a user-friendly interface(GUI) for generating QR codes. Users can input any text or URL and even chosse custom colours for the background and can also embed a logo into the center of the QR code. The application ensures high error correction so that QR remain scannable even when a logo is added to it.

## Features
- Text/URL Input: Generates a QR for any provided text or website link.

- Customizable Colours: Use any color for the QR and fill the background.

- Logo Embedding: select a local image to place in the center of the QR code.

- Save to File: Easily save the generated QR code image locally as a PNG file via a file dialog.

- Trick : Includes a button that does a trick.

## Technologies/tools used
1.Python: The programming language used for the project.

2.Tkinter : The standard Python interface that is used to create buttons and labels.

3.qrcode: An external library used to generate the actual QR code.

3.Pillow (PIL): The Python Imaging Library that is used for creating and pasting the optional logo.

## Steps to install & run the project
- Prerequisites: make sure you have Python installed on your system.

- Download: Download the file to your local machine.

- Install the libraries : Open your terminal and install the required external libraries using pip

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

2.In the "Enter text or URL" field, type a website or txt.

3.Click the "choose Fill Color" button and select a color other than black.

4.Click the "choose Background Color" button and select a color

5.To add a logo.Click "Choose Logo" and select a small image file from your computer.

6.Click the "Generate QR Code" button.

7.Give a filename and save it.

8.sometime try the easter egg too :) 

9.Open the file and use QR scanner app on your phone to scan it.

## Screenshots 
<img width="607" height="395" alt="Screenshot 2025-11-25 184818" src="https://github.com/user-attachments/assets/6ab81764-1c45-47d1-a4a2-87b74afee477" />
<img width="710" height="556" alt="Screenshot 2025-11-25 184832" src="https://github.com/user-attachments/assets/eb0c86a6-1b7a-4290-982d-1b43909da515" />
<img width="979" height="773" alt="Screenshot 2025-11-25 184912" src="https://github.com/user-attachments/assets/49ce7171-758f-4632-840e-b7206ec4ae62" />
<img width="654" height="652" alt="Screenshot 2025-11-25 184935" src="https://github.com/user-attachments/assets/0dd5bf1c-3762-40bb-9de9-021ac58d83c6" />



