

class Treasure:
    size = 0

    def __init__(self, val=None):
        self.value = val
        self.collection = 1
        self.depth = 1
        
        if (self.value != None):
            self.left = Treasure()
            self.right = Treasure()
        else: 
            self.left = None
            self.right = None
    
    def add_treasure(self, val):
        self.size += 1
        if (self.value == None):
            self.value = val
            self.left = Treasure()
            self.right = Treasure()
        else:
            if (val < self.value):
                self.left.depth = self.depth + 1
                self.left.add_treasure(val)
            elif (val > self.value):
                self.right.depth = self.depth + 1
                self.right.add_treasure(val)
            else:
                self.collection += 1

    def print_all(self):
        if (self.value != None):
            self.left.print_all()
            print("value: ", self.value, ", depth: ", self.depth, ", collection: ", self.collection, ".\n", sep="", end="")
            self.right.print_all()

    def price_table(self):
        if (self.value != None):
            self.left.price_table()
            print("treasure value: ", self.value, "\tcollection: ", self.collection, "\tprice: ", self.price(), sep="",)
            self.right.price_table()

    def buy_treasure(self, val):
        if (self.value == None):
            return
        if (self.value == val):
            if (self.collection > 0):
                price = self.price()
                if (price >= 30 & price <= 120):
                    print(chr(price), end="")
                self.collection -= 1
                return price
            else:
                return
        elif (self.value > val):
            self.left.buy_treasure(val)
        elif (self.value < val):
            self.right.buy_treasure(val)

    def price(self):
        if (self.value == None):
            return
        base_price = self.value * 2
        collection_charge = self.depth * 0.5
        package_charge = self.value / 20
        charge = int(base_price + collection_charge + package_charge)
        if (charge >= 80 and charge < 110):
            charge -= 2
        elif (charge >= 110 and charge < 120):
            charge -= 5
        elif (charge >= 120 and charge < 140):
            charge -= 16
        elif (charge >= 140):
            charge -= 30
        return charge

    def dig_treasure(self):
        for i in range(50, 55):
            self.add_treasure(i - 3)
            self.add_treasure(i)

        for i in range(43, 48):
            self.add_treasure(i)
            self.add_treasure(i + 5)

        for i in range(5, 15):
            self.add_treasure(i)

        for i in range(60, 70):
            self.add_treasure(i)

        for i in range(23, 33):
            self.add_treasure(i)
            self.add_treasure(50 - i)

        for i in range(55, 60):
            self.add_treasure(i)

        for i in range(45, 55):
            self.add_treasure(i + 10)

        for i in range(77, 83):
            self.add_treasure(i)

treasure_tree = Treasure()
treasure_tree.dig_treasure()
# treasure_tree.price_table()
# treasure_tree.print_all()

shopping_list = [12, 31, 50, 90, 58, 9, 54, 55, 7, 8, 13, 43, 66, 102, 13, 98, 67, 58, 1, 49]

for treasure in shopping_list:
    treasure_tree.buy_treasure(treasure)

"""3,  """
