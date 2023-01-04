import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from ttkbootstrap import Style
import function
from tkinter import filedialog
import pyperclip
import tkinter.messagebox



def losev():
    root.deiconify()
    top1.destroy()


def callback1():
    tkinter.messagebox.showinfo(title='关于',message='V.1.0 MADE BY CODEWYX')

def callback2(event=None):
    pyperclip.copy(myinfo)

def callback3(event=None):
    selectableMsg.event_generate('<<Copy>>')

def popup(event):
    menu = tkinter.Menu(root,tearoff=False)
    menu.add_command(label="复制全部", command=callback2)
    menu.add_command(label="复制选中", command=callback3)
    menu.post(event.x_root, event.y_root)  

def Overtk():
    root.deiconify() 
    top1.destroy()


def callback(event):
        f_path = filedialog.askopenfilename()
        global top1
        top1=tkinter.Toplevel(root) 
        top1.title('Is It Match? 检查结果') 
        top1.iconbitmap('resource/logo.ico')
        top1.attributes('-alpha', 0.95)
        top1.resizable(0,0) 
        top1["background"] = "#F0F4F4"
        top1.geometry('600x360') 
        top1.protocol("WM_DELETE_WINDOW", Overtk)
        global img1
        photo1 = Image.open("resource/top.png")
        photo1 = photo1.resize((600, 360))
        img1 = ImageTk.PhotoImage(photo1)
        label1 = ttk.Label(top1, image=img1)
        label1.pack()        
        root.withdraw()
        top1.deiconify()
        file_md5=function.file_md5(f_path)
        file_sha1=function.file_sha1(f_path)
        file_sha256=function.file_sha256(f_path)
        file_sha512=function.file_sha512(f_path)
        global selectableMsg   
        global myinfo  
        selectableMsg = tkinter.Text(top1,background="#F0F4F4",width=48, height=6,font=("微软雅黑", 14))
        myinfo = "MD5:"+file_md5+"\nSHA1:"+file_sha1+"\nSHA256:"+file_sha256   
        selectableMsg.insert(1.0,myinfo)
        selectableMsg.configure(state='disabled')
        selectableMsg.place(x=30, y=100)
        selectableMsg.bind("<Button-3>", popup)   
root = tkinter.Tk()
root.title('Is It Match? 主页')
root.geometry('600x360')
root.iconbitmap('resource/logo.ico')
root.attributes('-alpha', 0.95)
root.resizable(0,0) 
root["background"] = "#F0F4F4"
global img0
photo = Image.open("resource/index.png")
photo = photo.resize((600, 360))
img0 = ImageTk.PhotoImage(photo)
label = ttk.Label(root, image=img0)
label.bind("<Button-1>", callback)
label.pack()
style = Style(theme='default')
menubar = tkinter.Menu(root)
menubar.add_cascade(label='关于', command=callback1)
root['menu'] = menubar
root.mainloop()


