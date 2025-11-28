import csv
from datetime import datetime, timedelta, date
# La línea 'from prueba import Lotes' no es necesaria si la clase está definida aquí.

class Lotes:
    def __init__(self, item_id, item_name, category, batch_code, received_date, expiry_date, warehouse_area, current_stock, min_stock, unit_cost, supplier, status):
        # El constructor espera estos 12 argumentos
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.batch_code = batch_code
        self.received_date = received_date
        self.expiry_date = expiry_date  # Cadena en formato 'dd-mm-yyyy'
        self.warehouse_area = warehouse_area
        self.current_stock = current_stock
        self.min_stock = min_stock
        self.unit_cost = unit_cost
        self.supplier = supplier
        self.status = status

    # 🚨 ESTE MÉTODO DEBE ESTAR INDENTADO DENTRO DE LA CLASE 🚨
    def alerta_vencimiento_stock(self, dias_alerta: int) -> str:
        try:
            # Convierte la cadena self.expiry_date a date
            fecha_vencimiento = datetime.strptime(self.expiry_date, '%d-%m-%Y').date() 
        except ValueError:
            return f"❌ ERROR en Lote {self.batch_code}: Formato de fecha incorrecto ({self.expiry_date})."
        
        fecha_actual = date.today()
        
        # Calcular los días restantes
        diferencia_tiempo = fecha_vencimiento - fecha_actual
        dias_restantes = diferencia_tiempo.days
            
        if dias_restantes <= dias_alerta:
            
            # Vencimiento próximo (cubre vencidos y próximos)
            return f"⚠️ ALERTA: Lote {self.batch_code} ({self.item_name}) vence en {dias_restantes} días. Stock: {self.current_stock}." 
            
        else:
            # Vigencia suficiente
            return f"✅ OK: Lote {self.batch_code} tiene vigencia suficiente."
    
# --- Fin de la clase Lotes ---
# ----------------------------------------------------------------------

DIAS_UMBRAL = 60 # Definimos el umbral de alerta

# NOTA: Los 12 argumentos deben pasarse en el orden definido en __init__

# Caso 1: Alerta Próxima (días_restantes <= 60)
lote_alerta = Lotes(
    item_id="202", 
    item_name="Alcohol", 
    category="Desinfectante", 
    batch_code="L200", 
    received_date="15-10-2025", 
    expiry_date="20-01-2026", 
    warehouse_area="B2", 
    current_stock=50, 
    min_stock=10, 
    unit_cost=5.0, 
    supplier="QuimicaX", 
    status="Activo"
)

# Caso 2: Vigencia Suficiente (días_restantes > 60)
lote_seguro = Lotes(
    item_id="303", 
    item_name="Guantes", 
    category="EPI", 
    batch_code="L300", 
    received_date="20-11-2025", 
    expiry_date="01-03-2026", 
    warehouse_area="C3", 
    current_stock=1000, 
    min_stock=200, 
    unit_cost=0.1, 
    supplier="Suplimed", 
    status="Activo"
)

# Caso 3: Vencido (Se prueba con la misma lógica simple, resultará en días negativos)
lote_vencido = Lotes(
    item_id="101", 
    item_name="Mascarillas", 
    category="EPI", 
    batch_code="L100", 
    received_date="01-05-2025", 
    expiry_date="01-11-2025", 
    warehouse_area="A1", 
    current_stock=200, 
    min_stock=50, 
    unit_cost=0.5, 
    supplier="Suplimed", 
    status="Activo"
)

print("--- REPORTE DE PRUEBA DE VENCIMIENTO ---")
print(lote_alerta.alerta_vencimiento_stock(DIAS_UMBRAL))
print(lote_seguro.alerta_vencimiento_stock(DIAS_UMBRAL))
print(lote_vencido.alerta_vencimiento_stock(DIAS_UMBRAL))