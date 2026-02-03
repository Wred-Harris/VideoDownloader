import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import yt_dlp
import sys

def DownloadVideo():
    url = entry.get()
    if not savedir:
        messagebox.showerror("Error", "Select download folder")
        return
    ydl_opts = {
        'outtmpl': f'{savedir}/%(title)s.%(ext)s',
        'format': 'bv*+ba/b',
        'merge_output_format': 'mp4',
        'skip_unavailable_fragments': True,
        'extractor_args': {'youtube': {'player_client': ['windows']}},
        'quiet': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Starting download...")
        print("Success", f"Downloaded successfully to {savedir}")

    
    except Exception as e:
        messagebox.showerror(e)


def openFileDialog():
    global savedir
    folder = filedialog.askdirectory()
    if folder:
        savedir = folder
        browseBtn.config(text=savedir)

class ConsoleRedirect:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.configure(state="normal")
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)
        self.widget.configure(state="disabled")

    def flush(self):
        pass

#UI Init
root = tk.Tk()
center = tk.Frame(root)
root.state('zoomed')
center.place(relx=0.5, rely=0.5, anchor="n")

root.title("Media Downloader")
entrylable = Label(center, text="Enter a URL: ", font="helvetica")
entrylable.place(relx=0.5, rely=0.5, anchor='center')


entry = Entry(center, width=70)
entry.place(relx=0.5, rely=0.5, anchor='center')

browseBtn = tk.Button(center, text="Browse Folder", command=openFileDialog)

downloadBtn = Button(center, text="Download Media", font='helvetica', command=DownloadVideo)
downloadBtn.place(relx=0.5, rely=0.5, anchor='center')


console = Text(root, height=10, width=60, state="disabled")
console.pack(side=tk.TOP)
sys.stdout = ConsoleRedirect(console)
sys.stderr = ConsoleRedirect(console)

entrylable.grid(row=0, column=0, pady=8)
entry.grid(row=1, column=0, pady=8)
browseBtn.grid(row=2, column=0, pady=8)
downloadBtn.grid(row=3, column=0, pady=8)



root.grid_columnconfigure(0, weight=1)

root.mainloop()
