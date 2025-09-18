class Person:
    def __init__(self, name):
        self.name = name
        print("hi, create", self.name)
    
    # method 생성
    def talk(self):
        print("안녕하세요. 저는 ", self.name,"입니다.")

    
person1 = Person("Mindun1") # hi, create Mindun1
print(person1)              # <__main__.Person object at 0x104989be0>
person1.talk()              # 안녕하세요. 저는  Mindun1 입니다.

person2 = Person("Mindun2") # hi, create Mindun2
print(person2)              # <__main__.Person object at 0x104933390>
person2.talk()              # 안녕하세요. 저는  Mindun2 입니다.