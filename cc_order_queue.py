class Queue:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)

    
class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
          
    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops >= 1 and scoops <= 3:
            order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
            self.orders.enqueue(order)
            print("Order created!")
        elif flavor not in self.flavors:
            print("Sorry, we don't have that flavor!")
        elif scoops is not(scoops >= 1 and scoops <= 3):
            print("Choose 1 - 3 scoops!")
        
    def show_all_orders(self):
        print("")
        print("All Pending Ice Cream Orders:")
        for queue_list in self.orders.items:
            print("Customer: ", queue_list.get("Customer"), "-- Flavor: ", queue_list.get("Flavor"), "-- Scoops: ", queue_list.get("Scoops"))

    def next_order(self):
        print("")
        print("Next Order Up!")
        next_order = self.orders.dequeue()
        print("Customer: ", next_order.get("Customer"), "-- Flavor: ", next_order.get("Flavor"), "-- Scoops: ", next_order.get("Scoops"))
        

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()