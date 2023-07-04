from tkinter import *
from tkinter import ttk, messagebox
import math
class Aplicacion():
    __ventana = None
    
    __vest_cant = None
    __vest_base = None
    __vest_actual = None
    
    __ali_cant = None
    __ali_base = None
    __ali_actual = None
    
    __edu_cant = None
    __edu_base = None
    __edu_actual = None
    
    __ipc = None
    def __init__(self):
        self.__ventana = Tk()
        #self.__ventana.geometry('500x150')
        self.__ventana.title('Calculadora IPC')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        self.__vest_actual = StringVar()
        self.__vest_cant = StringVar()
        self.__vest_base = StringVar()
        self.__ali_actual = StringVar()
        self.__ali_cant = StringVar()
        self.__ali_base = StringVar()
        self.__edu_actual = StringVar()
        self.__edu_cant = StringVar()
        self.__edu_base = StringVar()
        self.__ipc = StringVar()
        
        ttk.Label(mainframe, text="Item").grid(column=0, row=0,padx=10,pady=10)
        ttk.Label(mainframe, text="Cantidad").grid(column=1, row=0,padx=10,pady=10)
        ttk.Label(mainframe, text="Precio Año Base").grid(column=2, row=0,padx=10,pady=10)
        ttk.Label(mainframe, text="Precio Año Actual").grid(column=3, row=0,padx=10,pady=10)
        
        ttk.Label(mainframe, text="Vestimenta").grid(column=0, row=1,padx=10,pady=10)
        self.vest_cantEntry=ttk.Entry(mainframe, width=15, textvariable=self.__vest_cant)
        self.vest_cantEntry.grid(column=1,row=1,padx=10,pady=10)
        self.vest_baseEntry=ttk.Entry(mainframe, width=15, textvariable=self.__vest_base)
        self.vest_baseEntry.grid(column=2,row=1,padx=10,pady=10)
        self.vest_actualEntry=ttk.Entry(mainframe, width=15, textvariable=self.__vest_actual)
        self.vest_actualEntry.grid(column=3,row=1,padx=10,pady=10)
        
        ttk.Label(mainframe, text="Alimentos").grid(column=0, row=2,padx=10,pady=10)
        self.ali_cantEntry=ttk.Entry(mainframe, width=15, textvariable=self.__ali_cant)
        self.ali_cantEntry.grid(column=1,row=2,padx=10,pady=10)
        self.ali_baseEntry=ttk.Entry(mainframe, width=15, textvariable=self.__ali_base)
        self.ali_baseEntry.grid(column=2,row=2,padx=10,pady=10)
        self.ali_actualEntry=ttk.Entry(mainframe, width=15, textvariable=self.__ali_actual)
        self.ali_actualEntry.grid(column=3,row=2,padx=10,pady=10)
        
        ttk.Label(mainframe, text="Educación").grid(column=0, row=3,padx=10,pady=10)
        self.edu_cantEntry=ttk.Entry(mainframe, width=15, textvariable=self.__edu_cant)
        self.edu_cantEntry.grid(column=1,row=3,padx=10,pady=10)
        self.edu_baseEntry=ttk.Entry(mainframe, width=15, textvariable=self.__edu_base)
        self.edu_baseEntry.grid(column=2,row=3,padx=10,pady=10)
        self.edu_actualEntry=ttk.Entry(mainframe, width=15, textvariable=self.__edu_actual)
        self.edu_actualEntry.grid(column=3,row=3,padx=10,pady=10)
        
        ttk.Button(mainframe, text='Calcular IPC', command=self.calcularIPC).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=5, sticky=W)
        
        
        ttk.Label(mainframe, text="IPC %").grid(column=0, row=6,padx=10,pady=10)
        ttk.Label(mainframe, textvariable=self.__ipc).grid(column=1, row=6, sticky=(W, E))
        ttk.Label(mainframe, text=" %").grid(column=2, row=6,padx=10,pady=10, sticky=(W))
        
        
        self.__ventana.mainloop()
        
    def calcularIPC(self):
        try:
            v_cant = int(self.vest_cantEntry.get())
            v_bas = float(self.vest_baseEntry.get())
            v_act = float(self.vest_actualEntry.get())
            
            a_cant = int(self.ali_cantEntry.get())
            a_bas = float(self.ali_baseEntry.get())
            a_act = float(self.ali_actualEntry.get())
            
            e_cant = int(self.edu_cantEntry.get())
            e_bas = float(self.edu_baseEntry.get())
            e_act = float(self.edu_actualEntry.get())
            
            actual = v_cant*v_act + a_cant*a_act + e_cant*e_act
            base = v_cant*v_bas + a_cant*a_bas + e_cant*e_bas
            ipc = actual/base
            
            self.__ipc.set((ipc - math.floor(ipc))*100)
            
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numéricos')
            self.__vest_actual.set('')
            self.__vest_cant.set('')
            self.__vest_base.set('')
            self.__ali_actual.set('')
            self.__ali_cant.set('')
            self.__ali_base.set('')
            self.__edu_actual.set('')
            self.__edu_cant.set('')
            self.__edu_base.set('')
            self.__ipc.set('')
            
            self.vest_cantEntry.focus()
            self.vest_actualEntry.focus()
            self.ali_cantEntry.focus()
            self.ali_actualEntry.focus()
            self.edu_cantEntry.focus()
            self.edu_actualEntry.focus()
            self.vest_baseEntry.focus()
            self.ali_baseEntry.focus()
            self.edu_baseEntry.focus()
            
