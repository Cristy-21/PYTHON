class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls):
        return cls(salmon = 2, tuna = 2, shrimp = 2, squid = 0)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon = 0, tuna = 10, shrimp = 0, squid = 1)

boris = SushiPlatter(salmon = 8, tuna = 4, shrimp = 5, squid = 10)
print(boris.salmon)

lunch_eater = SushiPlatter.lunch_special_A()
print(lunch_eater.salmon)
print(lunch_eater.squid)

tuna_fan = SushiPlatter.tuna_lover()
print(tuna_fan.tuna)





class Chocolate():
    def __init__(self,cacao_content):
        self.cacao_content=cacao_content
         
    @classmethod
    def sweet(cls):
        return cls(cacao_content=30)
    
    @classmethod
    def semisweet(cls):
        return cls(cacao_content=50)
        
    @classmethod
    def bittersweet(cls):
        return cls(cacao_content=70)
    
    @classmethod
    def bitter(cls):
        return cls(cacao_content=99)
