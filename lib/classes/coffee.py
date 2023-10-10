from statistics import mean


class Coffee:


    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total = [order.price for order in self.orders() if order.coffee is self]
        return mean(total) if len(total) else 0