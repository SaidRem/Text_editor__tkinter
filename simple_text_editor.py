from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def text_editor(root):
    root.title('Simple text editor')

    root.rowconfigure(0, minsize=800, weight=1)
    root.columnconfigure(1, minsize=800, weight=1)

    txt_edit = Text(root)

    fr_buttons = Frame(root)
    btn_open = Button(fr_buttons, text='OPEN', command=(lambda: open_file(txt_edit, root)))
    btn_save = Button(fr_buttons, text='Save as...', command=(lambda: save_file(txt_edit, root)))

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

def open_file(txt_edit, root):
    """Open file for editing
    :param txt_edit: Text widget from tkinter.
    :param root: Main window.
    """
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")],
    )

    if not filepath:
        return None

    txt_edit.delete("1.0", END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    root.title(f"Simple Text Editor - {filepath}")

def save_file(txt_edit, root):
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"),
                   ("All Files", "*.*")],
    )
    if not filepath:
        return None
    
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", END)
        output_file.write(text)
    root.title(f"Simple text editor - {filepath}")


if __name__ == '__main__':
    root = Tk()
    text_editor(root)

    root.mainloop()