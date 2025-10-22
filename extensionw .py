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

        self._product_id = final_code + number_part
        self._category_name_of_product = cat_name


    def category_name_of_product(self):
        return self._category_name_of_product

    def __str__(self):
        return ("Product ID: " + str(self._product_id) + "   |   "
            "Category: " + self._category_name_of_product + "   |   "
            "Name: " + self.product_name + "   |   "
            "Quantity: " + str(self.quantity) + "   |   "
            "Price: $" + "{:.2f}".format(self.price))
    
def display_introduction():
    NAME = "Tharaka Ravishan"
    STUDENT_ID = "n11849622"
    GREETING = "Hello, welcome to my program!"
    print("****************************************")
    print("Name: " + NAME)
    print("Student ID: " + STUDENT_ID)
    print(GREETING)
    print("****************************************")

def input_value(minValue,maxValue):
    while True:
        inputValue = input("Enter an integer between " + str(minValue) + " and " + str(maxValue) + ": ").strip()
        val = int(inputValue)
        if minValue <= val <= maxValue:
            return val
        else:
            print("Out of range. Please try again.")
       

def is_valid(product_id):
    inputString = str(product_id)
    if len(inputString) == 5:
        firstTwo_letrs = inputString[:2]
        lastThree_ltrs = inputString[2:]
        if firstTwo_letrs.isupper() and lastThree_ltrs.isdigit():
            return True
        else:
            return False
            
def get_product_data(n):
    product = [] 
    for i in range(1,n+1):
        print ("Enter Product Number " + str(i))
        while True:
            product_id = input("Product Id ")           
            if is_valid(product_id):
                break   
            else:
                print("Invalid Product ID given")
            
        name = input("Product Name: ")                  
        print("Quantity (1-50)")
        quantity_value= input_value(1,50)

        while True:
            inputPrice = input("Unit price: ").strip()
            price = float(inputPrice)
            if price >= 0:
                break
            else:
                print("invlid price ")
        
        p = Product()
        p.set_product_id(product_id)     
        p.product_name = name
        p.quantity = quantity_value
        p.price = price
        product.append(p)

    return product


def save_products_to_file(filename, products):
    with open(filename, "w", encoding="utf-8") as f:
        for p in products:
            f.write(f"{p.get_product_id()},{p.product_name},{p.quantity},{p.price}\n")
    print(f"Saved products to {filename}")

def load_products_from_file(filename):
    products = []
    f = open(filename, "r")

    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 4:
            pid = parts[0].strip()
            name = parts[1].strip()
            quantitytext = parts[2].strip()
            pricetext = parts[3].strip()

            if quantitytext.isdigit():
                quantiry_value = int(quantitytext)
            else:
                quantiry_value = 0

            price = float(pricetext)

            p = Product()
            p.set_product_id(pid)   
            p.product_name = name
            p.quantity = quantiry_value
            p.price = price
            products.append(p)

    f.close()
    print("Loaded " + str(len(products)) + " product(s) from " + filename)
    return products

def get_product_lists(products):
    print("Available categories:")
    for i in range(len(Product.categoryCodes)):
        print(Product.categoryCodes[i] + " - " + Product.categoryNames[i])

    while True:
        code = input("Enter a category code (or '!' to stop): ")
        if code == "!":
            break
        else:
            print("Products in category " + code + ":")
            total_quantity = 0
            total_value = 0.0

        for p in products:
            productID = p.get_product_id()
            if productID[:2].upper() == code:
                print(p)
                quantity_available = int(p.quantity)      
                price_num = float(p.price)    
                total_quantity = total_quantity + quantity_available
                total_value = total_value + (quantity_available * price_num)

        print("Total quantity: " + str(total_quantity))
        print("Total value: $" + str(round(total_value, 2)))

def display_all_products(products):
    for p in products:
        print(p)

def main():

    display_introduction()
    print("How many products do you want? (1 to 40)")
    amount = input_value(1, 40)
    items = get_product_data(amount)
    save_products_to_file("Ranathunga_Product.txt", items)
    print("View by category (enter '!' to stop):")
    get_product_lists(items)
    load_products = load_products_from_file("Ranathunga_Product.txt")
    display_all_products(load_products)

if __name__ == '__main__':
    main()
