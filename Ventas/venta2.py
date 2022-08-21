from tkinter import *
from tkinter import messagebox
from Datos import Database

datos = Database('ventas.db')


def populate_list():
        for row in datos.fetch():
            Producto_list.insert(END, row)

def add_item():
    if producto_text.get() == '' or cliente_text.get() == '' or vendedor_text.get() == '' or precio_text.get() == '':
        messagebox.showerror('Require Fileds','Please include all flieds')
        return
    datos.insert(producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    Producto_list.delete(0, END)
    Producto_list.insert(END, (producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get()))
    clear_text()
    populate_list()






def select_item(event):
    try:

        global select_item
        index = Producto_list.curselection() [0]
        select_item = Producto_list.get(index)

        producto_entry.delete(0, END)
        producto_entry.insert(END, select_item[1])
        cliente_entry.delete(0, END)
        cliente_entry.insert(END, select_item[2])
        vendedor_entry.delete(0, END)
        vendedor_entry.insert(END, select_item[3])
        precio_entry.delete(0, END)
        precio_entry.insert(END, select_item[4])
    except IndexError:
        pass




def remove_item():
    datos.remove(select_item[0])
    clear_text()
    populate_list()

def update_item():
    datos.update(select_item[0], producto_text.get(), cliente_text.get(), vendedor_text.get(), precio_text.get())
    populate_list()

def clear_text():
    producto_entry.delete(0, END)
    cliente_entry.delete(0, END)
    vendedor_entry.delete(0, END)
    precio_entry.delete(0, END)


app = Tk()

producto_text = StringVar()
producto_Label = Label(app, text="Producto", font=("blod", 12))
producto_Label.grid(row=0, column=0, sticky=W)
producto_entry = Entry(app, textvariable=producto_text)
producto_entry.grid(row=0, column=1)

cliente_text = StringVar()
cliente_Labe1 = Label(app, text="Cliente", font=("blod", 12))
cliente_Labe1.grid(row=0, column=2, sticky=W)
cliente_entry = Entry(app, textvariable=cliente_text)
cliente_entry.grid(row=0, column=3)

vendedor_text = StringVar()
vendedor_Label = Label(app, text="Vendedor", font=("blod", 12))
vendedor_Label.grid(row=1, column=0, sticky=W)
vendedor_entry = Entry(app, textvariable=vendedor_text)
vendedor_entry.grid(row=1, column=1)

precio_text = StringVar()
precio_Label = Label(app, text="Precio", font=("blod", 12))
precio_Label.grid(row=1, column=2, sticky=W)
precio_entry = Entry(app, textvariable=precio_text)
precio_entry.grid(row=1, column=3)

Producto_list = Listbox(app, height=8, width=50, border=0)
Producto_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)


Producto_list.bind('<<Listboxselect>>', select_item)


btn1 = Button(app, text="Agregar", width=12)
btn1.grid(row=2, column=0, pady=20)

btn2 = Button(app, text="Eliminar", width=12)
btn2.grid(row=2, column=1)


btn3 = Button(app, text="Actualizar", width=12)
btn3.grid(row=2, column=2)

btn4 = Button(app, text="Limpiar", width=12)
btn4.grid(row=2, column=3)





app.title("Gerente de ventas")
app.geometry("700x350")
populate_list()

app.mainloop()