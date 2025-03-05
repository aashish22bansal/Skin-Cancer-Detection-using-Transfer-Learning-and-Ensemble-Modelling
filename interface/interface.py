from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

base = Tk()
base.title('detection of skin cancer')
title_label = Label(base,text="click upload button and upload your X-ray")
title_label.grid(row=0,column = 0,columnspan=3) 
def func():
    global img
    base.filename = filedialog.askopenfilename(initialdir="/",title="select",filetypes=[('image files', '.png'),('image files', '.jpg'),('image files', '.jpeg')])
    print(base.filename)
    x=Image.open(base.filename)
    resize = x.resize((400,400),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize)
    image_print = Label(image=img)
    image_print.grid(row=6,column = 0,columnspan=3) 

butt = Button(base,text="upload image",command=func)
butt.grid(row=2,column = 0,columnspan=3) 
base.minsize(200,200)
base.mainloop()