class Pizza:

    def __init__(self, cost, description):
        self.cost = 50
        self.description = "Pizza includes only cheese"
       
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost



class Klasik(Pizza):

    def __init__(self):
        self.cost = 100
        self.description = "Klasik pizza includes cheese and sausage!"        
    
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description


class Margherita(Pizza):

    def __init__(self):
        self.cost = 125
        self.description = "Margherita pizza includes cheese and tomato!" 
    
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class TurkPizza(Pizza):

    def __init__(self):
        self.cost = 150
        self.description = "Turk Pizza includes cheese and sausage and pepper!"
    
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class DominosPizza(Pizza):
    def __init__(self):
        self.cost = 200
        self.description = "Dominos pizza includes cheese and sausage and mushroom!"
    
    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

