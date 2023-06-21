class Person():
    # Phương thức khởi tạo - constructor
    # self tương đương với this, bên java,php, c++...
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    
    def info(self):
        return f"Person[name={self.name}, age={self.age}]"

# Phương thức là một hàm định nghĩa trong class

p1 = Person("Nguyen Van A", 20)
p2 = Person("Nguyen Van B", 21)
print(p1.info())
print(p2.info())

# Nếu muốn p3 = Person("Nguyen Van C") ???
p3 = Person("Nguyen Van C")
print(p3.info())

p4 = Person(age = 22, name = "Nguyen Van D")
print(p4.info())
