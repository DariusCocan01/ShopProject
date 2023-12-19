from Categories import *
from CreateTheProduct import *
import json
import os

class Product:
    def create_all_the_products():
        x = CreateTheProduct
        allProducts = []
        for i in range(0,100):
            type = x.makeTheTypeOfProduct()
            if(type==Sneakers or type == Boots or type == Loafers):
                size = x.makeTheSizeForShoes()
            else:
                size = x.makeTheSize()
            brand = x.makeTheBrand()
            price = x.makeThePrice(100,500)
            allProducts.append(type(brand = brand, size = size, price = price))
        return allProducts

class SavingProcess:
    def create_and_save():
        products = Product.create_all_the_products()
        with open("products.json", "w") as json_file:
            json.dump([product.to_dict() for product in products], json_file, indent=2)
        return products
    def verify_if_json_exists():
        file_path = "products.json"
        if not os.path.exists(file_path):
            x = SavingProcess.create_and_save()
        else:
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
            x = []
            for obj_data in data:
                obj_type = obj_data.get('type')
                obj_brand = obj_data.get('brand')
                obj_size = obj_data.get('size')
                obj_price = obj_data.get('price')
                class_mapping = {
                    'Slim_Jeans': Slim_Jeans,
                    'Regular_Jeans': Regular_Jeans,
                    'Oversized_Jeans': Oversized_Jeans,
                    'Crewneck_TShirt': Crewneck_TShirt,
                    'Vneck_TShirt': Vneck_TShirt,
                    'Long_Sleeve_TShirt': Long_Sleeve_TShirt,
                    'Bomber_Jackets': Bomber_Jackets,
                    'Leather_Jackets': Leather_Jackets,
                    'Denim_Jackets': Denim_Jackets,
                    'Maxi_Dresses': Maxi_Dresses,
                    'Cocktail_Dresses': Cocktail_Dresses,
                    'Sundresses': Sundresses,
                    'Sneakers': Sneakers,
                    'Boots': Boots,
                    'Loafers': Loafers,
                    'Crewneck_Sweaters': Crewneck_Sweaters,
                    'Turtleneck_Sweaters': Turtleneck_Sweaters,
                    'Cardigans': Cardigans,
                }
                if obj_type in class_mapping:
                # Use the mapping to create an instance of the corresponding class
                    obj_instance = class_mapping[obj_type](brand=obj_brand, size=obj_size, price=obj_price)
                    x.append(obj_instance)
                else:
                    print(f"Unknown type: {obj_type}")
        return x
    def remove_element(index):
        aux = index -1
        file_path = "products.json"
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        if 0 <= aux < len(data):
            removed_element = data.pop(aux)
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=2)
        else:
            print(f"Index {aux} is invalid.")