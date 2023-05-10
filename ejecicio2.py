import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry('300x200')
def changed(e):
  lblresult['text'] = f'Se escogió la opción: {combo.get()}'

lbl1 = ttk.Label(window,text='     ')
lbl1.grid(row=0, column=0, sticky="e")
lbl2 = ttk.Label(window,text='Escojer una opción:')
lbl2.grid(row=1, column=0, sticky="w",padx=5)
combo = ttk.Combobox(window, values=['Ropa','Zapatos','Accesorios','Otros'])
combo.grid(column=0,row=2,sticky='e',padx=5)
combo.bind("<<ComboboxSelected>>",changed)

lbl__ = ttk.Label(window,text='     ')
lbl__.grid(row=3, column=0, sticky="e")
lblresult = ttk.Label(window,text='Se escogió la opción:')
lblresult.grid(row=4, column=0, sticky="n")
window.mainloop()
