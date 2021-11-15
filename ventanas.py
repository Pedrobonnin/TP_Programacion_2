import sqlite3                  # Importamos módulo de manejo de Bases de Datos
from tkinter import *           # Importamos módulo de Interfaz Gráfica
from tkinter import ttk, Frame
from tkinter import messagebox

# ======================= I N T E R F A Z      G R A F I C A ========================
ventana = Tk()
# ======================= C O N E X I O N  A  BD========================
conexion = sqlite3.connect("gestion.db")
# ======================= CREACION BASES DE DATOS ========================


def crearDB():
    cursor = conexion.cursor()
    
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Proveedores (                       
            id	INTEGER NOT NULL UNIQUE,
            nombre	TEXT NOT NULL,
            calle	INTEGER,
            altura	INTEGER ,
            localidad	INTEGER ,
            email	TEXT NOT NULL,
            celular	INTEGER NOT NULL,
            cbu	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT))
            ''')
    except sqlite3.OperationalError:
        print("La tabla que intenta crear ya exite")
    else:
        print("La tabla se ha creado correctamente")
     

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Productos (                       
            id	INTEGER NOT NULL UNIQUE,
            producto	INTEGER NOT NULL UNIQUE,
            precio	INTEGER NOT NULL,
            proveedor	INTEGER NOT NULL,
	        stock	INTEGER,
            FOREIGN KEY("proveedor") REFERENCES "Proveedores"("id"),
            FOREIGN KEY("producto") REFERENCES "Ventas"("id"),
	        PRIMARY KEY("id" AUTOINCREMENT))
            ''')
    except sqlite3.OperationalError:
        print("La tabla que intenta crear ya exite")
    else:
        print("La tabla se ha creado correctamente")

    

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Ventas (
            id	INTEGER NOT NULL UNIQUE,
            fecha	INTEGER NOT NULL,
            producto	INTEGER NOT NULL,
        	PRIMARY KEY("id" AUTOINCREMENT))''')
    except sqlite3.OperationalError:
        print("La tabla que intenta crear ya exite")
    else:
        print("La tabla se ha creado correctamente")

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Caja (
            id	INTEGER NOT NULL,
            fecha	INTEGER NOT NULL,
            importe_ventas	INTEGER NOT NULL,
            saldo_inicial	INTEGER NOT NULL,
            pago_proveedor	INTEGER NOT NULL,
            FOREIGN KEY("fecha") REFERENCES "Ventas"("fecha"),
            PRIMARY KEY("id" AUTOINCREMENT))
            ''')
    except sqlite3.OperationalError:
        print("La tabla que intenta crear ya exite")
    else:
        print("La tabla se ha creado correctamente")

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS Compras (
            id	INTEGER NOT NULL,
            fecha	INTEGER NOT NULL,
            producto	INTEGER NOT NULL,
            precio      INTEGER NOT NULL
            proveedor	INTEGER NOT NULL,
            cantidad	INTEGER NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT))
            ''')
    except sqlite3.OperationalError:
        print("La tabla que intenta crear ya exite")
    else:
        print("La tabla se ha creado correctamente")

    conexion.close()

# ==========================C E R R A R    V E N T A N A=========================================

def salir():
    ventana.quit()

# =========================A G R E G A R   P R O V E E D O R=====================================


def Agregar_proveedor():
    cursor = conexion.cursor()
    try:
        datos = (nombre.get(),calle.get(),altura.get(),localidad.get(),email.get(),celular.get(),cbu.get())
        cursor.execute("INSERT INTO Proveedores VALUES(NOT NULL,?,?,?,?,?,?,?)", (datos))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("CONEXION", "Registro creado exitosamente")
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al crear el registro, verifique conexión con la Base de Datos")
    pass
    limpiarCamposProveedores()

# =========================A G R E G A R   P R O V E E D O R=====================================

def Agregar_productos():
    conexion = sqlite3.connect("gestion.db")
    cursor = conexion.cursor()
    try:
        datos = (producto.get(),precio.get(),proveedor.get(),stock.get())
        cursor.execute("INSERT INTO Productos VALUES(NOT NULL,?,?,?,?)", (datos))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("CONEXION", "Registro creado exitosamente")
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al crear el registro, verifique conexión con la Base de Datos")
    pass
    limpiarProductos()
# =========================A G R E G A R   C O M P R A S=====================================

def Agregar_compras():
    conexion = sqlite3.connect("gestion.db")
    cursor = conexion.cursor()
    try:
        datos = (fecha_compra.get(),producto_compra.get(),proveedor_compra.get(),cantidad_compra.get())
        cursor.execute("INSERT INTO Compras VALUES(NOT NULL,?,?,?,?)", (datos))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("CONEXION", "Registro creado exitosamente")
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al crear el registro, verifique conexión con la Base de Datos")
    pass
    limpiarCompras()


# =========================A G R E G A R   V E N T A S=====================================
def Agregar_venta():
    conexion = sqlite3.connect("gestion.db")
    cursor = conexion.cursor()
    try:
        datos = (fecha_venta.get(),producto_venta.get())
        cursor.execute("INSERT INTO Ventas VALUES(NOT NULL,?,?)", (datos))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("CONEXION", "Registro creado exitosamente")
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al crear el registro, verifique conexión con la Base de Datos")
    pass
    limpiarVentas()


# =======================L I M P I A R    C A M P O S   D E   D A T O S=============================

def Elimina():
    
    pass

# =======================L I M P I A R    F O R M U L A R I O=============================

#---------------------------limpiar Proveedores------------------------------------------------------
def limpiarCamposProveedores():
    nombre.set("")
    calle.set("")
    altura.set("")
    localidad.set("")
    email.set("")
    celular.set("")
    cbu.set("")

#---------------------------limpiar Productos------------------------------------------------------
def limpiarProductos():
    producto.set("")
    precio.set("")
    proveedor.set("")
    stock.set("")

#---------------------------limpiar compras------------------------------------------------------
def limpiarCompras():
    fecha_compra.set("")
    producto_compra.set("")
    proveedor_compra.set("")
    cantidad_compra.set("")

#---------------------------limpiar ventas------------------------------------------------------
def limpiarVentas():
    fecha_venta.set("")
    producto_venta.set("")


# ==============================M O S T R A R    D A T O S=============================
def Leer_proveedores():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Proveedores")
    datos = cursor.fetchall()
    return datos

def Leer_ventas():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Ventas")
    datos = cursor.fetchall()
    return datos

def Leer_caja():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Caja")
    datos = cursor.fetchall()
    return datos
   
 

def Tabla_focus():

    pass
        

 
# ==============================V E N T A N A   P R O V E E D O R E S=============================
def proveedores():
    ventanaProveedores = Toplevel(ventana)
    ventanaProveedores.title("Proveedores")
    ventanaProveedores.geometry("710x600")
    ventanaProveedores.resizable(0,0)
    ventanaProveedores.config(bg="#E4E4E4")

    frame= Frame(ventanaProveedores) 
    frame.place(x=110,y=10,width=500,height=200) 

    lblnombre = Label(frame, text="Nombre")
    # grid en este caso reemplaza a pack
    lblnombre.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    nombre_ = Entry(frame, relief="flat", textvariable=nombre)
    nombre_.grid(row=0, column=1, padx=10, pady=10)

    lblCalle = Label(frame, text="Calle")
    lblCalle.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    calle_ = Entry(frame, relief="flat", textvariable=calle)
    calle_.grid(row=2, column=1, padx=10, pady=10)

    lblAltura = Label(frame, text="Altura")
    lblAltura.grid(row=3, column=0, sticky="e")
    altura_ = Entry(frame, relief="flat", textvariable=altura)
    altura_.grid(row=3, column=1,padx=10, pady=10)

    lblLocalidad = Label(frame, text="Localidad")
    lblLocalidad.grid(row=1, column=2, sticky="e", padx=10, pady=10)
    localidad_ = Entry(frame, relief="flat", textvariable=localidad)
    localidad_.grid(row=1, column=3, padx=10, pady=10)

    lblemail = Label(frame, text="Email")
    lblemail.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    email_ = Entry(frame, relief="flat", textvariable=email)
    email_.grid(row=1, column=1, padx=10, pady=10)

    lblcelular = Label(frame, text="Celular")
    lblcelular.grid(row=2, column=2, sticky="e", padx=10, pady=10)
    celular_ = Entry(frame, relief="flat", textvariable=celular)
    celular_.grid(row=2, column=3, padx=10, pady=10)

    lblcbu = Label(frame, text="CBU")
    lblcbu.grid(row=0, column=2, sticky="e", padx=10, pady=10)
    cbu_ = Entry(frame, relief="flat", textvariable=cbu)
    cbu_.grid(row=0, column=3, padx=10, pady=10)

    frame1= Frame(ventanaProveedores) 
    frame1.place(x=10,y=250,width=700,height=259)                  
        
    tabla=ttk.Treeview(frame1,columns=("col1","col2","col3","col4","col5","col6")) 
    tabla.column("#0",width=100, anchor=CENTER)
    tabla.column("col1",width=100, anchor=CENTER)
    tabla.column("col2",width=90, anchor=CENTER)
    tabla.column("col3",width=90, anchor=CENTER)
    tabla.column("col4",width=100, anchor=CENTER)
    tabla.column("col5",width=100, anchor=CENTER)
    tabla.column("col6",width=100, anchor=CENTER)
    tabla.heading("#0",text="Nombre", anchor=CENTER)
    tabla.heading("col1",text="Calle", anchor=CENTER)
    tabla.heading("col2",text="Altura", anchor=CENTER)
    tabla.heading("col3",text="Localidad", anchor=CENTER)
    tabla.heading("col4",text="Email", anchor=CENTER)
    tabla.heading("col5",text="Celular", anchor=CENTER)
    tabla.heading("col6",text="Cbu", anchor=CENTER)
    
    tabla.pack(side=LEFT,fill = Y)        
    sb = Scrollbar(frame1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill = Y)
    tabla.config(yscrollcommand=sb.set)
    sb.config(command=tabla.yview)
        

    #insertar datos en  tabla
    datos =Leer_proveedores()
    for row in datos:
        tabla.insert("",END, text=row[1], values=(row[2],row[3],row[4],row[5],row[6],row[7]))
        

    
    boton_proveedor = Button(ventanaProveedores, text="Agregar", command=Agregar_proveedor,bg="#3eb070",relief="flat")
    boton_proveedor.place(x=110,y=220)
    boton_proveedor_buscar = Button(ventanaProveedores, text="Buscar", command="", bg="#2e69a0",relief="flat")
    boton_proveedor_buscar.place(x=200,y=220)
    boton_proveedor_buscar_ = Entry(ventanaProveedores, bg="#E4E4E4")
    boton_proveedor_buscar_.place(x=250,y=220, width=200, height=25)
    boton_proveedor = Button( ventanaProveedores, text="Salir", command=ventanaProveedores.destroy ,bg="#d9594d",relief="flat")
    boton_proveedor.place(x=635,y=550, width=55, height=30)


# =========================V E N T A N A   P R O D U C T O S=============================
def productos():
    ventanaProductos = Toplevel(ventana)
    ventanaProductos.title("Productos")
    ventanaProductos.geometry("800x600")

    lblProducto = Label(ventanaProductos, text="Producto")
    # grid en este caso reemplaza a pack
    lblProducto.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    Producto_ = Entry(ventanaProductos, textvariable=producto)
    Producto_.grid(row=0, column=1, padx=10, pady=10)

    lblPrecio = Label(ventanaProductos, text="Precio")
    lblPrecio.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    Precio_ = Entry(ventanaProductos, textvariable=precio)
    Precio_.grid(row=1, column=1, padx=10, pady=10)

    lblPrveedor = Label(ventanaProductos, text="Prveedor")
    lblPrveedor.grid(row=0, column=2, sticky="e", padx=10, pady=10)
    Prveedor_ = Entry(ventanaProductos, textvariable=proveedor)
    Prveedor_.grid(row=0, column=3, padx=10, pady=10)

    lblStock = Label(ventanaProductos, text="Stock")
    lblStock.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Stock_ = Entry(ventanaProductos, textvariable=stock)
    Stock_.grid(row=3, column=1, padx=10, pady=10)

    boton_productos = Button(
        ventanaProductos, text="Agregar", command=Agregar_productos)
    boton_productos.grid(row=100)
    boton_proveedor = Button(ventanaProductos, text="Buscar", command="")
    boton_proveedor.grid(row=100, column=1)
    boton_proveedor_ = Button(ventanaProductos, text="Salir", command=ventanaProductos.destroy)
    boton_proveedor_.grid(row=100, column=2)


# =========================V E N T A N A   C O M P R A S=============================

def compras():
    ventanaCompras = Toplevel(ventana)
    ventanaCompras.title("Productos")
    ventanaCompras.geometry("800x600")

    lblProducto = Label(ventanaCompras, text="Producto")
    # grid en este caso reemplaza a pack
    lblProducto.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    Producto_ = Entry(ventanaCompras, textvariable=producto_compra)
    Producto_.grid(row=0, column=1, padx=10, pady=10)

    lblPrecio = Label(ventanaCompras, text="Precio")
    lblPrecio.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    Precio_ = Entry(ventanaCompras, textvariable=precio_compra)
    Precio_.grid(row=1, column=1, padx=10, pady=10)

    lblPrveedor = Label(ventanaCompras, text="Prveedor")
    lblPrveedor.grid(row=0, column=2, sticky="e", padx=10, pady=10)
    Prveedor_ = Entry(ventanaCompras, textvariable=proveedor_compra)
    Prveedor_.grid(row=0, column=3, padx=10, pady=10)

    lblCantidad = Label(ventanaCompras, text="Cantidad")
    lblCantidad.grid(row=1, column=2, sticky="e", padx=10, pady=10)
    Cantidad = Entry(ventanaCompras, textvariable=cantidad_compra)
    Cantidad.grid(row=1, column=3, padx=10, pady=10)

    lblFecha = Label(ventanaCompras, text="Fecha")
    lblFecha.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Fecha_ = Entry(ventanaCompras, textvariable=fecha_compra)
    Fecha_.grid(row=3, column=1, padx=10, pady=10)

    boton_Compras = Button(ventanaCompras, text="Agregar", command=Agregar_compras)
    boton_Compras.grid(row=100)
    boton_Compras = Button(ventanaCompras, text="Buscar", command="")
    boton_Compras.grid(row=100, column=1)
    boton_Compras_ = Button( ventanaCompras, text="Salir", command=ventanaCompras.destroy)
    boton_Compras_.grid(row=100, column=2)

# =========================V E N T A N A   V E N T A S=============================
def ventas():
    ventanaVentas = Toplevel(ventana)
    ventanaVentas.geometry("325x535")
    ventanaVentas.title("Ventas")
    ventanaVentas.resizable(0,0)  
    
    
    frame = Frame(ventanaVentas,bg="#d3d3d3" ) 
    frame.place(x=10,y=5,width=304,height=230)   

    lblproducto = Label(frame, text="Producto",bg="#d3d3d3" )
    lblproducto.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    producto_ = Entry(frame, relief="flat", textvariable=producto_venta)
    producto_.grid(row=2, column=1, pady=10)

    lblFecha = Label(frame, text="Fecha",bg="#d3d3d3" )
    lblFecha.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Fecha_ = Entry(frame, relief="flat", textvariable=fecha_venta )
    Fecha_.grid(row=3, column=1, padx=10, pady=10)


    frame1= Frame(ventanaVentas) 
    frame1.place(x=10,y=250,width=310,height=250)                  
    tabla=ttk.Treeview(frame1,columns=("col1")) 
    tabla.column("#0",width=100, anchor=CENTER)
    tabla.column("col1",width=190, anchor=CENTER)
    tabla.heading("#0",text="Fecha", anchor=CENTER)
    tabla.heading("col1",text="Productos", anchor=CENTER)

    tabla.pack(side=LEFT,fill = Y)        
    sb = Scrollbar(frame1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill = Y)
    tabla.config(yscrollcommand=sb.set)
    sb.config(command=tabla.yview)

    datos =Leer_ventas()
    for row in datos:
        tabla.insert("",END, text=row[1], values=(row[2]))
        
    
   
    boton_listar = Button(frame, text="Listar", command=Leer_caja,bg="#3eb070",relief="flat")
    boton_listar.place(x=130,y=200)
    boton_Ventas = Button(frame, text="Agregar", command=Agregar_venta,bg="#3eb070",relief="flat")
    boton_Ventas.place(x=120,y=100)
    boton_Ventas = Button(ventanaVentas, text="Salir", command=ventanaVentas.destroy, bg="#d9594d",relief="flat")
    boton_Ventas.place(x=280,y=505)



# ===================I N I C I A L I Z A R       V A L I A B L E S=============================

#VARIABLES PROVEDOR
nombre = StringVar()
calle = StringVar()
altura = StringVar()
email = StringVar()
localidad = StringVar()
cbu = StringVar()
celular = StringVar()

#VARIABLES PRDUCTO
producto = StringVar()
precio = StringVar()
proveedor = StringVar()
stock = StringVar()

#VARIABLES COMPRAS
fecha_compra = StringVar()
producto_compra = StringVar()
precio_compra = StringVar()
proveedor_compra = StringVar()
cantidad_compra = StringVar()

#VARIABLES VENTAS
fecha_venta = StringVar()
producto_venta = StringVar()


tabla_focus = StringVar()

# ===================V E N T A N A============================
ventana.title("Caja")
ventana.geometry("525x580")
ventana.resizable(0,0)
    

frame = Frame(ventana,bg="#d3d3d3" ) 
frame.place(x=100,y=5,width=330,height=265)         
lblventas = Label(frame, text="Ventas",font=("Helvetica" ,18),bg="#d3d3d3" )
lblventas.grid(row=0, column=1, sticky="e", padx=50, pady=20)


lblproducto = Label(frame, text="Producto",bg="#d3d3d3")
lblproducto.grid(row=1, column=0, sticky="e", padx=10, pady=10)
producto_ = Entry(frame, relief="flat", textvariable=producto_venta)
producto_.grid(row=1, column=1, pady=10)

lblFecha = Label(frame, text="Fecha",bg="#d3d3d3" )
lblFecha.grid(row=2, column=0, sticky="e", padx=10, pady=10)
Fecha_ = Entry(frame, relief="flat", textvariable=fecha_venta )
Fecha_.grid(row=2, column=1, padx=10, pady=10)




frame1= Frame(ventana) 
frame1.place(x=10,y=275,width=510,height=250)                  
tabla=ttk.Treeview(frame1,columns=("col1","col2","col3","col4")) 
tabla.column("#0",width=90, anchor=CENTER)
tabla.column("col1",width=100, anchor=CENTER)
tabla.column("col2",width=100, anchor=CENTER)
tabla.column("col3",width=100, anchor=CENTER)
tabla.column("col4",width=100, anchor=CENTER)
tabla.heading("#0",text="Fecha", anchor=CENTER)
tabla.heading("col1",text="Saldo inicial", anchor=CENTER)
tabla.heading("col2",text="Importe de venta", anchor=CENTER)
tabla.heading("col3",text="Pago proveedor", anchor=CENTER)
tabla.heading("col4",text="Saldo final", anchor=CENTER)

tabla.pack(side=LEFT,fill = Y)        
sb = Scrollbar(frame1, orient=VERTICAL)
sb.pack(side=RIGHT, fill = Y)
tabla.config(yscrollcommand=sb.set)
sb.config(command=tabla.yview)
    

#insertar datos en  tabla
datos = Leer_caja()
for row in datos:
    tabla.insert("",END, text=row[1], values=(row[2],row[3],row[4]))
    


boton_caja = Button(ventana, text="Agregar", command=Agregar_venta,bg="#3eb070",relief="flat")
boton_caja.place(x=240,y=160)
boton_caja_buscar = Button(ventana, text="Buscar", command="", bg="#2e69a0",relief="flat")
boton_caja_buscar.place(x=153,y=220)
boton_caja_buscar_ = Entry(ventana, bg="#E4E4E4")
boton_caja_buscar_.place(x=200,y=220, width=200, height=25)
boton_caja_salir = Button( ventana, text="Salir", command=salir,bg="#d9594d",relief="flat")
boton_caja_salir.place(x=437,y=530, width=55, height=30)




# ===================M E N U=============================

barra_de_menu = Menu(ventana)
ventana.config(menu=barra_de_menu)


menuPrincipal = Menu(barra_de_menu, tearoff=0)
menuPrincipal.add_command(label="Proveedores", command=proveedores)
menuPrincipal.add_command(label="Caja")
menuPrincipal.add_command(label="Compras", command=compras)
menuPrincipal.add_command(label="Productos", command=productos)
menuPrincipal.add_command(label="Ventas", command=ventas)
menuPrincipal.add_separator()
menuPrincipal.add_command(label="Salir", command=salir)

menuTablas = Menu(barra_de_menu, tearoff=0)
menuTablas.add_cascade(label="Crear Tablas", command=crearDB)
menuTablas.add_cascade(label="Historial")
menuTablas.add_cascade(label="Categorías de productos")

menuAyuda = Menu(barra_de_menu, tearoff=0)
menuAyuda.add_command(label="Acerca de...")

barra_de_menu.add_cascade(label="Principal", menu=menuPrincipal)
barra_de_menu.add_cascade(label="Tablas", menu=menuTablas)
barra_de_menu.add_cascade(label="Ayuda", menu=menuAyuda)


ventana.mainloop()
