from admindatos import AdminDatos
lista=AdminDatos.leer_csv("dataset3_clinical_supplies_inventory.csv")
print("Elige una opcion para gestionar los suministro:")
print("1. Buscar por stock:")
print("2. Alerta de stock por vencer")
print("3. Buscar por lote")

opcion_principal = input("Selecciona la opcion principal:")
if opcion_principal == '1':
    print("Busquedas por stock:")
    print("a. Stock por distribuidor")
    print("b. Stock por estado")
    print("c. Stock por item")
    print("d. Stock por categoria")
    print("e. Stock por bodega")

    opcion_stock=str(input("Elige una opcion por stock:"))
    if opcion_stock == 'a':
        print(AdminDatos.stockpor(lista,"supplier"))
    elif opcion_stock == 'b':
        print(AdminDatos.stockpor(lista,"status"))
    elif opcion_stock == 'c':
        print(AdminDatos.stockpor(lista,"item_name"))
    elif opcion_stock == 'd':
        print(AdminDatos.stockpor(lista,"category"))
    elif opcion_stock == 'e':
        print(AdminDatos.stockpor(lista,"warehouse_area"))
    else:
        print("Opcion invalida")

elif opcion_principal == '2':
    listaven=AdminDatos.alerta_vencimiento_stock(lista)
    print("Los siguientes lotes estan vencidos: ",listaven)
elif opcion_principal == '3':
    AdminDatos.busca_lote(lista)
else:
    print("Opcion invalida")
