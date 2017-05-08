# coding=utf-8
from DnD import DnD
from PIL import Image, ImageTk
import subprocess

def app():
    import Tkinter
    from tkinter import ttk
    root = Tkinter.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 200
    root_width = (screen_width - 240) / 2
    root_height = (screen_height - 180) /2

    root.geometry('240x180+%s+%s' % (root_width, root_height))
    root.resizable(False,False)

    def apply(event, py, ico):
        command = 'pyinstaller ' + py + ' -i ' + ico
        subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    tip_label = ttk.Label(root, text="将文件拖入下方对应区域中")
    tip_label.grid(column=0, row=0, pady=10, columnspan=3)

    py_label = ttk.Label(root, text='PYTHON', background='white', relief='solid', width=10, anchor='center')
    py_label.grid(column=0, row=1, padx=20, pady=0, ipady=25)

    add_label = ttk.Label(root, text="+")
    add_label.grid(column=1, row=1, padx=0, pady=0, ipady=25)

    icon_label = ttk.Label(root, text='ICON', background='white', relief='solid', width=10, anchor='center')
    icon_label.grid(column=2, row=1, padx=20, pady=0, ipady=25)

    apply_btn = ttk.Button(root, text="生成")
    apply_btn.grid(column=0, row=2, columnspan=3, pady=20)

    root.update()# may be necessary on unix
    # now make the listbox a drop target:
    
    def drag(action, actions, type, win, X, Y, x, y, data):
        return action
        
    def drag_enter(action, actions, type, win, X, Y, x, y, data):
        return action
    
    def drop(action, actions, type, win, X, Y, x, y, data):
        if data[-2:] == 'py':
            global py
            py = data
            img = Image.open('res/python.ico')
            setBgColor(img)
            photo = ImageTk.PhotoImage(img)
            py_label.configure(image = photo)
            py_label.image = photo
            py_label.grid(ipady=2, ipadx=2)
        if data[-3:] == 'ico':
            apply_btn.bind("<Button-1>", lambda event, py=py, ico=data: apply(event, py, ico))
            img = Image.open(data).convert('RGBA')
            setBgColor(img)
            photo = ImageTk.PhotoImage(img)
            icon_label.configure(image = photo)
            icon_label.image = photo
            icon_label.grid(ipady=2, ipadx=2)
        root.update()

    def setBgColor(img):
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)

    # bind drop event
    dnd = DnD(root)
    dnd.bindtarget(py_label, 'text/uri-list', '<Drag>', drag, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(py_label, 'text/uri-list', '<DragEnter>', drag_enter, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(py_label, 'text/uri-list', '<Drop>', drop, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y','%D'))

    dnd.bindtarget(icon_label, 'text/uri-list', '<Drag>', drag, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(icon_label, 'text/uri-list', '<DragEnter>', drag_enter, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(icon_label, 'text/uri-list', '<Drop>', drop, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y','%D'))

    root.mainloop()

if __name__ == '__main__':
    app()