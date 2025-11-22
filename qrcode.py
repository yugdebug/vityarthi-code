#pip install qrcode

#pip install pillow

import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

def generate_qrcode():
    data=entry.get()
    if not data:
        messagebox.showwarning("input is required", "please enter some text or URL")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=7,)
    qr.add_data(data)
    qr.make(fit=True)

    qr_img=qr.make_image(fill_color=fill_color.get(), back_color=back_color.get()).convert("RGB")

    if logo_path.get():
        try:
            logo=Image.open(logo_path.get())
            qr_w, qr_h= qr_img.size

            logo_size= int(qr_w / 4)
            logo= logo.resize((logo_size, logo_size))
            pos= ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)

            qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            messagebox.showerror("Logo Error", f"Failed to add logo: {e}")

    filename= filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        qr_img.save(filename)
        messagebox.showinfo("__Done__", f"QR Code saved as {filename}")

def choose_color(var):
    color_code= colorchooser.askcolor(title="Choose colour")[1]
    if color_code:
        var.set(color_code)

def choose_logo():
    path= filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path:
        logo_path.set(path)

root= tk.Tk()
root.title("QR Code Generator by Yug")
tk.Label(root,text="Enter text or URL:").pack(pady=5)
entry= tk.Entry(root, width=67)
entry.pack(pady=5)

fill_color = tk.StringVar(value="black")
back_color = tk.StringVar(value="white")
logo_path = tk.StringVar(value="")

tk.Button(root, text="Pick Fill Colour", command=lambda: choose_color(fill_color)).pack(pady=2)
tk.Button(root, text="Pick Background Colour", command=lambda: choose_color(back_color)).pack(pady=2)
tk.Button(root, text="Choose Logo (optional)", command=choose_logo).pack(pady=2)

tk.Button(root, text="Generate QR Code", command=generate_qrcode, bg="green", fg="white").pack(pady=10)

root.mainloop()