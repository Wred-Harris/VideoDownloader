import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import yt_dlp


def DownloadVideo():
    url = entry.get()
    if not savedir:
        messagebox.showerror("Error", "Select download folder")
        return
    ydl_opts = {
        'outtmpl': f'{savedir}/%(title)s.%(ext)s',
        'format': 'best'
        'skip_unavailable_fragments: False'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Downloaded successfully to {savedir}")
        root.withdraw()

    
    except Exception as e:
        messagebox.showerror(e)


savedir = r"C:\Users\wredt\OneDrive\Videos\Videos"

def openFileDialog():
    global savedir
    folder = filedialog.askdirectory()
    if folder:
        savedir = folder
        browseBtn.config(text=savedir)
 
#UI Init
root = tk.Tk()
center = tk.Frame(root)
root.state('zoomed')
root.configure(bg='blue')
center.place(relx=0.5, rely=0.5, anchor="n")


root.title("Media Downloader")
entrylable = Label(center, text="Enter a URL: ", font="helvetica")
entrylable.place(relx=0.5, rely=0.5, anchor='center')


entry = Entry(center, width=70)
entry.place(relx=0.5, rely=0.5, anchor='center')

browseBtn = tk.Button(center, text="Browse Folder", command=openFileDialog)

downloadBtn = Button(center, text="Download Media", font='helvetica', command=DownloadVideo)
downloadBtn.place(relx=0.5, rely=0.5, anchor='center')


entrylable.grid(row=0, column=0, pady=8)
entry.grid(row=1, column=0, pady=8)
browseBtn.grid(row=2, column=0, pady=8)
downloadBtn.grid(row=3, column=0, pady=8)


root.grid_columnconfigure(0, weight=1)


root.mainloop()
