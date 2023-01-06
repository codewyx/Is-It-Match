#导入一堆库
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import function
from tkinter import filedialog
import pyperclip
import tkinter.messagebox
import ctypes
import webbrowser


#欢迎运行和开发本项目，本项目遵循MIT协议！ Welcome to run and develop this project, which follows MIT LICENSE!
print("开发本项目，本项目遵循MIT协议！\nWelcome to run and develop this project, which follows MIT LICENSE!\n————————————————————————————————————————————————————————————————————————")
global version
version="v1.3"


#页面的显示（中文&English）

#首页背景图片
def showbg():
    if languageu == 1:
        photo = Image.open("resource/index.png")
    else:
        photo = Image.open("resource/index_en.png")
    photo = photo.resize((600, 360))
    global img0
    img0 = ImageTk.PhotoImage(photo)
    label = ttk.Label(root, image=img0)
    label.bind("<Button-1>", callback)
    label.place(x=0,y=0)

#结果页面背景图片
def showbg2():
    if languageu == 1:
        photo1 = Image.open("resource/top.png")
    else:
        photo1 = Image.open("resource/top_en.png")
    photo1 = photo1.resize((600, 360))
    global img1
    img1 = ImageTk.PhotoImage(photo1)
    label1 = ttk.Label(top1, image=img1)
    label1.place(x=0,y=0)     

#结果页面按钮布局
def savebutshow():
    s = ttk.Style()
    s.configure('my.TButton', font=("微软雅黑",10))
    if languageu == 1:
        button1 = ttk.Button(top1,text='保存结果',style='my.TButton',command=buttonclick)
        button2 = ttk.Button(top1,text='输入Hash验证',style='my.TButton',command=buttonclick2)
    else:
        button1 = ttk.Button(top1,text='Save Results',style='my.TButton',command=buttonclick)
        button2 = ttk.Button(top1,text='Enter Hash to verify',style='my.TButton',command=buttonclick2)
    
    button1.place(x=190, y=270)
    button2.place(x=310, y=270)

#结果-验证页面按钮布局
def subshow():
    s = ttk.Style()
    s.configure('my.TButton', font=("微软雅黑",10))
    if languageu == 1:
        button3 = ttk.Button(top2,text='提交',style='my.TButton',command=buttonclick3)
    else:
        button3 = ttk.Button(top2,text='Submit',style='my.TButton',command=buttonclick3)
    
    button3.place(x=400, y=8)


#获取windows系统语言，对MAC可能不怎么友好
global languageu
dll_h = ctypes.windll.kernel32
languagearea=hex(dll_h.GetSystemDefaultUILanguage())
if(languagearea=="0x804"):
    languageu=1
else:
    languageu=0

#关于界面显示
def callback1(self="M"):
    if languageu == 1:
        tkinter.messagebox.showinfo(title='关于',message=version+'\n由Codewyx制作')
    else:
        tkinter.messagebox.showinfo(title='About',message=version+'\nMade By Codewyx')
    

#语言切换操作
def callback4():
    global languageu
    languageu=1
    showbg()
    topdan()

def callback42():
    global languageu
    languageu=0
    showbg()
    topdan()

def topdan():
    if languageu==1: 
        root.config(menu="") 
        menubar = tkinter.Menu(root)
        root['menu'] = menubar
        filemenu = tkinter.Menu (menubar, tearoff=False)
        filemenu.add_command (label="关于",command=callback1)
        filemenu.add_separator() 
        filemenu.add_command (label="下载",command=callback11)
        filemenu.add_command (label="Github",command=callback12)
        menubar.add_cascade(label='帮助', menu=filemenu)
        
        filemenu1 = tkinter.Menu (menubar, tearoff=False)
        filemenu1.add_command (label="中文",command=callback4)
        filemenu1.add_command (label="English",command=callback42)
        menubar.add_cascade(label="语言/Language", menu=filemenu1,compound='left')
    else:
        root.config(menu="") 
        menubar = tkinter.Menu(root)
        root['menu'] = menubar      
        filemenu = tkinter.Menu (menubar, tearoff=False)
        filemenu.add_command (label="About",command=callback1)
        filemenu.add_separator() 
        filemenu.add_command (label="Download",command=callback11)
        filemenu.add_command (label="Github",command=callback12)
        menubar.add_cascade(label='Help', menu=filemenu)
        
        filemenu1 = tkinter.Menu (menubar, tearoff=False)
        filemenu1.add_command (label="中文",command=callback4)
        filemenu1.add_command (label="English",command=callback42)
        menubar.add_cascade(label="Language/语言", menu=filemenu1,compound='left')
    


#菜单：查询最新版
def callback11():
    webbrowser.open("https://github.com/codewyx/Is-It-Match/releases/latest", new=0, autoraise=True)

#菜单：仓库
def callback12():
    webbrowser.open("https://github.com/codewyx/Is-It-Match", new=0, autoraise=True)


#----------------------------------------------------------------------------------------------



#结果页的函数操作

#结果页面保存日志按钮被点击后保存文件的操作
def buttonclick():
    path_save = filedialog.asksaveasfilename(initialfile='information.log',filetypes=[("日志文件", ".log")]) 
    path_save = path_save.replace("/", "\\\\")
    f = open(path_save,'w',encoding='utf-8')
    f.write(myinfo) 
    f.close()

