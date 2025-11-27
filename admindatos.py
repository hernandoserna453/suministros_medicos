import csv
from lotes import Lotes
from datetime import datetime
class AdminDatos: #admindatos es para modificar o mostrar datos, aqui Felipe debe agregar el metodo que borra los objetos que tengan fechas vacias
    @staticmethod
    def leer_csv(ruta): #Esto es para leer el archivio csv y transformamrlo en una lista de objetos Lotes
        objetos = []
        with open(ruta,encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                obj=Lotes(**fila) #El **fila automatiza los atributos para llamar la clase
                objetos.append(obj) #acá se añade el objeto a la lista
        return objetos
    @staticmethod
    def mostrar(lista): #este metodo es mas que nada para comprobar si el programa funcionaba
        for obj in lista[:5]:
            print(f"ID: {obj.item_id}")
            print(f"Nombre: {obj.item_name}")
            print(f"Categoría: {obj.category}")
            print(f"Lote: {obj.batch_code}")
            print(f"Recibido: {obj.received_date}")
            print(f"Expira: {obj.expiry_date}")
            print(f"Área: {obj.warehouse_area}")
            print(f"Stock actual: {obj.current_stock}")
            print(f"Stock mínimo: {obj.min_stock}")
            print(f"Costo unitario: {obj.unit_cost}")
            print(f"Proveedor: {obj.supplier}")
            print(f"Estado: {obj.status}")
            print("-" * 40)
    def stockpor(lista,parametro): #muestra el stock dependiendo del parametro que haya elegido el cliente

        stock={} #se guarda en este diccionario
        for lis in lista:
            clave=getattr(lis,parametro) #en el main se debe hacer un menú que llame el metodo 'parametro' debe ser un string identico al nombre del atributo del objeto
            if clave in stock: #si el parametro no esta en la lista se crea info en el diccionario, si ya existe solo se suma.abs
                stock[clave]+=int(lis.current_stock) if lis.current_stock.strip() != "" else 0
            else:
                stock[clave]=int(lis.current_stock) if lis.current_stock.strip() != "" else 0
        return stock