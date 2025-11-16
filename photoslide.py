from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image paths
image_paths = [
    r"C:\users\rahul\OneDrive\Pictures\IMG20251017120102.jpg",
    r"C:\users\rahul\OneDrive\Pictures\WhatsApp Image 2025-09-30 at 11.46.32 PM (1).jpeg",
    r"C:\users\rahul\OneDrive\Pictures\IMG20240714200301.jpg",
]

# Resize the images to 720x720
image_size = (720, 720)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

# Create an iterator that cycles through images
slideshow = cycle(photo_images)

def update_image():
    # Get next image from cycle
    next_image = next(slideshow)
    label.config(image=next_image)
    label.image = next_image  # Keep reference to prevent garbage collection
    # Schedule next update after 3 seconds (3000 ms)
    root.after(3000, update_image)

def start_slideshow():
    update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()
