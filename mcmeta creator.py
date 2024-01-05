import tkinter as tk

primary = [
    'option 1',
    'option 2',
    'option 3',
    'option 4'
    ]

options1 = [
    'option 1.1',
    'option 1.2',
    'option 1.3',
    'option 1.4'
    ]
options2 = [
    'option 2.1',
    'option 2.2',
    'option 2.3',
    'option 2.4'
    ]

secondary = options1


#Window builder
window = tk.Tk()
window.geometry('400x200')

#Primary Drop Down Options
primDD = tk.StringVar()
primDD.set(primary[0])
primOpt = tk.OptionMenu(window, primDD, *primary)

#secondary Selector
if primDD.get() == 'options 1':
    secondary = options1
elif primDD.get() == 'options 2':
    secondary = options2

#Secondary Drop Down Options
secDD = tk.StringVar()
secDD.set(secondary[0])
secOpt = tk.OptionMenu(window, secDD, *secondary)

#Window Layout
primOpt.config(width=20)
secOpt.config(width=30)
primOpt.grid(row=0, column=0, padx=1.25, pady=1.25)
secOpt.grid(row=0, column=1, padx=1.25, pady=1.25)

def change_optionmenu2(*args):
    print(args)
    if primDD.get() == "option 1":
        new_options = options1
    elif primDD.get() == "option 2":
        new_options = options2
    else:
        new_options = ["Not coded in"]
    secDD.set('')
    secOpt['menu'].delete(0, 'end')
    for choice in new_options:
        secOpt['menu'].add_command(label=choice, command=tk._setit(secDD, choice))
    secDD.set(new_options[0])

primDD.trace("w", change_optionmenu2)

window.mainloop()