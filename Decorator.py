import Pizza

class Decorator(Pizza.Pizza):

   def __init__(self, cost, description):
       self.cost = cost
       self.description = description
       
   def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)


   def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)
    
class Zeytin(Decorator):

    def __init__(self):
       self.cost = 15
       self.description = "Sos olarak zeytin seçtiniz."
       
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Mantar(Decorator):

    def __init__(self):
       self.cost = 20
       self.description = "Sos olarak mantar seçtiniz."
       
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class KeciPeyniri(Decorator):

    def __init__(self):
       self.cost = 25
       self.description = "Sos olarak keçi penyiri seçtiniz."
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Et(Decorator):

    def __init__(self):
       self.cost = 30
       self.description = "Sos olarak et seçtiniz."
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Sogan(Decorator):

    def __init__(self):
       self.cost = 35
       self.description = "Sos olarak soğan seçtiniz."
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Misir(Decorator):

    def __init__(self):
       self.cost = 40
       self.description = "Sos olarak mısır seçtiniz."
    
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
