from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('1200x1000')
c=Canvas(root,bg="gray16",height=400,width=400)
filename=PhotoImage(file="C:\\Users\\prach\\Pictures\\Screenshots\\Screenshot (240).png")
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()
root.resizable(0,0)
root.title("YOU TUBE VIDEO DOWNLOADER")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()