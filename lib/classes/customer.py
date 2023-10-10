class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 15:
            self._name = name
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        from classes.order import Order
        return Order(self, coffee, price)
    