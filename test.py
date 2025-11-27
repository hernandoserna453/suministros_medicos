from admindatos import AdminDatos

lista=AdminDatos.leer_csv("dataset3_clinical_supplies_inventory.csv")
AdminDatos.mostrar(lista)

print("Ejemplo de stock por warehouse")
print(AdminDatos.stockpor(lista,"warehouse_area"))