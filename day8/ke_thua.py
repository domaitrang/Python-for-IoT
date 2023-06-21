# tao 1 class Student ke thua tu Person co them thuoc tinh age

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"person[name={self.name}, age={self.age}]"
    
# class student extends person
class student(person):
    def __init__(self, id, name, age):
        super().__init__(name, age)
        self.id = id
    
    # Ghi de lai info -> lat xu ly tiep
    def info(self):
        return f"student[id={self.id},{super().info()}]"


p1 = person("Nguyen Van A", 20)
s1 = student(123,"Nguyen Van B", 18)
print(p1.info())
print(s1.info())



