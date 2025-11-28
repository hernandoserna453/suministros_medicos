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
    
    def alerta_vencimiento_stock(lista): #muestra los lotes que van a vencer en los proximos 30 dias
        hoy = date.today()
        fecha_limite = hoy + timedelta(days=30)
        lotes_vencidos = []

        for lote in lista:
            if lote.expiry_date and lote.expiry_date.strip() != "":
                try:
                    fecha_expiracion = datetime.strptime(lote.expiry_date, "%Y/%m/%d").date() #el formato de fecha estaba mal, se corrigió con /
                    if fecha_expiracion<hoy: #aca compara con la fecha hoy, las fechas menores estan vencidas
                        lotes_vencidos.append(lote.batch_code)
                except ValueError:
                    print(f"Formato de fecha inválido para el lote {lote.batch_code}: {lote.expiry_date}")

        return lotes_vencidos

    
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
    def busca_lote(lista):  # Función encargada de buscar por batch_code
        print("Datos por: Todos los datos / específico")
        
        # Verifica si la lista de lotes está vacía
        if not lista:
            print("Mostrar todos los datos")
            return  # Salimos si no hay lotes disponibles

        # Sub menú para elegir si mostrar todo o solamente un lote específico
        opcion = input("Seleccione 1 para mostrar todos los lotes o 2 para buscar un lote específico: ")
        if opcion:
            if opcion == "1":
                AdminDatos.mostrar(lista)
            elif opcion == "2":
                batch_code ="Lote-"+ input("Ingrese el lote a buscar: ").strip()
                if not batch_code:
                    print("Ingrese un lote correcto")
                    return
                AdminDatos.mostrar(lista, batch_code)
            else:
                print("Opción no válida")

    @staticmethod
    def mostrar(lotes, batch_code=None):
        for obj in lotes:
            if batch_code is None or obj.batch_code == batch_code:
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
