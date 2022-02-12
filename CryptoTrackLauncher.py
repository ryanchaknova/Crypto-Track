# from test import runCrypto
# import tkinter as tk
import sys, os, getopt

# class Application(tk.Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master=master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.crypto=tk.Button(self)
#         self.crypto["text"]="Run CryptoTrackV6"
#         self.crypto["command"]=self.runCrypto
#         self.crypto.pack(side="top")

#         self.quit=tk.Button(self, text="QUIT",fg="red",command=self.master.destroy)
#         self.quit.pack(side="bottom")

def runCrypto():
    os.system('g++ ' + "CryptoTrackV6.cpp -I/usr/include/python3.8 -lpython3.8")
    os.system("./a.out")


# root=tk.Tk()
# app=Application(master=root)
# app.mainloop()

runCrypto()

