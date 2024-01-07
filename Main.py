import tkinter
from tkinter import ttk, W
from zipfile import ZipFile
import os

import GuiUtils
import PackUtils
import OSUtils
from EnvVars import *
import tkinter as tk
from PIL import Image, ImageTk

from Pack import Pack

# Checks the default textures exists
GuiUtils.sectionPrint("Checking Default Textures")
if not os.path.exists(TEXTURES_PATH + DEFAULT_TEXTURES):
    raise Exception("Default textures folder is INVALID")

# Gets all the zip files from within TEXTURES_FOLDER
GuiUtils.sectionPrint("Getting Packs")
texture_zips = OSUtils.getFiles(TEXTURES_PATH)

# Iterate through each zip and extract it to its own folder
GuiUtils.sectionPrint("Extracting Packs")
for zip_name in texture_zips:
    with ZipFile(TEXTURES_PATH + zip_name, 'r') as zip:
        zip.extractall(path=(TEXTURES_PATH + zip_name.strip(".zip")))
        print('Extracted: ' + zip_name)

# Gets all the folders from within TEXTURES_FOLDER
texture_folders = OSUtils.getFolders(TEXTURES_PATH)
texture_folders.remove(DEFAULT_TEXTURES)

# Checks each pack to see if the valid files are present
GuiUtils.sectionPrint("Checking Packs")
valid_packs = []
for pack in texture_folders:
    if PackUtils.checkTexturePack(TEXTURES_PATH, pack):
        valid_packs += [pack]
displayPacks = ["textures"] + valid_packs

# Getting all block types and textures
GuiUtils.sectionPrint("Getting blocks and textures")
typesAndTextures = {}
folders = OSUtils.getFolders(TEXTURES_PATH + DEFAULT_TEXTURES)
for folder in folders:
    textures = OSUtils.getFiles(TEXTURES_PATH + DEFAULT_TEXTURES + "/" + folder)
    typesAndTextures.update({folder: textures})

newpack = Pack()

# GUI

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.configure(bg="black")
        self._frame.configure()
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        tk.Label(self, text="MC Texture Pack Combiner", bg="black", fg="white", font=("none", 25)).pack()
        tk.Label(self, text="by Alex", bg="black", fg="white", font=("none", 10)).pack()
        tk.Label(self, text="Please enter texture pack name:", bg="black", fg="white").pack()
        packName = tk.Entry(self, bg="white", fg="black")
        packName.pack()

        tk.Label(self, text="Please enter the pack format you want:", bg="black", fg="white",
                 font=("none", 10)).pack()
        tk.Label(self, text="18 = 1.20.2+", bg="black", fg="white", font=("none", 8)).pack()
        version = tk.Entry(self, bg="white", fg="black")
        version.pack()

        tk.Label(self, text="Please select the name of the texture pack below:", bg="black", fg="white").pack()
        tk.Label(self, text="\"textures\" is the default Minecraft textures", bg="black", fg="white",
                 font=("none", 8)).pack()
        basePack = ttk.Combobox(self, values=displayPacks, state="readonly")
        basePack.set(displayPacks[0])
        basePack.pack()

        tk.Label(self, fg="white", bg="black").pack()
        tk.Button(self, text="Proceed", command=lambda: self.submitForm(packName.get(), basePack.get(), version.get())).pack()

    def submitForm(self, pack_name, basePack, version):
        newpack.setPackInfo(pack_name, basePack, int(version), "Default pack description", list(typesAndTextures.keys()))
        self.master.switch_frame(selectPage)


class selectPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="MC Texture Pack Combiner", bg="black", fg="white", font=("none", 25)).grid(row=0, column=0,
                                                                                                        columnspan=20)
        tk.Label(self, text="Select the texture you would like to change:", bg="black", fg="white",
                 font=("none", 10)).grid(row=1, column=0, columnspan=6)

        def changeTextureDD(*args):
            new_options = typesAndTextures.get(chosenType.get())
            if not new_options:
                new_options = ["null"]
            chosenTexture["values"] = new_options
            chosenTexture.set(new_options[0])
            changePictures()

        def changeTypeBase(*args):
            newpack.changeTypeBase(chosenType.get(), chosenTypeBase.get())

        def createPack(*args):
            PackUtils.createBasePack(OUTPUT_PATH, newpack.getPackName(), newPack.getJson())
            PackUtils.buildPack(newpack.getPackName())


        def changeTexture(*args):
            newpack.assignTexture(chosenType.get(), radios.get(), chosenTexture.get())

        def changePictures(*args):
            for i in range(len(displayPacks)):
                if displayPacks[i] == "textures":
                    path = TEXTURES_PATH + DEFAULT_TEXTURES + "/" + chosenType.get() + "/" + chosenTexture.get()
                else:
                    path = TEXTURES_PATH + displayPacks[
                        i] + "/assets/minecraft/textures/" + chosenType.get() + "/" + chosenTexture.get()
                if not OSUtils.exists(path) or not (".png" in path):
                    path = TEXTURES_PATH + DEFAULT_TEXTURES + "/block/dirt.png"
                img = resizeImage(path, 100, 100)
                packImages[i]['image'] = img
                img.image = img

        packImages = []

        # types dropdown
        tk.Label(self, text="Texture type:", bg="black", fg="white").grid(row=2, column=0, columnspan=1, pady=5,
                                                                          sticky=tkinter.E)
        chosenType = ttk.Combobox(self, values=list(typesAndTextures.keys()), state="readonly")
        chosenType.grid(row=2, column=1, columnspan=1, pady=5, sticky=tkinter.W)
        chosenType.bind("<<ComboboxSelected>>", changeTextureDD)
        chosenType.set(next(iter(typesAndTextures)))

        # typebase dropdown
        tk.Label(self, text="Type base:", bg="black", fg="white").grid(row=2, column=2, columnspan=1, pady=5,
                                                                       sticky=tkinter.E)
        chosenTypeBase = ttk.Combobox(self, values=list(displayPacks), state="readonly")
        chosenTypeBase.grid(row=2, column=3, columnspan=1, pady=5, sticky=tkinter.W)
        chosenTypeBase.set(displayPacks[0])
        (tk.Button(self, text="Change type base", command=changeTypeBase)
         .grid(row=3, column=3, columnspan=1, pady=5, sticky=tkinter.W))

        # Textures dropdown
        tk.Label(self, text="Texture:", bg="black", fg="white").grid(row=3, column=0, columnspan=1, sticky=tkinter.E)
        chosenTexture = ttk.Combobox(self, values=typesAndTextures.get(next(iter(typesAndTextures))), state="readonly")
        chosenTexture.grid(row=3, column=1, columnspan=1, sticky=tkinter.W)
        chosenTexture.bind("<<ComboboxSelected>>", changePictures)
        chosenTexture.set(typesAndTextures.get(next(iter(typesAndTextures)))[0])

        radios = tkinter.StringVar(self, "")
        for i, pack in enumerate(displayPacks):
            if pack == "textures":
                path = TEXTURES_PATH + DEFAULT_TEXTURES + "/" + chosenType.get() + "/" + chosenTexture.get()
            else:
                path = TEXTURES_PATH + pack + "/assets/minecraft/textures/" + chosenType.get() + "/" + chosenTexture.get()
            if not (OSUtils.exists(path) and (".png" in path)):
                path = TEXTURES_PATH + DEFAULT_TEXTURES + "/block/dirt.png"
            img = resizeImage(path, 100, 100)
            texturesImage = ttk.Label(self)
            texturesImage['image'] = img
            img.image = img
            texturesImage.grid(row=4, column=i, columnspan=1, pady=5)
            tkinter.ttk.Radiobutton(self, text=pack, variable=radios, value=pack).grid(row=5, column=i, columnspan=1,
                                                                                    pady=5)
            packImages.append(texturesImage)

        tk.Button(self, text="Change texture", command=changeTexture).grid(row=6, column=0, columnspan=20)
        tk.Button(self, text="create pack", command=createPack).grid(row=7, column=0, columnspan=20)


# GUI

# What a stupid function
def resizeImage(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


app = App()
app.mainloop()
