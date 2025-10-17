class Product:
    categoryCodes = ["GR", "HB", "CF", "EL", "HL", "OT"]
    categoryNames = ["Groceries", "Health & Beauty", "Clothing & Footwear",
                     "Electronics", "Home & Living", "Others"]

    def __init__(self, product_id=None, product_name="", quantity=0, price=0.0):
        self._product_id = None
        self._category_name_of_product = ""
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        if product_id is not None:
            self.set_product_id(product_id)

    def get_product_id(self):
        return self._product_id

    def set_product_id(self, product_id):
        s = str(product_id)
        code = s[:2].upper()
        number_part = s[2:]

        if code in Product.categoryCodes:
            final_code = code
            idx = Product.categoryCodes.index(code)
            cat_name = Product.categoryNames[idx]
        else:
            final_code = "OT"
            cat_name = "Others"

        self._product_id = self._product_id = final_code + number_part
        self._category_name_of_product = cat_name


    def category_name_of_product(self):
        return self._category_name_of_product

    def __str__(self):
        return (f"Product ID: {self._product_id}   |   "
                f"Category: {self._category_name_of_product}   |   "
                f"Name: {self.product_name}   |   "
                f"Quantity: {self.quantity}   |   "
                f"Price: ${self.price:.2f}")
    
    def display_introduction(self):
        NAME = "Tharaka Ravishan"
        STUDENT_ID = "n11849622"
        GREETING = "Hello, welcome to my program!"
        print("****************************************")
        print("Name: " + NAME)
        print("Student ID: " + STUDENT_ID)
        print(GREETING)
        print("****************************************")

    def input_value(minValue,maxValue):
        input_val = input("Enter an Integer between : " + str(minValue) + "and" + str(maxValue))
        value=int(input_val)
        if minValue <= value <= maxValue:
            return value
        else: 
            print("Value is out of range")
    

    def is_valid(product_id):
        input_string = str(product_id).strip()
        if len(input_string) == 5:
            firstTwo_letrs = input_string[:2]
            lastThree_ltrs = input_string[2:]
            return firstTwo_letrs.isalpha() and firstTwo_letrs.isupper() and lastThree_ltrs.isdigit()
        
    def get_product_data(n):
        products = []

        i = 0
        while i <= n:
            print("Enter Details of the product:")



if __name__ == "__main__":
    
    p4 = Product()
    print(p4.display_introduction())

    p1 = Product()
    print("Default product:")
    print(p1)

    p2 = Product("EL205", "Bluetooth Speaker", 1, 49.99)
    print("\nValid code example:")
    print(p2)

    p3 = Product("ZZ101", "Unknown Widget", 5, 12.5)
    print("\nUnknown code rewritten to OT:")
    print(p3)