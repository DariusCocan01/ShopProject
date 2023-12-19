import random
from Categories import *
class CreateTheProduct:    
    def makeThePrice(a: int, b: int):
        return random.randrange(a,b) 
    def makeTheBrand() -> str:
        brands = ["Nike","Adidas","Gucci","Zara","H&M","Levi's","Calvin Klein","Puma","Tommy Hilfiger","Ralph Lauren","Versace","Under Armour","Prada","Chanel","Balenciaga","Fendi","Dior","Yves Saint Laurent","Armani","Gap"]
        return random.choice(brands)
    def makeTheSize() -> str:
        sizes = ["XS","S","M","L","XL","XXL"]
        return random.choice(sizes)
    def makeTheSizeForShoes() -> str:
        sizes = ["36","36.5","37","37.5","38","38.5","39","39.5","40","40.5","41","41.5","42","42.5","43","43.5","44","44.5","45","45.5","46"]
        return random.choice(sizes)
    def makeTheTypeOfProduct():
        cat = [Regular_Jeans,Slim_Jeans,Oversized_Jeans,Crewneck_TShirt,Vneck_TShirt,Long_Sleeve_TShirt,Bomber_Jackets,Leather_Jackets,Denim_Jackets,Maxi_Dresses,Cocktail_Dresses,Sundresses,Sneakers,Boots,Loafers,Cardigans,Crewneck_Sweaters,Turtleneck_Sweaters]
        return random.choice(cat)