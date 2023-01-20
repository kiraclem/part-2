import csv

from pprint import pprint

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv('sample.csv')



def add_to_dictionary(self):
    
    cupcake_dictionary = {
        "size": self.size,
        "name": self.name,
        "price": self.price,
        "flavor": self.falvor,
        "frosting": self.frosting,
        "sprinkles": self.sprinkles,
        "filling": self.filling
    }
 




# from abc import ABC

# class Cupcake(ABC):
#     size = 'regular'
#     def __init__ (self, name, price, flavor, frosting, gluten_free):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.sprinkles = []
#         self.gluten_free = gluten_free

#     def add_sprinkles(self, *args):
#         for sprinkle in args:
#             self.sprinkles.append(sprinkle)

#     @abstractmethod
#     def calculate_price(self, quantity):
#         return self.price * quantity

class Cupcake():
    size = 'regular'
    def __init__ (self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    def calculate_price(self, quantity):
        return self.price * quantity

class Mini(Cupcake):
    size = 'mini'

class Large(Cupcake):
    size = 'large'

# sprinkles and gluten_free are boolen values. aka True or False.

cupcake_1 = Cupcake("vanilla cupcake", 3.29, "vanilla", "vanilla", "cream")
cupcake_1.add_sprinkles('rainbow', 'vanilla', 'chocolate')
cupcake_2 = Cupcake("chocolate cupcake", 3.29, "chocolate", "chocolate", "chocolate")
cupcake_3 = Cupcake("Cake cupcake", 3.59, "vanilla", "cake frosting","none")
cupcake_4 = Cupcake("cookies and cream", 3.59, "chocolate", "vanilla oreo", "oreo cream")


print(cupcake_4.flavor)

print('===================')

mini_cupcake_1 = Mini("mini vanilla cupcake", 2.29, "vanilla", "vanilla", "cream")
print(mini_cupcake_1.filling)
print(mini_cupcake_1.frosting)
print(mini_cupcake_1.name)

print('===================')

#showing how to get rid of class attribute from Parent class. 
# just dont specify class attribute




class Mini(Cupcake):
    size = 'mini'
    def __init__ (self, name, price, flavor, frosting, gluten_free):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []


# WILL NOW GIVE AN ERROR SINCE GLUTEN FREE NO LONGER EXSISTS IN THE CLASS.

# mini_cupcake_1 = Mini("mini vanilla cupcake", 2.29, "vanilla", "vanilla", False)
# print(mini_cupcake_1.filling)


cupcake_list = [
    cupcake_1,
    cupcake_2,
    cupcake_3,
    cupcake_4,
    mini_cupcake_1
]

def prettier_sprinkle(self):
    for sprinkle in self.sprinkles:
        print(sprinkle)


sprinkle = prettier_sprinkle(cupcake_1)

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size","name","price","flavor","frosting","sprinkles","filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({ "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                writer.writerow({ "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


# REWRITES FILE!!
write_new_csv("sample.csv", cupcake_list)



def add_to_csv(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size","name","price","flavor","frosting","sprinkles","filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader() no longer need to write a header anymore.

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({ "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles, "filling": cupcake.filling})
            else:
                writer.writerow({ "size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})



# original text: regular,Stars and Stripes,2.99,Vanilla,Vanilla,"['Red', 'White', 'Blue', 'Chocolate']",Chocolate
# mini,Oreo,0.99,Chocolate,Cookies and Cream,['Oreo pieces'],
# large,Red Velvet,3.99,Red Velvet,Cream Cheese,[],
# regular,Triple Chocolate,2.99,Chocolate,Chocolate,[],Chocolate
# regular,Strawberry,2.99,Stawberry,Vanilla,[],