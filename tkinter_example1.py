# from tkinter import *
# frame=Tk()
# l1=Label(frame,text="username:")
# l2=Label(frame,text="Password:")

# entry=Entry(frame)
# entry2=Entry(frame)
# l1.grid(row=0,column=0)
# entry.grid(row=0,column=1)
# l2.grid(row=1, column=0)
# entry2.grid(row=1,column=1)
# btn=Button(frame,text="Login",fg="red",bg="black")
# btn.grid(row=2, column=0)

#Photo Image
# import tkinter as tk

# root = tk.Tk()
# root.title("PhotoImage Example")

# # Use a raw string for the file path
# image_path = r"c:\Users\python\Pictures\Saved Pictures\rough.jfif"  # Replace with the actual path to your image

# # Create a PhotoImage object
# image = tk.PhotoImage(file=image_path)

# # Create a Label widget to display the image
# image_label = tk.Label(root, image=image)
# image_label.pack(padx=10, pady=10)

# # Start the Tkinter event loop
# root.mainloop()
from tkinter import * 
from tkinter import messagebox 
  
root = Tk() 

  
# w = Label(root, text ='GeeksForGeeks')  
# w.pack() 
  
# messagebox.showinfo("showinfo", "Information") 
  
# messagebox.showwarning("showwarning", "Warning") 
  
# messagebox.showerror("showerror", "Error") 
  
# messagebox.askquestion("askquestion", "Are you sure?") 
  
# messagebox.askokcancel("askokcancel", "Want to continue?") 
  
# messagebox.askyesno("askyesno", "Find the value?") 
  
  
# messagebox.askretrycancel("askretrycancel", "Try again?")   
  
# root.mainloop()  
# from tkinter import *

# root = Tk()
# root.title("Simple Checkbutton Example")

# # Create a BooleanVar to store the check state
# check_var = BooleanVar()

# # Create a Checkbutton widget
# check_button = Checkbutton(root, text="Check me", )
# check_button2 = Checkbutton(root, text="click me", )
# check_button.pack()
# check_button2.pack()

# # Start the Tkinter event loop
# root.mainloop()
# import tkinter as tk

# root = tk.Tk()
# root.title("Simple OptionMenu Example")

# # Create a StringVar to store the selected option
# selected_option = tk.StringVar()

# # Set default value and available options
# value_inside = StringVar(root) 
  
# # Set the default value of the variable 
# value_inside.set("Select an Option") 
# selected_option.set("Option 1")
# options = ["Option 1", "Option 2", "Option 3"]

# # Create OptionMenu widget
# option_menu = tk.OptionMenu(root, selected_option, *options)
# option_menu.pack(pady=10)

# Start the Tkinter event loop
# root.mainloop()


#radio Button
# import tkinter as tk

# root = tk.Tk()
# root.title("RadioButton Example")

# # Create a StringVar to store the selected option
# selected_option = tk.StringVar()

# # Set default value and available options for radio buttons
# selected_option.set("Option 1")
# options = ["Option 1", "Option 2", "Option 3"]

# # Create and place radio buttons
# for option in options:
#     radio_button = tk.Radiobutton(root, text=option, variable=selected_option, value=option)
#     radio_button.pack(pady=5)

# # Create a Label to display the selected option
# label = tk.Label(root, textvariable=selected_option)
# label.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Listbox Example")

# # Create a Listbox widget
# listbox = tk.Listbox(root, selectmode=tk.SINGLE)
# listbox.pack(pady=10)

# # Add items to the Listbox
# items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
# for item in items:
#     listbox.insert(tk.END, item)

# # Start the Tkinter event loop
# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Menu Example")

# # Create a menu bar
# menu_bar = Menu(root)
# root.config(menu=menu_bar)

# # Create a File menu
# file_menu = Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Add items to the File menu
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.destroy)

# # Create an Edit menu
# edit_menu = tk.Menu(menu_bar, tearoff=0)
# menu_bar.add_cascade(label="Edit", menu=edit_menu)

# # Add items to the Edit menu
# edit_menu.add_command(label="Cut")
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")

# # Start the Tkinter event loop
# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Panel Example")

# Create a frame to resemble a panel
panel_frame = tk.Frame(root, bg="lightgray", padx=20, pady=20)
panel_frame.pack(padx=10, pady=10)

# Add widgets to the panel frame
label = tk.Label(panel_frame, text="This is a panel", font=("Helvetica", 16), bg="lightgray")
label.pack(pady=10)

button = tk.Button(panel_frame, text="Click me", command=root.destroy)
button.pack()

# Start the Tkinter event loop
root.mainloop()
