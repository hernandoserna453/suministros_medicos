from admindatos import AdminDatos

lista=AdminDatos.leer_csv("dataset3_clinical_supplies_inventory.csv")
AdminDatos.mostrar(lista)