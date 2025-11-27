import csv
from lotes import Lotes
from datetime import datetime, timedelta, date
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

    def alerta_vencimiento_stock(self, dias_alerta: int) -> str:
        try:
            fecha_vencimiento = datetime.strptime(self.expiry_date, '%d-%m-%Y').date() #convierte la cadena self.expiry_date a date
        except ValueError:
            return f" ERROR en Lote {self.batch_code}: Formato de fecha incorrecto ({self.expiry_date})."
        
        fecha_actual = date.today()
        
        diferencia_tiempo = fecha_vencimiento - fecha_actual   #calcular los días restantes
        dias_restantes = diferencia_tiempo.days
            
        if dias_restantes <= dias_alerta:
            return f" ALERTA: Lote {self.batch_code} ({self.item_name}) vence en {dias_restantes} días. Stock: {self.current_stock}."   #vencimiento próximo
            
        else:
            return f" OK: Lote {self.batch_code} tiene vigencia suficiente."   #vigencia suficiente
    def stockpor(lista,parametro): #muestra el stock dependiendo del parametro que haya elegido el cliente

        stock={} #se guarda en este diccionario
        for lis in lista:
            clave=getattr(lis,parametro) #en el main se debe hacer un menú que llame el metodo 'parametro' debe ser un string identico al nombre del atributo del objeto
            if clave in stock: #si el parametro no esta en la lista se crea info en el diccionario, si ya existe solo se suma.abs
                stock[clave]+=int(lis.current_stock) if lis.current_stock.strip() != "" else 0
            else:
                stock[clave]=int(lis.current_stock) if lis.current_stock.strip() != "" else 0
        return stock
    @staticmethod
    def especifico_lote(lista, batch_code=None):
        if not lista:
            print("no hay lotes que buscar")
            return []
        if batch_code:

            resultado = []
            batch_code_lower = batch_code.lower().strip()
            for  lote in lista:
                lote_batch_code = str(lote.batch_code).lower() if lote.batch_code else ""
                if batch_code_lower in lote_batch_code:
                    resultado.append(lote)
            if resultado:
              print(f"se encontraron {len(resultado)} informacion,del lote { batch_code}: ")
              AdminDatos.mostrar(resultado)

              print(f"todos los lotes {len(resultado)} lotes encontrados")
            else:
              print(f"no se encotraron lotes : {batch_code}")
            return []
        else:
         print(f"se encontraron lotes: {len(lista)}")
         AdminDatos.mostrar(lista)
         print(f"se muestra todo los {len(lista)} lotes en total:")
         return lista
    @staticmethod  
    def busca_lote(self):
        print("datos por:Todos los datos/ especifico")

        if not self.lote:
            print("mostrar todos los datos")
            print("buscar lote espefico")

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
