import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Add Image Tool")


# file frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="Add Image")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="Delete Image")
btn_del_file.pack(side="right")


# List frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# Save path frame
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True)

btn_dest_path = Button(path_frame, text="Search")
btn_dest_path.pack(side="right")


# Option frame
frame_option = LabelFrame(root, text="option")
frame_option.pack(padx=5, pady=5, ipady=5)

# Width option
lbl_width = Label(frame_option, text="Width")
lbl_width.pack(side="left")

# Width combo
opt_width = ["Keep Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left")

# Space option
lbl_space = Label(frame_option, text="Space")
lbl_space.pack(side="left")

# Space combo
opt_space = ["None", "Narrow", "Middle", "Wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left")

# Format option
lbl_format = Label(frame_option, text="Format")
lbl_format.pack(side="left")

# Format combo
opt_format = ["PNG", "JPEG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left")

# Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# Run frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, text="Close", command=root.quit)
btn_close.pack(side="right")

btn_run = Button(frame_run, text="Run")
btn_run.pack(side="right")

root.resizable(False, False)
root.mainloop()
