from tkinter import *

root = Tk()
root.title("Add Image Tool")


# file frame
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, text="Add Image")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="Delete Image")
btn_del_file.pack(side="right")


# list frame
list_frame = Frame(root)
list_frame.pack()

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)




root.resizable(False, False)
root.mainloop()
