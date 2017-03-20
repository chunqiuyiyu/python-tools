# coding=utf-8
from tkinter import *
from tkinter import ttk
import utils 

root = Tk()
root.title("newsreader")
root.withdraw()
root.iconbitmap('icon.ico')
# set the position of  window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() - 100    #under windows, taskbar may lie under t
root.resizable(FALSE,FALSE)

# add news list
frame = ttk.Frame(root, padding=(5, 5, 5, 5))
frame.grid(column=0, row=0, sticky=(N,W,E,S)) 

l = Listbox(frame, height=32, width=48)
l.grid(column=0, row=0, rowspan=2)
utils.setData(l)

queryBtn = ttk.Button(frame, text='浏览', command=utils.query)
queryBtn.grid(column=1, row=0, padx=10)

aboutBtn = ttk.Button(frame, text='关于', command=utils.about)
aboutBtn.grid(column=1, row=1, padx=10)

root.update_idletasks()
root.deiconify()    #now window size was calculated
root.withdraw()     #hide window again
root.geometry('%sx%s+%s+%s' % (root.winfo_width(), root.winfo_height(), (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2) )    #center window on desktop
root.deiconify()

if __name__ == '__main__':
	root.mainloop()