
class Test():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_name(self, nice):
        self.name = nice 

    def __str__(self):
        return str(self.name) + str(self.age)

a = Test('cat','test')

print(5/10)