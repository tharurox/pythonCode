class product():
    categoryCodes = ["GR", "HB", "CF", "EL", "HL", "OT"]
    categoryNames = ["Groceries", "Health & Beauty", "Clothing & Footwear", "Electronics", "Home & Living", "Others"]

    
    def __init__(self, product_id,category_name_of_product, product_name, quantity, price):
        self.product_id = product_id            
        self.category_name_of_product = category_name_of_product
        self.product_name: str = product_name   
        self.quantity = quantity 
        self.price = price

