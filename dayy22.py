class Person():
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary


#Membuat objek oPerson1
oPerson1 = Person('diloo', 90000)


#Mengakses variabel salary dengan method getSalary()
print(oPerson1.getSalary())

#mengubah nilai variabel name dengan method setName()
oPerson1.setName('diloo')

#mengubah nilai variabel salary dengan method setSalary()
oPerson1.setSalary(100000)

#mengakses variabel name dan salary
print(oPerson1.getName())
print(oPerson1.getSalary())
