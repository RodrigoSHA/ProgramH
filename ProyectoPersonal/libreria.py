import sqlite3
def menu():
    print("--------------MENU----------------")
    print("1) Crear tabla.")
    print("2) Agregar producto.")
    print("3) Eliminar producto.")
    print("4) Cambiar cantidad de un producto.")
    print("5) Salir.")
while True:
    conexion = sqlite3.connect('libreria.db')
    cursor=conexion.cursor()
    menu()
    opc=int(input("Ingrese la opcion deseada: "))
    if opc==1:   
        cursor.execute('CREATE TABLE productos (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nombre VARCHAR(100), Cantidad INTEGER, Precio FLOAT)')
    elif opc==2:
        prod=str(input("Ingrese el nombre del producto: "))
        cant=int(input("Ingrese la cantidad de productos: "))
        prec=float(input("Ingrese el precio del producto: "))
        cursor.execute("INSERT INTO productos VALUES(null,'{}',{},{})".format(prod,cant,prec))
        conexion.commit()
    elif opc==3:
        prode=str(input("Ingrese el nombre del producto a eliminar: "))
        cursor.execute("DELETE FROM productos WHERE Nombre=='{}'".format(prode))
        conexion.commit()
    elif opc==4:
        proda=str(input("Ingrese el nombre del producto al cual cambiar la cantidad: "))
        cantn=int(input("Ingrese la nueva cantidad del producto: "))
        cursor.execute("UPDATE productos SET Cantidad={} WHERE Nombre='{}'".format(cantn,proda))
        conexion.commit()
    elif opc==5:
        break
conexion.close()