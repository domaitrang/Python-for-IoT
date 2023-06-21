# Link: https://www3.ntu.edu.sg/home/ehchua/programming/java/j3f_oopexercises.html

class account:
    def __init__(self, id, name, balance=0) -> None:
        # __: private
        self.__id = id
        self.__name = name
        self.__balance = balance

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def credit(self, amount):
        self.__balance += amount
        return self.__balance

    def debit(self, amount):
        if (amount <= self.__balance):
            self.__balance -= amount
        else:
            print("Amount exceeded balance")

        return self.__balance

    def transfer_to(self, another, amount):
        # Tai khoan can chuyen A - hien tai
        # Tai khoan dc chuyen B
        if (self.__balance >= amount):
            self.__balance -= amount
            # Cong tien vao tai khoan con lai
            another.__balance += amount
        else:
            print("Amount exceeded balance")
        return self.__balance

    def to_string(self):
        return f"account[id={self.__id},name={self.__name},balance={self.__balance}]"


a1 = account("A101", "Tan Ah Teck", 88)
print(a1.to_string())
a2 = account("A102", "Kumar")
print(a2.to_string())

a1.credit(100)
print(a1.to_string())
a1.debit(50);
print(a1.to_string())
a1.debit(500)
print(a1.to_string())

print("Chuyen khoan a1 sang a2")
a1.transfer_to(a2, 100)
print(a1.to_string())
print(a2.to_string())