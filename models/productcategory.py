class ProductCategory:
    id = None
    name = None
    is_night_use = False
    is_day_use = False

    def __init__(self, id, name, is_night_use, is_day_use):
        self.id = id
        self.name = name
        self.is_night_use = is_night_use
        self.is_day_use = is_day_use
        
        
