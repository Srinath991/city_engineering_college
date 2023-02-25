import tkinter as tk
from time import strftime
def sri():
    global pysri
    obj=strftime('%I:%M:%S %p')
    pysri.config(text=obj)
    pysri.after(1000,sri)
root=tk.Tk()
root.title('Digital Clock')
pysri=tk.Label(root,text='00:00:00 AM',bg='purple',fg='white',font=('calibri',40,'bold'))
pysri.grid(row=0,column=0,)
sri()
root.mainloop()