from abc import ABC, abstractmethod

class Categories(ABC):
    def get_description(self) -> None:
        raise NotImplementedError
    def to_dict(self):
        # Creează un dicționar care conține toate atributele obiectului
        product_dict = self.__dict__
        # Adaugă și tipul obiectului în dicționar
        product_dict["type"] = self.__class__.__name__
        return product_dict
class Jeans(Categories):
    def get_description(self) -> None:
        raise NotImplementedError
    
class Slim_Jeans(Jeans):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Slim Jeans(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Slim Jeans size {self.size} having the price {self.price}$"
    
class Regular_Jeans(Jeans):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Regular Jeans(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Regular Jeans size {self.size} having the price {self.price}$"
    
class Oversized_Jeans(Jeans):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Oversized Jeans(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Oversized Jeans size {self.size} having the price {self.price}$"
    

class TShirts(Categories):
    def get_description(self) -> None:
        raise NotImplementedError 
    
class Crewneck_TShirt(TShirts):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Crewneck T-Shirt(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Crewneck T-Shirt size {self.size} having the price {self.price}$"

class Vneck_TShirt(TShirts):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"V-neck T-Shirt(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} V-neck T-Shirt size {self.size} having the price {self.price}$"

class Long_Sleeve_TShirt(TShirts):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Long Sleeve T-Shirt(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Long Sleeve T-Shirt size {self.size} having the price {self.price}$"
    
class Jackets(Categories):
    def get_description(self) -> None:
        raise NotImplementedError 
    
class Bomber_Jackets(Jackets):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Bomber Jackets(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Bomber Jackets size {self.size} having the price {self.price}$"

class Leather_Jackets(Jackets):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Leather Jackets(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Leather Jackets size {self.size} having the price {self.price}$"

class Denim_Jackets(Jackets):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Denim Jackets(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Denim Jackets size {self.size} having the price {self.price}$"
    
class Dresses(Categories):
    def get_description(self) -> None:
        raise NotImplementedError

class Maxi_Dresses(Dresses):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Maxi Dresses(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Maxi Dresses size {self.size} having the price {self.price}$"
    
class Cocktail_Dresses(Dresses):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Cocktail Dresses(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Cocktail Dresses size {self.size} having the price {self.price}$"

class Sundresses(Dresses):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Sundresses(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Sundresses size {self.size} having the price {self.price}$"

class Shoes(Categories):
    def get_description(self) -> None:
        raise NotImplementedError
class Sneakers(Shoes):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Sneakers(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Sneakers size {self.size} having the price {self.price}$"
    
class Boots(Shoes):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Boots(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Boots size {self.size} having the price {self.price}$"
    
class Loafers(Shoes):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Loafers(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Loafers size {self.size} having the price {self.price}$"

class Sweaters(Categories):
    def get_description(self) -> None:
        raise NotImplementedError
    
class Crewneck_Sweaters(Sweaters):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Crewneck Sweaters(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Crewneck Sweaters size {self.size} having the price {self.price}$"

class Turtleneck_Sweaters(Sweaters):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Turtleneck Sweaters(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Turtleneck Sweaters size {self.size} having the price {self.price}$"
    
class Cardigans(Sweaters):
    def __init__(self, size: str, price: int, brand: str):
        self.brand = brand
        self.size=size
        self.price = price
    def __repr__(self) -> str:
        return f"Cardigans Sweaters(\"{self.size}\", {self.price})"
    def get_description(self) -> str:
        return f"{self.brand} Cardigans Sweaters size {self.size} having the price {self.price}$"