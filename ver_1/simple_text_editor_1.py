from tkinter import *


class Text_Editor(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        if text:
            self.settext(text, file)
        
    def makewidgets(self):
        """Widgets for Text Editor."""
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(sid=LEFT, expand=YES, fill=BOTH)
        self.text = text
    
    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')  # Set cursor insert.
        self.text.focus()                  # Mouse click on the text widget.

if __name__ == '__main__':
    root = Tk()
    te = Text_Editor()
    root.mainloop()
