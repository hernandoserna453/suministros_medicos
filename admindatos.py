import csv
from lotes import Lotes
from datetime import datetime
class AdminDatos: #admindatos es para modificar o mostrar datos, aqui Felipe debe agregar el metodo que borra los objetos que tengan fechas vacias
  
    @staticmethod
    def mostrar(lista):
        for obj in lista:
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
    
    @staticmethod
    def eliminar_fechas_vacias(lista):
        
        inicial = len(lista)
        lista_filtrada = []
        
        for obj in lista:
            fecha_recibido_vacia = not obj.received_date or obj.received_date.strip() == ''
            fecha_expiracion_vacia = not obj.expiry_date or obj.expiry_date.strip() == ''
            
           
            if not fecha_recibido_vacia and not fecha_expiracion_vacia:
                lista_filtrada.append(obj)
        
        eliminados = inicial - len(lista_filtrada)
        print(f"Se eliminaron {eliminados} registros con fechas vacías")
        return lista_filtrada, eliminados
    
    @staticmethod
    def limpiar_registros_completamente_vacios(lista):
      
        inicial = len(lista)
        lista_filtrada = []
        
        for obj in lista:
         
            campos = [
                obj.item_id, obj.item_name, obj.category, obj.batch_code,
                obj.received_date, obj.expiry_date, obj.warehouse_area,
                obj.current_stock, obj.min_stock, obj.unit_cost,
                obj.supplier, obj.status
            ]
            
            
            if all(campo is not None and str(campo).strip() != '' for campo in campos):
                lista_filtrada.append(obj)
        
        eliminados = inicial - len(lista_filtrada)
        print(f"✅ Se eliminaron {eliminados} registros completamente vacíos/inválidos")
        return lista_filtrada, eliminados  
    

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
        for obj in lista:
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

ruta = r"C:\Users\Aprendiz\Desktop\luis\suministros_medicos"