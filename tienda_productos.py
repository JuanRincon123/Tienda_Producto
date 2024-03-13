from tkinter import *
from tkinter import ttk
class Product():
    def __init__(self,window):
        self.win=window
        self.win.title("TIENDA-PRODUCTOS")
    
        frame=LabelFrame(self.win,text="register new product")
        frame.grid(row=0,column=0,columnspan=3,pady=20)

        Label(frame ,text="Nombre: ").grid(row=1,column=0)
        self.Nombre=Entry(frame).grid(row=1,column=1)

        Label(frame ,text="Categoria: ").grid(row=2,column=0)
        self.Categoria=Entry(frame).grid(row=2,column=1, columnspan=2,pady=10)

        Label(frame ,text="Precio: ").grid(row=3,column=0)
        self.Precio=Entry(frame).grid(row=3,column=1,columnspan=2, pady=10)

        Label(frame ,text="Cantidad: ").grid(row=4,column=0)
        self.Cantidad=Entry(frame).grid(row=4,column=1,columnspan=2 ,pady=10)

        Button(frame, text="Guardar Producto").grid(row=5,columnspan=2, sticky=W+E)

        self.tabla=ttk.Treeview(height=10,column=("size","j","lastmod"),padding=10)
        self.tabla.grid(row=6,column=1)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("j",text="Categoria",anchor=CENTER)
        self.tabla.heading("size",text="Precio",anchor=CENTER)
        self.tabla.heading("lastmod",text="Cantidad",anchor=CENTER)

if __name__=="__main__":
    window=Tk()
    application=Product(window)
    window.mainloop()