## 说明
一款用来阅读游戏资讯的小软件。新闻资讯类的网站大家都懂得，各种广告内容让人忍无可忍。但是，网站中的资讯内容确实是我所希望阅读的，为此，我在空余时间开发了这款小软件，用来滤除无用的网页信息，只展示出自己感兴趣的资讯标题，在认为确实要详细了解内容时，跳转到网站阅读资讯。

## 技术
软件本质是一个网络爬虫，使用python是顺理成章的事情，用到了十分流行的requests与BeautifulSoup两个模块。requests负责网络请求，相较于以前使用的urllib等模块。这个模块的API更加人性化，更加易于使用。它的口号是：
> Requests 是唯一的一个非转基因的 Python HTTP 库，人类可以安全享用。

我想它做到了这一点。要注意的是抓取下来网页内容后，需设置正确的编码，这样网页的内容才能正确显示。
```python
r = requests.get('http://www.example.com/')
r.encoding = 'gbk'
```
BeautifulSoup用来对抓取下来的网页内容进行解析，它提供十分直观易用的API，让你能够从文档树中快速正确地获取你想要的内容。BeautifulSoup需要和html文档解析器一起搭配使用，这里我用到的是lxml。
接下来就是软件界面了。依旧使用经典的tkinter，tkinter在较新的版本中引入了ttk，在ttk中提供了更加美观和符合系统特色的控件，建议在能使用ttk控件时使用它，本程序中用到的是它的框架（Frame）和按钮（Button）控件。编写界面时，有一部分代码是通用的，用来使软件窗口居于屏幕中心位置。tkinter本身并没有提供类似居中的API方法，原因很简单：窗口的大小不是固定的，窗口相当于一个盒子，它的大小是用里面的控件撑起来的。因此，首先生成窗口控件，然后将其隐藏，最后等所有的控件添加到窗口上时，再通过计算将窗口显示到屏幕的中心。我用的系统是windows，需要在竖直方向上减去任务栏高度的像素。
```python
root = Tk()
root.title("example")
root.withdraw()
root.iconbitmap('icon.ico')
# set the position of  window
screen_width = root.winfo_screenwidth()
# under windows, taskbar need some space
screen_height = root.winfo_screenheight() - 100   
root.resizable(FALSE,FALSE)

# add some widgets
...
# end

root.update_idletasks()
# now window size was calculated
root.deiconify()    
root.withdraw()  
# hide window again  
root.geometry('%sx%s+%s+%s' % (root.winfo_width(), root.winfo_height(), (screen_width - root.winfo_width())/2, (screen_height - root.winfo_height())/2) )    
# center window on desktop
root.deiconify()
```
最后用pyinstaller打包指定的脚本，用一条命令搞定：
```shell
pyinstaller exampe.py -i icon.ico -w
```
`-i`选项指定打包后的exe文件图标，`-w`表示以窗口形式运行脚本，在运行exe时就不会显示控制台了。
## 效果
![newsreader.png][1]
## 后记
从桌面应用开发的角度来说，使用C/C++/C#开发的应用运行效率肯定要超过python，但是这几种语言的学习成本确实比较高。当你在工作或者生活中用python开发了几款顺手的工具想分发给别人使用时，tkinter和pyinstaller就是不错的选择。 


  [1]: http://www.chunqiuyiyu.com/usr/uploads/2017/03/3474326995.png
