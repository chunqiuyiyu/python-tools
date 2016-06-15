import Tkinter
import Image
from DnDwrapper import *

def main():
    root = Tkinter.Tk()
    root.wm_title('DealImg')
    dnd = DnD(root)
    Tkinter.Label(root, text='Drop image file into the listbox').pack(side='top')
    l = Tkinter.Listbox(root)
    l.pack(side='top', fill='both', expand=1)
    root.update()# may be necessary on unix
    # now make the listbox a drop target:
    
    def drag(action, actions, type, win, X, Y, x, y, data):
        return action
        
    def drag_enter(action, actions, type, win, X, Y, x, y, data):
        l.focus_force()
        return action
    
    def drop(action, actions, type, win, X, Y, x, y, data):
        #data:the file path
        path = data
        if data[0]=='{':
            path = data[1:-1]
        exten  = path[-3:]
        arr = path.split('/')
        print path
        im = Image.open(path)
        s = im.size
        newImg = Image.new("RGBA",(s[0],s[1]),(0,0,0,0))
        newImg.save(arr[-1],exten.upper())
        
    dnd.bindtarget(l, 'text/uri-list', '<Drag>', drag, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(l, 'text/uri-list', '<DragEnter>', drag_enter, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(l, 'text/uri-list', '<Drop>', drop, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y','%D'))
    
    root.mainloop()

if __name__ == '__main__':
    main()
