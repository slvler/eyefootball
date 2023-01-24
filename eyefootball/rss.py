import feedparser
from tkinter import *
import webview
from eyefootball.command import *

cmd = command("https://www.eyefootball.com/")

def close():
   window.destroy()

def open_url(event):
    webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
    webview.start()


def clear_frame():
    for widget in mainFrame.winfo_children():
        widget.destroy()

def clear_btn():
    btn_football_full.configure(bg='#54FA9B')
    btn_football.configure(bg='#54FA9B')
    btn_football_transfer.configure(bg='#54FA9B')
    btn_football_blogs.configure(bg='#54FA9B')
    btn_football_blogs.configure(bg='#54FA9B')

def add_comment(values):
    for key in values.entries:
        Label(mainFrame, text=key.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill='x')
        lbl_link = Label(mainFrame, text=key.link, anchor='w', font=('Helveticabold', 14), fg='blue', cursor="hand2")
        lbl_link.pack(side=TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(mainFrame, text="-", anchor="center", fg='pink').pack(side=TOP, fill='x')

def football_full_command():
    clear_frame()
    clear_btn()
    add_comment(cmd.football_full_command())

def football_command():
    clear_frame()
    clear_btn()
    add_comment(cmd.football_command())

def football_transfer_command():
    clear_frame()
    clear_btn()
    add_comment(cmd.football_transfer_command())

def football_blogs_command():
    clear_frame()
    clear_btn()
    add_comment(cmd.football_blogs_command())

def mobile_site_command():
    clear_frame()
    clear_btn()
    add_comment(cmd.mobile_site_command())


window = Tk()
window.title('RSS feeds at eyefootball.com')
window.geometry("1000x600")

mainFrame = Frame(window, height=600)
buttonFrame = Frame(window, relief=RAISED, bg="gray", bd=2)

btn_football_full = Button(buttonFrame, text="Full covarage", font=('Arial Bold', 14), bg='#54FA9B', command=football_full_command)
btn_football = Button(buttonFrame, text="Football News", font=('Arial Bold', 14), bg='#54FA9B', command=football_command)
btn_football_transfer = Button(buttonFrame, text="Transfer", font=('Arial Bold', 14), bg='#54FA9B', command=football_transfer_command)
btn_football_blogs = Button(buttonFrame, text="BLogs", font=('Arial Bold', 14), bg='#54FA9B', command=football_blogs_command)
btn_mobile_site = Button(buttonFrame, text="Mobile", font=('Arial Bold', 14), bg='#54FA9B', command=mobile_site_command)
btn_close = Button(buttonFrame, text="Close", font=('Arial Bold', 14), bg='red', command=close)

btn_football_full.grid(row=0, column=0, sticky="new", padx=5, pady=5)
btn_football.grid(row=1, column=0, sticky="new", padx=5, pady=5)
btn_football_transfer.grid(row=3, column=0, sticky="new", padx=5, pady=5)
btn_football_blogs.grid(row=4, column=0, sticky="new", padx=5, pady=5)
btn_mobile_site.grid(row=5, column=0, sticky="new", padx=5, pady=5)
btn_close.grid(row=6, column=0, sticky="new", padx=5, pady=5)


buttonFrame.grid(row=0, column=0, sticky="ns")
mainFrame.grid(row=0, column=1, sticky="nsew")


window.mainloop()