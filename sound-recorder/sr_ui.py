 
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI")

# Create a label widget
label = tk.Label(root, text="Sound Recorder")
label.pack(pady=20)
# for switching stop and start

# Create a button widget
def on_click():
    with open('sound_recorder.py') as f:
        exec(f.read())

Start_btn = tk.Button(root, text="start", command=on_click)

# Stop_btn = tk.Button(root, text="stop", command=lambda: print("Button clicked!"))

Start_btn.pack(pady=10)


# Run the application
root.mainloop()
