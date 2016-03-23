#coding=utf-8
import Tkinter
import ttk
import win32ui
import webbrowser
import downfaster
import threading

class ToolGUI():
    def __init__(self):
	self.root=root= ttk.Tkinter.Tk()
	#set window title,size and icon
	root.wm_title('downfaster 2.0')

	root.withdraw()    #hide window
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight() - 100    #under windows, taskbar may lie under the screen
	root.resizable(False,False)
	root.iconbitmap('icon.ico')
	#add some widgets to the root window...
	#game name entry

	ttk.Label(root, text=u'请悉知', foreground='brown').grid(row=0, sticky='E', padx=5, pady=10)
	ttk.Label(root, text=u'这是一个简单的下载工具，你可以用它来快速下载html5\n小游戏中的资源，如有建议问题，欢迎点击关于按钮反馈:-)',foreground='brown', 
		justify='left').grid(row=0, column=1, sticky='W', pady=10)
	ttk.Label(root, text=u'请输入小游戏名称：').grid(row=1, column=1, sticky='W', padx=5, pady=0)
	self.entry=ttk.Entry(root)
	self.entry.grid(row=1, column=1, sticky='E', padx=30)

	ttk.Label(root, text=u'选择har文件路径（不要有中文）：').grid(row=2, column=1, sticky='W', padx=5, pady=0)	

	self.select_btn = ttk.Button(root, text=u'选择')
	self.select_btn.bind('<Button-1>', self.select_har)
	self.select_btn.grid(row=2,column=1,pady=10, sticky='E', padx=30)

	self.tips=ttk.Tkinter.Label(root, text=u"提示：har文件可以从Chrome中下载得到")
	self.tips.grid(row=3, column=1, sticky='W')	

	self.down_btn = ttk.Button(root, text=u'下载')
	self.down_btn.bind('<Button-1>', self.down_res)
	self.down_btn.grid(row=4,column=1,pady=10, sticky='W')

	self.about_btn = ttk.Button(root, text=u'关于')
	self.about_btn.bind('<Button-1>', self.about_me)
	self.about_btn.grid(row=4,column=1,pady=10, sticky='E', padx=30)

	root.update_idletasks()
	root.deiconify()    #now window size was calculated
	root.withdraw()     #hide window again
	root.geometry('%sx%s+%s+%s' % (root.winfo_width() + 10, root.winfo_height() + 10, (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2) )    #center window on desktop
	root.deiconify()

	root.bind("<<TIPS>>",lambda evt:self.update_tips(downfaster.q.get()))
	root.mainloop()

    def down_res(self, event):

    	downfaster.game_name=self.entry.get()
    	print downfaster.game_name
    	urls=downfaster.mak_dirs(self.filename)
    	self.create_down(urls,self.root)
    	self.create_html(self.filename)

    def select_har(self, event):
    	# 1 for open file dialog
    	self.dlg = win32ui.CreateFileDialog(1) 
    	 # set the initialdir when the dialog is open
	self.dlg.SetOFNInitialDir(r'C:\Users\win 7\Downloads')
	self.dlg.DoModal()
	 # get selected file path name
	self.filename = self.dlg.GetPathName()
	print self.filename
	self.tmp="当前路径："+ self.filename
	#self.update_tips(self.tmp)

    def about_me(self, event):
        browser = webbrowser.get()
        browser.open('https://github.com/chunqiuyiyu')

    def update_tips(self,str):
        self.tips['text'] = str
        self.tips.update()
    def create_down(self,urls,root):
        threading.Thread(target=downfaster.down_game, args=(urls,root)).start()
    def create_html(self,filename):
        threading.Thread(target=downfaster.down_html, args=(filename,)).start()

app = ToolGUI()