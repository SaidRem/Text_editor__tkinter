from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Text_Editor(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        if text:
            self.settext(text, file)
        self.master.title('Text Editor')
        self.menu_bar()
        
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
    
    def menu_bar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.file_open_menu()
    
    def file_open_menu(self):
        pulldown = Menu(self.menubar, tearoff=False)
        pulldown.add_command(label='Open File', command=self.open_file)
        pulldown.add_command(label='Save as...', command=self.notdone)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
    
    def open_file(self):
        """Open File Explorer to select a file."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"),
                       ("html", "*.html"),
                       ("All Files", "*.*")],
        )
        if filepath:
            self.settext(file=filepath)
                
    
    def notdone(self):
        showerror('Not implemented', 'Not available')

if __name__ == '__main__':
    # root = Tk()
    Text_Editor().mainloop()
    # root.mainloop()
