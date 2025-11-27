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
    def especifico_lote(lista, batch_code=None): # FUNCION LOTES
        if not lista:
            print("no hay lotes que buscar")
            return []
        if batch_code:
            # ESPECIFICAR LOTE
            resultado = []

            batch_code_lower = batch_code.lower().strip()
            for  lote in lista:
                lote_batch_code = str(lote.batch_code).lower() if lote.batch_code else ""
                if batch_code_lower in lote_batch_code:
                    resultado.append(lote)
            #Mostrar todos los datos  
            if resultado:
              print(f"se encontraron {len(resultado)} informacion,del lote { batch_code}: ")
              #muestra  los datos especificos
              AdminDatos.mostrar(resultado)
            
              print(f"todos los lotes {len(resultado)} lotes encontrados")

              #datos especificos

            else:
              print(f"no se encotraron lotes : {batch_code}")
            return []
        else:
         print(f"se encontraron lotes: {len(lista)}")
         #muestra los objeto de clase lotes
         AdminDatos.mostrar(lista)
         print(f"se muestra todo los {len(lista)} lotes en total:")
         return lista
    @staticmethod  
    def busca_lote(self): #Funcion encarga de buscar por bach_code
        print("datos por:Todos los datos/ especifico")
        #condicion cumplida

        if not self.lote:
            print("mostrar todos los datos")
            print("buscar lote espefico")

        #sub menu para elegir si mostrar todo o solamente un lote especifico

        opcion = input("seleccione 1 -2")

        if opcion:
            if opcion  == "1":
                AdminDatos.mostrar(self.lote)
            elif opcion == "2":
                batch_code = input(f"ingrese el lute a buscar:").strip()
                if not batch_code:
                    print("ingrese un lote correcto")
                    return
                AdminDatos.mostrar(self.lote, batch_code)
            else:
                print("opcion no valida")

    @staticmethod
    def eliminar_fechas_vacias(lista):
        
        #datos encargados para uso de(csv)
        inicial = len(lista)
        lista_filtrada = []
        #elimina vacios de fecha
        for obj in lista:
            fecha_recibido_vacia = not obj.received_date or obj.received_date.strip() == ''
            fecha_expiracion_vacia = not obj.expiry_date or obj.expiry_date.strip() == ''
            
           
            if not fecha_recibido_vacia and not fecha_expiracion_vacia:
                lista_filtrada.append(obj)#añade cambios

        #datos eliminados
        eliminados = inicial - len(lista_filtrada)
        print(f"Se eliminaron {eliminados} registros con fechas vacías")
        return lista_filtrada, eliminados
    
    @staticmethod
    #se elimina todos los vacios de todo el archivo
    def limpiar_registros_completamente_vacios(lista):
      #datos encargados de (csv)
        inicial = len(lista)
        #lista eliminar vacios
        lista_filtrada = []
        

        for obj in lista:
         #criterios 
            campos = [
                obj.item_id, obj.item_name, obj.category, obj.batch_code,
                obj.received_date, obj.expiry_date, obj.warehouse_area,
                obj.current_stock, obj.min_stock, obj.unit_cost,
                obj.supplier, obj.status
            ]
            
            
            if all(campo is not None and str(campo).strip() != '' for campo in campos):
                lista_filtrada.append(obj)
        #eliminacion
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
