from parse import getInfo
import keyboard,  tkinter

holidays = getInfo()

def set_geometry(root):
    root.resizable(False, False)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2.8 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3.5 - windowHeight/2)
    root.geometry('+{}+{}'.format(positionRight, positionDown))

def set_app():
    root = tkinter.Tk()
    root.title('Holidays')
    set_geometry(root)
    root.configure(bg='#ffcccc')
    TextFrame = tkinter.Frame(master=root, relief=tkinter.FLAT,
                          borderwidth=50, bg='#ffccff')
    message = tkinter.Label(master=TextFrame, bg='#ffccff',
                             text=holidays, font=('Calibri', 18))
    message.pack()
    TextFrame.pack(fill=tkinter.BOTH, side=tkinter.TOP)
    root.mainloop()

keyboard.add_hotkey('Ctrl+1', lambda: set_app())
keyboard.wait('esc')

