class Lotes:
    def __init__(self,item_id,item_name,category,batch_code,received_date,expiry_date,warehouse_area,current_stock,min_stock,unit_cost,supplier,status):
        self.item_id=item_id
        self.item_name=item_name
        self.category=category
        self.batch_code=batch_code
        self.received_date=received_date
        self.expiry_date=expiry_date
        self.warehouse_area=warehouse_area  #Aqui estamos declarando el constructor para despues crear los objetos facilmente
        self.current_stock=current_stock
        self.min_stock=min_stock
        self.unit_cost=unit_cost
        self.supplier=supplier
        self.status=status