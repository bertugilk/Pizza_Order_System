class Pizza:
    def __init__(self):
        self.cost = 0
        self.description = "description"
        self.piece = 0
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
    def get_piece(self):
        return self.piece

class Classic_Pizza(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.cost=80
        self.description="Klasik pizza: İçinde sucuk, zeytin, mısır, biber, ve mantar bulunur."
        self.piece = 0
class Margherita(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.cost=100
        self.description = "Margarita pizza: (İtalyanca: Pizza Margherita), domates, " \
                           "mozarella, fesleğen, zeytinyağı ve tuzla yapılan Napoli pizzasıdır."
        self.piece = 0
class Turk_Pizzasi(Pizza):
    def __init__(self):
        Pizza.__init__(self)
        self.cost=150
        self.description = "Türk Pizza: İçinde sucuk, pastırma, biber, ve mantar bulunur."
        self.piece = 0

class Decorator:
    def __init__(self):
        self.cost = 0
        self.description = "description"
        self.piece = 0
    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description
    def get_piece(self):
        return self.piece

class Olive(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.cost=10
        self.description = "Pizzanız için zeytin sosu."
        self.piece = 0

class Meat(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.cost = 30
        self.description = "Pizzanız için et sosu."
        self.piece = 0

class Onion(Decorator):
    def __init__(self):
        Decorator.__init__(self)
        self.cost = 20
        self.description = "Pizzanız için soğan sosu."
        self.piece = 0