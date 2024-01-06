from tkinter import ttk
from zipfile import ZipFile
import os

import GuiUtils
import PackUtils
import OSUtils
from EnvVars import *
import tkinter as tk
from PIL import Image, ImageTk


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

# Getting all block types and textures
GuiUtils.sectionPrint("Getting blocks and textures")
typesAndTextures = {}
folders = OSUtils.getFolders(TEXTURES_PATH + DEFAULT_TEXTURES)
for folder in folders:
    textures = OSUtils.getFiles(TEXTURES_PATH + DEFAULT_TEXTURES + "/" + folder)
    typesAndTextures.update({folder: textures})


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
        variable = tk.StringVar(self)
        variable.set(valid_packs[0])
        basePack = tk.OptionMenu(self, variable, *valid_packs)
        basePack.pack()

        tk.Label(self, fg="white", bg="black").pack()
        tk.Button(self, text="Proceed", command=lambda: master.switch_frame(selectPage)).pack()


class selectPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="MC Texture Pack Combiner", bg="black", fg="white", font=("none", 25)).pack()
        tk.Label(self, text="Select the texture you would like to change:", bg="black", fg="white",
                 font=("none", 10)).pack()
        tk.Label(self, text="Texture type:", bg="black", fg="white").pack()







        def changeTextureDD(*args):
            new_options = typesAndTextures.get(chosenType.get())
            if not new_options:
                new_options = ["null"]
            chosenTexture["values"] = new_options

        def changePictures(*args):
            for i in range(len(displayPacks)):
                if displayPacks[i] == "textures":
                    path = TEXTURES_PATH + DEFAULT_TEXTURES + "/" + chosenType.get() + "/" + chosenTexture.get()
                else:
                    path = TEXTURES_PATH + displayPacks[i] + "/assets/minecraft/textures/" + chosenType.get() + "/" + chosenTexture.get()
                if OSUtils.exists(path) and (".png" in path):
                    img = resizeImage(path, 100, 100)
                    packImages[i]['image'] = img
                    img.image = img
                else:
                    print(path)


        # types dropdown
        typeDD = tk.StringVar(self)
        typeDD.set(next(iter(typesAndTextures)))
        chosenType = ttk.Combobox(self, values=list(typesAndTextures.keys()), state="readonly")
        chosenType.pack()
        chosenType.bind("<<ComboboxSelected>>", changeTextureDD)

        # Textures dropdown
        textureDD = tk.StringVar(self)
        textureDD.set(typesAndTextures.get(next(iter(typesAndTextures)))[0])
        chosenTexture = ttk.Combobox(self, values=typesAndTextures.get(next(iter(typesAndTextures))), state="readonly")
        chosenTexture.pack()
        chosenTexture.bind("<<ComboboxSelected>>", changePictures)


        displayPacks = ["textures"] + valid_packs
        packImages = []
        for pack in displayPacks:
            if pack == "textures":
                path = TEXTURES_PATH + DEFAULT_TEXTURES + "/" + chosenType.get() + "/" + chosenTexture.get()
            else:
                path = TEXTURES_PATH + pack + "/assets/minecraft/textures/" + chosenType.get() + "/" + chosenTexture.get()
            if not(OSUtils.exists(path) and (".png" in path)):
                path = TEXTURES_PATH + DEFAULT_TEXTURES + "/block/dirt.png"
            img = resizeImage(path, 100, 100)
            texturesImage = ttk.Label(self)
            texturesImage['image'] = img
            img.image = img
            texturesImage.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            packImages.append(texturesImage)

# GUI

# What a stupid function
def resizeImage(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)




app = App()
app.mainloop()


# GuiUtils.sectionPrint("Debug")
# pack_name = "MyPack1"
# pack_base = "textures"
# pack_format = 22
# pack_description = "My first texture pack"
# newPack = Pack(pack_name, pack_base, pack_format, pack_description)
# newPack.assignTexture("block", "VanillaXBR - 1.20.4", "activator_rail")
# newPack.assignTexture("item", "VanillaXBR - 1.20.4", "*")
#
# PackUtils.createBasePack(OUTPUT_PATH, pack_name, newPack.getJson())
#
# PackUtils.buildPack(pack_name)
#
# print("Done")
