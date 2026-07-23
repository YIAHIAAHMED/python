
# base class, parent class, common attribute + functionality
# derived class, child class, uncommon attribute + functionality

# common gulu niye asbo
class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

     
    def run(self):
        return f'Running laptor: {self.brand}'

class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd

    
    def coding(self):
        return f'learning python and practicing'
    
class Phone:
    def __init__(self, dual_sim):
        self.dual_sim = dual_sim


    def phone_call(self, number, text):
        return f'sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, pixel):
    
        self.pixel = pixel


    def change_lens(self):
        pass

    