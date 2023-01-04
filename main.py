#导入一堆库
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import function
from tkinter import filedialog
import pyperclip
import tkinter.messagebox
import ctypes

#中英文系统
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

def savebutshow():
    s = ttk.Style()
    s.configure('my.TButton', font=("微软雅黑",10))
    if languageu == 1:
        button1 = ttk.Button(top1,text='保存结果',style='my.TButton',command=buttonclick)
    else:
        button1 = ttk.Button(top1,text='Save Results',style='my.TButton',command=buttonclick)
    
    button1.place(x=250, y=270)

#主页的函数操作

#获取windows系统语言，对MAC可能不怎么友好
global languageu
dll_h = ctypes.windll.kernel32
languagearea=hex(dll_h.GetSystemDefaultUILanguage())
if(languagearea=="0x804"):
    languageu=1
else:
    languageu=0

#关于界面显示
def callback1():
    if languageu == 1:
        tkinter.messagebox.showinfo(title='关于',message='v1.2\n由Codewyx制作')
    else:
        tkinter.messagebox.showinfo(title='About',message='v1.2\nMade By Codewyx')
    

#语言切换操作：先删除再增加
def callback4():
    global languageu
    print(languageu)
    if languageu == 1:
        print("2")
        languageu=0
        menubar.delete(2)
        menubar.delete(1)
        menubar.add_cascade(label="中文", command=callback4)
        menubar.add_cascade(label='About', command=callback1)
    else:
        languageu=1
        menubar.delete(2)
        menubar.delete(1)
        menubar.add_cascade(label="English", command=callback4)
        menubar.add_cascade(label='关于', command=callback1) 
    showbg()


#结果页的函数操作

#结果页面保存日志按钮被点击后保存文件的操作
def buttonclick():
    path_save = filedialog.asksaveasfilename(initialfile='information.log',filetypes=[("日志文件", ".log")]) 
    path_save = path_save.replace("/", "\\\\")
    f = open(path_save,'w',encoding='utf-8')
    f.write(myinfo) 
    f.close()

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




#检查文件结果的代码
def callback(event):
        #判断点击取消就返回
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
menubar = tkinter.Menu(root)
menubar.add_cascade(label="English", command=callback4)
menubar.add_cascade(label='关于', command=callback1)
root['menu'] = menubar
#显示Root页面
root.mainloop()


