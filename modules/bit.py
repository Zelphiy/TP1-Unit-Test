from enum import Enum

class Bit(Enum):
    BIT_0 = 0
    BIT_1 = 1

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Bit.{self.name}"