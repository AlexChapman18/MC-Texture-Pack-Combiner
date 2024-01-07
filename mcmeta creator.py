from tkinter import *
import ctypes

# end of imports

# try for hidpi

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except: pass

window = Tk()
window.title("pack.mcmeta Creator v1.4")
window.configure(bg="black")
window.resizable(width=FALSE, height=FALSE)


# variables

# there aren't any needed functions

# functions


def generatemcmeta():
    resPackName = nameEntry.get()
    minecraftVersion = versionEntry.get()
    packmcmeta = open('pack.mcmeta', 'w+')
    filecontents = '{"pack":{"pack_format":' + minecraftVersion + ',"description":"' + resPackName + '"}}'
    packmcmeta.write(filecontents)
    packmcmeta.close()
    generateStatus.config(text="The file has been generated!", fg="green")


# tkinter elements

titleLabel = Label(window, text="pack.mcmeta Creator", bg="black", fg="white", font=("none", 25)) .pack()
titleSpace = Label(window, text="by cnnd", bg="black", fg="white", font=("none", 7)) .pack()
versionLabel = Label(window, text="Please enter the desired Minecraft version below.", bg="black", fg="white") .pack()
versionEntry = Entry(window, bg="white", fg="black")
versionEntry.pack()
versionHelpLabel1 = Label(window, text="1 for Minecraft 1.6 to 1.8", bg="black", fg="white", font=("none", 10)) .pack()
versionHelpLabel2 = Label(window, text="2 for Minecraft 1.9 and 1.10", bg="black", fg="white", font=("none", 10)) .pack()
versionHelpLabel3 = Label(window, text="3 for Minecraft 1.11 and 1.12", bg="black", fg="white", font=("none", 10)) .pack()
versionHelpLabel4 = Label(window, text="4 for Minecraft 1.13 and 1.14", bg="black", fg="white", font=("none", 10)) .pack()
versionHelpLabel4 = Label(window, text="5 for Minecraft 1.15 and 1.16", bg="black", fg="white", font=("none", 10)) .pack()
nameLabel = Label(window, text="Please enter the name of the texture pack below.", bg="black", fg="white") .pack()
nameEntry = Entry(window, bg="white", fg="black")
nameEntry.pack()
generateSpace = Label(window, fg="white", bg="black") .pack()
generateButton = Button(window, text="Generate pack.mcmeta", command=generatemcmeta) .pack()
generateStatus = Label(window, text="The file has not been generated.", bg="black", fg="red")
generateStatus.pack()


window.mainloop()