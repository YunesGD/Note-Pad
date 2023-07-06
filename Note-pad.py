import tkinter as tk
import tkinter.filedialog

window = tk.Tk()
window.title('Note-Pad')
window.geometry("300x300")


# Set variable for open file name
global Open_status_name
Open_status_name = False

# Set variable for selected TExt
global selected
selected = False


files_types = [('Text Document (.txt)', '*.txt')]


def New_File(event=None):
    txt.delete('1.0', tk.END)
    window.title('New File - Text Box')

    # Set variable for open file name
    global Open_status_name
    Open_status_name = False


def Open_File(event=None):
    txt.delete('1.0', tk.END)

    fd = tkinter.filedialog.askopenfilename(
        initialdir='C:/Users/*/Desktop', title='Open File', filetypes=files_types)

    # check to see if there is a file name
    if fd:
        # Make filename global so we can access it later
        global Open_status_name
        Open_status_name = fd

    name = fd.split('/')[-1]
    window.title(f'{name} - Text Box')

    # Open The File
    fd = open(fd, 'r')
    stuff = fd.read()
    # Add File to textbox
    txt.insert(tk.END, stuff)
    # Close the Opened File
    fd.close()


def Save_As_File(event=None):
    fd = tkinter.filedialog.asksaveasfilename(
        defaultextension=".*", initialdir='C:/Users/*/Desktop', title='Save As File', filetypes=files_types)

    # check to see if there is a file name
    if fd:
        # Make filename global so we can access it later
        global Open_status_name
        Open_status_name = fd

    if fd:
        # Update Status Bars
        name = fd.split('/')[-1]
        window.title(f'{name} - Text Box')

        # Save the file
        fd = open(fd, 'w')
        fd.write(txt.get(1.0, tk.END))
        # Close the file
        fd.close()


def Save_File(event=None):
    global Open_status_name

    if Open_status_name:
        # Save the file
        fd = open(Open_status_name, 'w')
        fd.write(txt.get(1.0, tk.END))
        # Close the file
        fd.close()
    else:
        Save_As_File()


def Exit(event=None):
    window.quit()


def Cut_text(event=None):
    global selected
    # check to see if we used keyboard shortcuts
    if event:
        selected-window.clipboard_get()
    else:
        if txt.selection_get():
            # Garb Selected Text FromText Box
            selected = txt.selection_get()
            # Delete Selected Text From Text Box
            txt.delete('sel.first', 'sel.last')
            # clear the clipboard than append
            window.clipboard_clear()
            window.clipboard_append(selected)


# Copy Text
def Copy_text(event=None):
    global selected
    # check to see if we used keyboard shortcuts
    if event:
        selected = window.clipboard_get()

    if txt.selection_get():
        # Garb Selected Text FromText Box
        selected = txt.selection_get()
        # clear the clipboard than append
        window.clipboard_clear()
        window.clipboard_append(selected)


# Paste Text
def Paste_text(event=None):
    global selected
    # check to see if we used keyboard shortcuts
    if event:
        selected-window.clipboard_get()
    else:
        if selected:
            position = txt.index(tk.INSERT)
            txt.insert(position, selected)


def Delete_text(event=None):
    # Delete previous text
    txt.delete('1.0', tk.END)


def showMenu(event):
    edit_menu.post(event.x_root, event.y_root)


menu1 = tk.Menu(master=window)
window.config(menu=menu1)

# Add File Menu
file = tk.Menu(menu1, tearoff=0)
menu1.add_cascade(label="File", menu=file)
file.add_command(label="New", command=New_File, accelerator="Ctrl+N")
file.add_command(label="Open", command=Open_File, accelerator="Ctrl+O")
file.add_command(label="Save", command=Save_File, accelerator="Ctrl+S")
file.add_command(label="Save as", command=Save_As_File, accelerator="F2")
file.add_separator()
file.add_command(label="Exit", command=Exit, accelerator="Ctrl+Q")

# Add Edit Menu
edit_menu = tk.Menu(menu1, tearoff=0)
menu1.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=Cut_text, accelerator='Ctrl+X')
edit_menu.add_command(label="Copy", command=Copy_text, accelerator='Ctrl+C')
edit_menu.add_command(label="Paste", command=Paste_text, accelerator='Ctrl+V')
edit_menu.add_command(label="Delete All",
                      command=Delete_text, accelerator='Ctrl+D')


txt = tk.Text(window)
txt.pack()
window.bind("<Control-o>", Open_File)
window.bind("<Control-s>", Save_File)
window.bind("<Control-n>", New_File)
window.bind("<F2>", Save_As_File)
window.bind("<Control-q>", Exit)

window.bind("<Control-x>", Cut_text)
window.bind("<Control-c>", Copy_text)
window.bind("<Control-v>", Paste_text)

window.bind('<Button-3>', showMenu)

window.mainloop()
