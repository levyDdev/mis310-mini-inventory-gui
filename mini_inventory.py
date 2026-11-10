# MIS 310 - Class Practice: Mini Inventory GUI

from tkinter import *

# Add an equipment name to the list.
def add_equipment():
    name = equipment_entry.get().strip()

    if name == "":
        message_label.config(text="Please enter an equipment name.")
    else:
        equipment_list.insert(END, name)
        equipment_entry.delete(0, END)
        message_label.config(text="")
        update_count()


# Update the number of equipment entries.
def update_count():
    total = equipment_list.size()
    count_label.config(text="Number of entries: " + str(total))


# Close the program.
def quit_program():
    window.destroy()


# Create the main window.
window = Tk()
window.title("Mini Inventory")
window.geometry("400x350")

title_label = Label(window, text="Equipment Inventory", font=("Arial", 14))
title_label.pack(pady=10)

# Use a Frame and grid() for the entry form.
form_frame = Frame(window)
form_frame.pack(pady=5)

equipment_label = Label(form_frame, text="Equipment Name:")
equipment_label.grid(row=0, column=0, padx=5, pady=5)

equipment_entry = Entry(form_frame, width=22)
equipment_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = Button(form_frame, text="Add", command=add_equipment)
add_button.grid(row=1, column=0, columnspan=2, pady=5)

message_label = Label(window, text="", fg="red")
message_label.pack()

# Display equipment in a Listbox with a vertical Scrollbar.
list_frame = Frame(window)
list_frame.pack(pady=5)

equipment_list = Listbox(list_frame, width=35, height=8)
equipment_list.pack(side=LEFT)

scrollbar = Scrollbar(list_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

equipment_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=equipment_list.yview)

count_label = Label(window, text="Number of entries: 0")
count_label.pack(pady=5)

quit_button = Button(window, text="Quit", command=quit_program)
quit_button.pack(pady=5)

window.mainloop()
