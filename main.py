from tkinter import simpledialog, filedialog
from customtkinter import ThemeManager
import customtkinter as ctk
import qrcode
import re

def grayfix(colors):
    return [re.sub(r"gray(\d+)", r"#\1\1\1", i) for i in colors]

darker, lighter = grayfix(ThemeManager.theme["CTk"]["fg_color"])

content = simpledialog.askstring("QR Code Generator", "Enter the content of the QR code")
print(content)
qr_setup = qrcode.QRCode()
qr_setup.add_data(content)
qr = qr_setup.make_image(fill_color=darker, back_color=lighter).get_image()

root = ctk.CTk()
root.title("QR Code Generator")
root.resizable(False, False)

img = ctk.CTkImage(light_image=qr, dark_image=qr, size=qr.size)
ctk.CTkLabel(root, text="", image=img).pack(padx=10, pady=10)

ctk.CTkButton(root, text="Save QR Code", command=lambda: qr.save(filedialog.asksaveasfilename(
    initialfile="qrcode.png",
    defaultextension=".png",
    filetypes=[("PNG file", "*.png"), ("All files", "*.*")]
))).pack(fill="x", padx=10, pady=(0, 10))

root.mainloop()