from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.brush_size = 1
        self.brush_color = "black"
        self.color = "black"
        self.setUI()
        
        
    def setUI(self):
        self.parent.title("Simple Paint")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(7, weight=1)
        self.rowconfigure(2, weight=1)
        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind('<B1-Motion>', self.draw)
        self.canv.bind('<ButtonRelease-1>', self.reset)
        
        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)
        red_btn = Button(self, text="Red", bg='red', width=10, command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)
        green_btn = Button(self, text="Green", bg='green', width=10, command=lambda: self.set_color("green"))
        green_btn.grid(row=0, column=2)
        blue_btn = Button(self, text="Blue", bg='blue', fg='white', width=10, command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)
        black_btn = Button(self, text="Black", bg='black', fg='white', width=10, command=lambda: self.set_color("black"))
        black_btn.grid(row=0, column=4)        
        white_btn = Button(self, text="Eraser", width=10, command=lambda: self.set_color("white"))
        white_btn.grid(row=0, column=6)
        color_button = Button(self, text='Color', width=10, command=lambda:self.choose_color())
        color_button.grid(row=0, column=5)
        
        size_lab = Label(self, text="Size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="2x", width=10, command=lambda: self.choose_size_button.set(2))
        one_btn.grid(row=1, column=1)
        two_btn = Button(self, text="5x", width=10, command=lambda: self.choose_size_button.set(5))
        two_btn.grid(row=1, column=2)        
        five_btn = Button(self, text="7x", width=10, command=lambda: self.choose_size_button.set(7))
        five_btn.grid(row=1, column=3)         
        seven_btn = Button(self, text="10x", width=10, command=lambda: self.choose_size_button.set(10))
        seven_btn.grid(row=1, column=4)
        ten_btn = Button(self, text="20x", width=10, command=lambda: self.choose_size_button.set(20))
        ten_btn.grid(row=1, column=5)
        twenty_btn = Button(self, text="50x", width=10, command=lambda: self.choose_size_button.set(50))
        twenty_btn.grid(row=1, column=6)

        self.choose_size_button = Scale(self, length=250, from_=1, to=100, orient=HORIZONTAL)
        self.choose_size_button.grid(row=1, column=7)
        
        clear_btn = Button(self, text="Clear", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=7, sticky=W)
        
        self.old_x = None
        self.old_y = None
        self.brush_size = 2
           
    def draw(self, event):
        paint_color = self.color
        self.brush_size = self.choose_size_button.get()
        if self.old_x and self.old_y:
            self.canv.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.brush_size, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    
    def set_color(self, new_color):
        self.color = new_color
        
    def reset(self, event):
        self.old_x, self.old_y = None, None        
        
    def choose_color(self):
        self.color = askcolor(color=self.color)[1]        
 

        
        
        
def main():
    root = Tk()
    root.geometry("800x600+200+200")
    app = Paint(root)
    root.mainloop()
        
if __name__ == "__main__":
    main()
    