#结果页面点击验证逻辑
def buttonclick2():
    global top2
    top2=tkinter.Toplevel(top1) 
    top2.title('Is It Match?') 
    top2.iconbitmap('resource/logo.ico')
    top2.attributes('-alpha', 0.95)
    top2.resizable(0,0) 
    top2["background"] = "#F0F4F4"
    top2.geometry('520x50') 
    global v
    v = tkinter.StringVar()
    ttk.Entry(top2,width=50,textvariable=v).place(x=37, y=10)
    subshow()

#提交验证逻辑
def buttonclick3():
    #隐藏窗口
    top2.destroy()
    #获取输入内容
    entryget=v.get()
    #按照语言和算法开始遍历
    if languageu == 1:
        if entryget == file_md5:
            tkinter.messagebox.showinfo(title='信息',message='验证正确')
        elif entryget == file_sha1:
            tkinter.messagebox.showinfo(title='信息',message='验证正确')    
        elif entryget == file_sha256:
            tkinter.messagebox.showinfo(title='信息',message='验证正确')    
        elif entryget == file_sha512:
            tkinter.messagebox.showinfo(title='信息',message='验证正确')    
        else:
            tkinter.messagebox.showerror(title='信息',message='验证错误')    
    else:
        if entryget == file_md5:
            tkinter.messagebox.showinfo(title='Message',message='File Hash verification is correct')
        elif entryget == file_sha1:
            tkinter.messagebox.showinfo(title='Message',message='File Hash verification is correct')    
        elif entryget == file_sha256:
            tkinter.messagebox.showinfo(title='Message',message='File Hash verification is correct')    
        elif entryget == file_sha512:
            tkinter.messagebox.showinfo(title='Message',message='File Hash verification is correct')   
        else:
            tkinter.messagebox.showerror(title='Message',message='File Hash verification is wrong')    
    
#结果页面关闭的操作
def Overtk():
    root.deiconify() 
    top1.destroy()

#结果页面右键菜单
def popup(event):
    menu = tkinter.Menu(root,tearoff=False)
    if languageu == 1:
        menu.add_command(label="复制全部", command=callback2)
        menu.add_command(label="复制选中", command=callback3)
    else:
        menu.add_command(label="Copy All", command=callback2)
        menu.add_command(label="Copy Selected", command=callback3)
    menu.post(event.x_root, event.y_root)  

#结果页面右键菜单复制所有内容
def callback2(event=None):
    pyperclip.copy(myinfo)

#结果页面右键菜单复制选中内容
def callback3(event=None):
    selectableMsg.event_generate('<<Copy>>')

#检查页面初始化
def callback(event):
        #判断点击取消就返回
        global f_path
        f_path = filedialog.askopenfilename()
        if function.ifright(f_path)=="error":
            return
        #弹出提示给予用户信心、告诉用户需要等待，以免用户误认为软件崩溃
        if languageu == 1:
            tkinter.messagebox.showinfo(title='提示',message='正在获取中，请稍后！')
        else:
            tkinter.messagebox.showinfo(title='Tips',message='Getting results, please wait!')
        #掐掉Root页面
        root.withdraw()
        #显示并定义Top1界面
        global top1
        top1=tkinter.Toplevel(root) 
        #掐掉Top1，等一下再显示，以免界面一闪一闪的用户觉得奇怪……
        top1.iconify()
        top1.title('Is It Match?') 
        top1.iconbitmap('resource/logo.ico')
        top1.attributes('-alpha', 0.95)
        top1.resizable(0,0) 
        top1["background"] = "#F0F4F4"
        top1.geometry('600x360') 
        top1.protocol("WM_DELETE_WINDOW", Overtk)
        #显示背景图片
        showbg2() 
        #通过Function的函数计算Hash值并且显示
        global file_md5
        global file_sha1
        global file_sha256
        global file_sha512
        file_md5=function.file_md5(f_path)
        file_sha1=function.file_sha1(f_path)
        file_sha256=function.file_sha256(f_path)
        file_sha512=function.file_sha512(f_path)
        global selectableMsg   
        selectableMsg = tkinter.Text(top1,background="#F0F4F4",width=58, height=8,font=("微软雅黑", 11))
        global myinfo  
        myinfo = "File："+f_path+"\nMD5："+file_md5+"\nSHA1："+file_sha1+"\nSHA256："+file_sha256+"\nSHA512："+file_sha512
        selectableMsg.insert(1.0,myinfo)
        selectableMsg.configure(state='disabled')
        selectableMsg.place(x=30, y=100)
        selectableMsg.bind("<Button-3>", popup)   
        #显示保存按钮
        savebutshow()
        #显示Top1界面
        top1.deiconify()

#定义Root页面
global root
root = tkinter.Tk()
root.title('Is It Match?')
root.geometry('600x360')
root.iconbitmap('resource/logo.ico')
root.attributes('-alpha', 0.95)
root.resizable(0,0) 
root["background"] = "#F0F4F4"
#显示背景图片
showbg()
#设置顶部菜单
topdan()
#显示Root页面
root.mainloop()