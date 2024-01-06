import tkinter as tk

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
        variable.set(TYPES[0])
        basePack = tk.OptionMenu(self, variable, *TYPES)
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

        typeDD = tk.StringVar(self)
        typeDD.set(TYPES[0])
        chosenType = tk.OptionMenu(self, typeDD, *TYPES)
        chosenType.pack()

        textureDD = tk.StringVar(self)
        textureDD.set(BLOCK[0])
        chosenTexture = tk.OptionMenu(self, textureDD, *BLOCK)
        chosenTexture.pack()

        def changeTextureDD(*args):
            if typeDD.get() == "blocks":
                new_options = BLOCK
            elif typeDD.get() == "items":
                new_options = ITEMS
            else:
                new_options = ITEMS
            textureDD.set('')
            textureDD.set(new_options[0])

        typeDD.trace("w", changeTextureDD)



if __name__ == "__main__":
    app = App()
    app.mainloop()
