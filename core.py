import tkinter as tk
import random
import extractor as ext
from PIL import Image, ImageTk

INTRO_MSG = ("Verdana", 12)

author, quote = ext.tex_extract('Tags')
imgname = ext.img_extract()

def imgrand():
    irand = random.randint(0, len(imgname)-1)
    return imgname[irand]
def qtaggen():
    qrand = random.randint(1, len(quote))
    return quote[qrand] + " - " + author[qrand] 


class ImgTagGen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #make the stage for this application
        stage = tk.Frame(self)
        stage.pack(side="top", fill="both", expand=True)
        stage.rowconfigure(0, weight=1)
        stage.columnconfigure(0, weight=1)
        #make the storage for the different scenes
        self.scenes = {}
        #scenes
        scene = StartScene(stage, self)
        self.scenes[StartScene] = scene
        scene.grid(row=0, column=0, sticky="nsew")
        self.scenes[ImgTag]=None

        self.show_scene(StartScene)

    def show_scene(self, stage):
        scene = self.scenes[stage]
        scene.tkraise()
    
    def genNew(self, stage):
        #generates a new image, tag pair and then displays it
        self.scenes[ImgTag] = None
        scene = ImgTag(stage, self)
        self.scenes[ImgTag] = scene
        scene.grid(row=0, column=0, sticky="nsew")
        
class StartScene(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        intro_msg = tk.Label(self, text="Image Tag Generator", font=INTRO_MSG)
        intro_msg.pack(pady=10, padx=10)

        button = tk.Button(self, text="Generate Image+Tag", command=lambda: controller.genNew(parent))
        button.pack(side="bottom")

class ImgTag(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #load random image and display
        load = Image.open(imgrand()).resize((500, 500), Image.ANTIALIAS)
        rend = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=rend)
        img.image = rend
        img.pack(pady=10, padx=10)
        #random tag to pair with img
        img_tag = tk.Label(self, text=qtaggen(), font=INTRO_MSG)
        img_tag.pack(pady=10, padx=10)
        button = tk.Button(self, text="Generate Image+Tag", command=lambda: controller.genNew(parent))
        button.pack(side="bottom")
        

#start performance
perform=ImgTagGen()
perform.title("Photo + Tag")
perform.mainloop()