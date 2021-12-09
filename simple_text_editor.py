from tkinter import *

def text_editor(root):
    root.title('Simple text editor')

    root.rowconfigure(0, minsize=800, weight=1)
    root.columnconfigure(1, minsize=800, weight=1)

    txt_edit = Text(root)

    fr_buttons = Frame(root)
    btn_open = Button(fr_buttons, text='OPEN')
    btn_save = Button(fr_buttons, text='Save as...')

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

if __name__ == '__main__':
    root = Tk()
    text_editor(root)

    root.mainloop()