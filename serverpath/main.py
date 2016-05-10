#coding=utf-8
import Tkinter
import ttk
import webbrowser
import re
# import threading
# import tkFileDialog

class ToolGUI():
    def __init__(self):
	self.root=root= ttk.Tkinter.Tk()
	#set window title,size and icon
	root.wm_title('xampp folder')

	root.withdraw()    #hide window
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight() - 100    #under windows, taskbar may lie under the screen
	root.resizable(False,False)
	root.iconbitmap('icon.ico')
	#add some widgets to the root window...

	ttk.Label(root, text=u'请悉知', foreground='brown').grid(row=0, sticky='E', padx=5, pady=10)
	ttk.Label(root, text=u'这是一个简单的工具，你可以用它来修改xampp默认的\n服务器目录，如有建议问题，欢迎点击关于按钮反馈:-)',foreground='brown', 
		justify='left').grid(row=0, column=1, sticky='W', pady=10)

	# ttk.Label(root, text=u'xampp安装路径（不要有中文）：').grid(row=1, column=1, sticky='W', padx=5, pady=0)	

	# self.select_btn = ttk.Button(root, text=u'选择')
	# self.select_btn.bind('<Button-1>', self.selectXampp)
	# self.select_btn.grid(row=1,column=1,pady=10, sticky='E', padx=30)

	ttk.Label(root, text=u'选择服务器目录：').grid(row=1, column=1, sticky='W', padx=5, pady=0)
	filname = 'path.ini'
	mylist = []
	with open(filname) as f:
		for x in f:
		    mylist.append(x)
	self.dirname = mylist[0].replace('\n','')
	self.countrynames = tuple(mylist[1:])
	self.cnames = Tkinter.StringVar(value=self.countrynames)
	self.listHeight = len(self.countrynames)
	self.listbox = ttk.Tkinter.Listbox(root, listvariable=self.cnames, height=self.listHeight, activestyle='none')
	self.listbox.grid(row=1,column=1,pady=10, sticky='E', padx=30)
	self.listbox.bind("<<ListboxSelect>>", self.PrintSelected)

	self.tips=ttk.Tkinter.Label(root, text=u"提示：服务器目录可以在path.ini文件中设置")
	self.tips.grid(row=2, column=1, sticky='W')	

	self.down_btn = ttk.Button(root, text=u'修改')
	self.down_btn.bind('<Button-1>', self.modify)
	self.down_btn.grid(row=3,column=1,pady=10, sticky='W')

	self.about_btn = ttk.Button(root, text=u'关于')
	self.about_btn.bind('<Button-1>', self.about_me)
	self.about_btn.grid(row=3,column=1,pady=10, sticky='E', padx=30)

	self.browser = webbrowser.get()


	root.update_idletasks()
	root.deiconify()    #now window size was calculated
	root.withdraw()     #hide window again
	root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10, (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2) )    #center window on desktop
	root.deiconify()

	root.mainloop()

    def PrintSelected(self, e):
        self.currentPath = self.countrynames[int(self.listbox.curselection()[0])];
        print self.currentPath

    def selectXampp(self, event):
    	self.dirname = tkFileDialog.askdirectory()
	print self.dirname

    def modify(self, e):
        filname = self.dirname +'apache/conf/httpd.conf'
        with open(filname, 'r+') as f:
	        d = f.read()
	        new = 'DocumentRoot "'+self.currentPath+'"\n'+'<Directory "'+self.currentPath+'">'
	        x = re.sub(r'DocumentRoot\s.*\n<.*>',new, d)
	        x = re.sub(r'\n"','"',x)
	        f.seek(0)
	        f.write(x)
	        f.close()	    

    def about_me(self, event):
        self.browser.open('https://github.com/chunqiuyiyu')


if __name__ == '__main__':
	app = ToolGUI()