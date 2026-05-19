from PIL import ImageTk
from tkinter import simpledialog, filedialog
import tkinter as tk
from ctypes import windll
import qrcode

windll.shcore.SetProcessDpiAwareness(1)

content = str(simpledialog.askstring("QR Code Generator", "Enter the content of the QR code:"))
qr = qrcode.make(content)

root = tk.Tk()
root.title("QR Code Generator")
root.resizable(False, False)

img = ImageTk.PhotoImage(qr)
qr_label = tk.Label(root, image=img)
qr_label.image = img
qr_label.pack()

tk.Button(root, text="Save QR Code", command=lambda: qr.save(filedialog.asksaveasfilename(
    initialfile="QR Code",
    defaultextension=".png",
    filetypes=[
        ("Image File", "*.png"),
        ("Image File", "*.jpg"),
        ("Image File", "*.jpeg"),
        ("Image File", "*.webp"),
        ("Image File", "*.bmp"),
        ("All Files", "*.*")
    ]
))).pack(fill="x")

root.mainloop()