#pip install qrcode
#pip install pillow

import webbrowser
import qrcode
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

#my fav video about QR code i watched a while back
def easter():
    webbrowser.open("https://www.youtube.com/watch?v=w5ebcowAJD8")

#simple color choose but please choose the default as sometime u might not see the qr
def choose_color(n):
    color_code=colorchooser.askcolor(title="Choose color")[1]
    if color_code:
        n.set(color_code)

#last time i went to a restraunt i saw them use there logo qr to order so, got function to to maybe add them for them
def choose_logo():
    example_logo=filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if example_logo:
        logo_path.set(example_logo)

#the main qr generator function to use
def generate_a_qr_code():
    data=entry.get()
    if not data:
        messagebox.showwarning("input is required")
        return

    qr=qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_H,
                     box_size=20,
                     border=7)

    qr.add_data(data)
    qr.make(fit=True)
    qr_one=qr.make_image(fill_color=fill_color.get(),
                         back_color=back_color.get()).convert("RGB")

    if logo_path.get():
        try:
            logo=Image.open(logo_path.get())

            qr_width, qr_height=qr_one.size

            logo_size=int(qr_width / 4.5)
            logo=logo.resize((logo_size,
                               logo_size))
            position=((qr_width - logo_size) // 2,
                  (qr_height - logo_size) // 2)

            qr_one.paste(logo, 
                         position,
                          mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            messagebox.showerror("Logo Error",
                                  f"Cannot to add a logo: {e}")

    filename=filedialog.asksaveasfilename(defaultextension=".png", 
                                          filetypes=[("PNG files", "*.png")])
    if filename:
        qr_one.save(filename)
        messagebox.showinfo("__Done__")


#basic main 
main=tk.Tk()
main.title("__QR Code Generator by Yug__")
tk.Label(main,
         text="Enter some text or URL: ").pack(pady=6)
entry=tk.Entry(main, width=70)
entry.pack(pady=6)
fill_color=tk.StringVar(value="black")
back_color=tk.StringVar(value="white")
logo_path=tk.StringVar(value="")

#buttons in a line to better see for changes
tk.Button(main, 
          text="choose Fill Color",
          command=lambda: choose_color(fill_color)).pack(pady=2)
tk.Button(main, 
          text="choose Background Color", 
          command=lambda: choose_color(back_color)).pack(pady=2)
tk.Button(main, 
          text="Choose Logo (optional)", 
          command=choose_logo).pack(pady=2)
tk.Button(main, 
          text="some knowledge ", 
          command=easter, 
          fg="blue").pack(pady=2)
tk.Button(main, 
          text="Generate QR Code", 
          command=generate_a_qr_code, 
          bg="pink", 
          fg="white").pack(pady=10)

#final line to show the app
main.mainloop()
