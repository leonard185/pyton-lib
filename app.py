class person:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age

    def greet(self):
        print(f'Hello my name is {self.name} and I am {self.age} years old')

person_one = person (1, 'John', 25, 'Male')
person_two = person (2, 'Jane', 30, 'Female')
person_one.greet()

print(person_one.id, person_one.name, person_one.age, person_one.gender)
print(person_two.id,person_two.name,person_two.age,person_two.gender )
