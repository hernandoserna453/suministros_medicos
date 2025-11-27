
print("Elige una opcion para gestionar los suministro:")
print("1. Buscar por stock:")
print("2. Alerta de stock por vencer")
print("3. Buscar por lote")
      
opcion_principal = int(input("Selecciona la opcion principal:"))
    if opcion_principal == '1':
 
        print("Busquedas por stock:")
        print("a. Stock por distribuidor")
        print("b. Stock por estado")
        print("c. Stock por mes recibido")
        print("d. Stock por item")
        print("e. Stock por categoria")
        print("f. Stock por bodega")

        opcion_stock = str(input("Elige una opcion por stock:"))
        if opcion_stock == 'a':
            if opcion_stock == 'b':
            elif opcion_stock == 'c':
            elif opcion_stock == 'd':
            elif opcion_stock == 'e':
            elif opcion_stock == 'f':
        else:
            print("Opcion invalida")

        elif opcion_principal == '2':
        elif opcion_principal == '3':
        else print("Opcion invalida")
